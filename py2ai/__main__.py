import ast
import getpass
import json
import os
import string
from argparse import ArgumentParser
from typing import Any, Dict, List, Optional, Tuple

import dotenv

from py2ai.aia import AIAProject
from py2ai.compiler import PythonCompiler

dotenv.load_dotenv('.env')

ap = ArgumentParser(
    prog='py2ai', description='compile and modify .aia projects with Python code'
)

sp = ap.add_subparsers(
    metavar='SUBCOMMAND', help='subcommand to execute', required=True
)

ls = sp.add_parser('ls', help='view contents of an .aia project')
ls.set_defaults(cmd='ls')
ls.add_argument('inaia', help='input .aia file')
ls.add_argument('--json', action='store_true', help='output in json format')

create = sp.add_parser('create', help='create an .aia project')
create.set_defaults(cmd='create')
create.add_argument('name', help='name of the app')
create.add_argument('outaia', help='output .aia file')
create.add_argument(
    '--main-screen',
    '-m',
    metavar='NAME',
    help='the main screen, defaults to the first one',
)
create.add_argument(
    '--package-name',
    '-p',
    metavar='NAME',
    help='the name of the Java package, defaults to '
    'appinventor.<your_username>.<app_name>',
)
create.add_argument(
    '--screen',
    '-s',
    nargs=2,
    metavar=('FILE', 'NAME'),
    action='append',
    default=[],
    help='add a screen compiled from Python file with a given name',
)
create.add_argument(
    '--asset', '-a', metavar='file', action='append', default=[], help='add an asset'
)

modify = sp.add_parser('modify', help='modify an .aia file')
modify.set_defaults(cmd='modify')
modify.add_argument('inaia', help='input .aia file')
modify.add_argument('outaia', help='output .aia file')
modify.add_argument(
    '--add-screen',
    '-a',
    nargs=2,
    metavar=('FILE', 'NAME'),
    action='append',
    default=[],
    help='add a screen compiled from Python file with a given name',
)
modify.add_argument(
    '--delete-screen',
    '-d',
    metavar='NAME',
    action='append',
    default=[],
    help='delete a screen from the project',
)
modify.add_argument(
    '--add-asset',
    '-A',
    metavar='FILE',
    action='append',
    default=[],
    help='add an asset to the project',
)
modify.add_argument(
    '--delete-asset',
    '-D',
    metavar='FILE',
    action='append',
    default=[],
    help='delete an asset from the project',
)

args = ap.parse_args()


def _normalize(name):
    return name.lower().replace(' ', '_')


def _check_package(name):
    return (
        all(c in string.ascii_letters + string.digits + '_.' for c in name)
        and '..' not in name
        and all(f'.{d}' not in name for d in string.digits)
    )


def _dump_component(component, indent):
    name = component['$Name']
    type = component['$Type']
    if name.startswith('__py2ai__'):
        return
    if type == 'Form':
        type = 'Screen'
    print(f'{indent}{name} ({type}', end='')
    for key, value in component.items():
        if not key.startswith('$') and key != 'Uuid':
            print(f', {key}={value}', end='')
    print(')')
    children = component.get('$Components', [])
    indent += '  '
    for child in children:
        _dump_component(child, indent)


def _run_ls(args, ap):
    inaia: str = args.inaia
    out_json: bool = args.json

    project = AIAProject(inaia)
    data: Dict[str, Any] = {
        'name': None,
        'package': project.package_name,
        'main': project.main_name,
        'properties': dict(project.properties),
    }

    data['screens'] = screens = []
    for screen in project.screens:
        screens.append(
            {'name': screen.name, 'blk': screen.blockly.to_xml(), 'scm': screen.schema}
        )
        if screen.name == project.main_name:
            data['name'] = screen.schema['Properties']['AppName']

    data['assets'] = assets = list(project.assets)

    if out_json:
        print(json.dumps(data))
        return

    print('App name:   ', data['name'])
    print('Package:    ', data['package'])
    print('Main screen:', data['main'])

    print()
    print('Screens:')
    for screen in screens:
        _dump_component(screen['scm']['Properties'], '  ')

    if assets:
        print()
        print('Assets:')
        for asset in assets:
            print(' ', asset)


def _run_create(args, ap):
    app_name: str = args.name
    outaia: str = args.outaia
    main_name: Optional[str] = args.main_screen
    package_name: Optional[str] = args.package_name
    screens: List[Tuple[str, str]] = args.screen
    assets: List[str] = args.asset

    if len(screens) < 1:
        ap.error('no screens provided')

    if main_name is None:
        main_name = screens[0][1]

    if package_name is None:
        package_name = f'appinventor.{getpass.getuser()}.{_normalize(app_name)}'
    if not _check_package(package_name):
        ap.error(f'invalid package name {package_name!r}')

    project = AIAProject(package_name=package_name, main_name=main_name)

    compiler = PythonCompiler()
    for screen_file, screen_name in screens:
        with open(screen_file) as f:
            code = f.read()
        node = ast.parse(code)
        screen = compiler.create(node, screen_name, app_name)
        project.screens.append(screen)

    for asset in assets:
        with open(asset, 'rb') as f:
            project.assets[os.path.basename(asset)] = f.read()

    project.save(outaia)


def _run_modify(args, ap):
    inaia: str = args.inaia
    outaia: str = args.outaia
    add_screens: List[Tuple[str, str]] = args.add_screen
    del_screens: List[str] = args.delete_screen
    add_assets: List[str] = args.add_asset
    del_assets: List[str] = args.delete_asset

    project = AIAProject(inaia)

    main_name = project.main_name
    if main_name in del_screens and not any(x[1] == main_name for x in add_screens):
        ap.error('cannot delete the main screen')
    main_screen = project.get_screen(main_name)
    app_name: str = main_screen.schema['Properties'].get('AppName', main_name)

    for _, screen_name in add_screens:
        if screen_name not in del_screens:
            try:
                project.get_screen(screen_name)
            except KeyError:
                pass
            else:
                del_screens.append(screen_name)

    for screen in del_screens:
        try:
            screen = project.get_screen(screen)
            project.screens.remove(screen)
        except KeyError:
            ap.error(f'screen {screen!r} not found')

    for asset in del_assets:
        if asset in project.assets:
            del project.assets[asset]
        else:
            ap.error(f'asset {asset!r} not found')

    compiler = PythonCompiler()
    for screen_file, screen_name in add_screens:
        with open(screen_file) as f:
            code = f.read()
        node = ast.parse(code)
        screen = compiler.create(node, screen_name, app_name)
        project.screens.append(screen)

    for asset in add_assets:
        with open(asset, 'rb') as f:
            project.assets[os.path.basename(asset)] = f.read()

    project.save(outaia)


if args.cmd == 'ls':
    _run_ls(args, ap)
elif args.cmd == 'create':
    _run_create(args, ap)
elif args.cmd == 'modify':
    _run_modify(args, ap)

import json, requests
from bs4 import BeautifulSoup, Tag, PageElement
from copy import deepcopy as copy

PAGES = [
    'userinterface',
    'layout',
    'media',
    'animation',
    'sensors',
    'social',
    'storage',
    'connectivity',
    'experimental',
]
BASE_URL = 'http://ai2.appinventor.mit.edu/reference/components/%s.html'
DATA = {'desc': None, 'properties': [], 'events': [], 'methods': []}

PROPERTY_TYPES = {
    'ChatBot': {'Model': 'str', 'Provider': 'str', 'System': 'str', 'Token': 'str'},
    'FirebaseDB': {'Persist': 'bool', 'ProjectBucket': 'str'},
}


def _get_type(clazz, comp=..., prop=...):
    ret = (
        'str'
        if 'text' in clazz
        else 'bool'
        if 'boolean' in clazz
        else 'int'
        if 'number' in clazz
        else 'list'
        if 'list' in clazz
        else 'dict'
        if 'dictionary' in clazz
        else 'Component'
        if 'component' in clazz
        else 'Any'
        if 'any' in clazz
        else 'enums.Color'
        if 'color' in clazz
        else 'enums.FileScope'
        if 'FileScopeEnum' in clazz
        else 'enums.Instant'
        if 'InstantInTime' in clazz
        else 'unknown'
    )
    if ret == 'unknown':
        if comp in PROPERTY_TYPES and prop in PROPERTY_TYPES[comp]:
            return PROPERTY_TYPES[comp][prop]
        print(f'ERROR: Unknown type: {clazz}, default to str')
        ret = 'str'
    return ret


index = []


def get_text(self):
    return (
        self.get_text()
        .replace('â\x80\x98', "'")
        .replace('â\x80\x99', "'")
        .replace('â\x80\x9c', '"')
        .replace('â\x80\x9d', '"')
        .replace('\n ', '\n')
    )


# patch .text so the quotation marks are ok
PageElement.text = property(get_text)  # type: ignore


for page in PAGES:
    data = {}
    print(f'fetching page {page}')
    url = BASE_URL % page
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print('finding components...')
    article = soup.select_one('article.documentation')
    assert article
    comp = None
    last_class = ''
    article_name = page
    for element in article:
        if not isinstance(element, Tag):
            continue
        if element.name == 'h1':
            article_name = element.text
            print(f'article name: {article_name}')
        if element.name == 'h2':
            comp = element.text
            data[comp] = copy(DATA)
            print(f'found component {comp}')
        elif element.name == 'p':
            if comp is None or data[comp]['desc']:
                continue
            data[comp]['desc'] = element.text
            # print('found desc for component')
        if 'class' not in element.attrs and 'properties' in last_class:
            element.attrs['class'] = 'properties'
        if 'class' not in element.attrs:
            continue
        if 'properties' in element.attrs['class']:
            # print('found properties for component')
            prop_name = None
            for d in element:
                if not isinstance(d, Tag):
                    continue
                if d.name == 'dt':
                    prop_name = d.text
                    clazz = d.attrs['class']
                    prop = {
                        'name': prop_name,
                        'type': _get_type(clazz, comp, prop_name),
                        'ro': 'ro' in clazz,
                        'do': 'do' in clazz,
                        'bo': 'bo' in clazz and prop_name not in ['Width', 'Height'],
                        'desc': None,
                    }
                    data[comp]['properties'].append(prop)
                    # print(f'found property {prop_name}')
                elif d.name == 'dd':
                    if prop_name is None:
                        continue
                    data[comp]['properties'][-1]['desc'] = d.text
                    # print('found desc for property')
        elif 'events' in element.attrs['class']:
            # print('found properties for component')
            event_name = None
            for d in element:
                if not isinstance(d, Tag):
                    continue
                if d.name == 'dt':
                    event_name = d.text.partition('(')[0]
                    event = {'name': event_name, 'args': [], 'desc': None}
                    for arg in d.select('em'):
                        arg_name = arg.text
                        arg_type = _get_type(arg.attrs['class'])
                        event['args'].append({'name': arg_name, 'type': arg_type})
                    data[comp]['events'].append(event)
                    # print(f'found event {event_name}')
                elif d.name == 'dd':
                    if event_name is None:
                        continue
                    data[comp]['events'][-1]['desc'] = d.text
                    # print('found desc for event')
        elif 'methods' in element.attrs['class']:
            # print('found methods for component')
            method_name = None
            for d in element:
                if not isinstance(d, Tag):
                    continue
                if d.name == 'dt':
                    method_name = d.text.partition('(')[0].strip()
                    method = {
                        'name': method_name,
                        'args': [],
                        'returns': None,
                        'desc': None,
                    }
                    if 'returns' in d.attrs['class']:
                        method['returns'] = _get_type(d.attrs['class'])
                    for arg in d.select('em'):
                        arg_name = arg.text
                        arg_type = _get_type(arg.attrs['class'])
                        method['args'].append({'name': arg_name, 'type': arg_type})
                    data[comp]['methods'].append(method)
                    # print(f'found method {method_name}')
                elif d.name == 'dd':
                    if method_name is None:
                        continue
                    data[comp]['methods'][-1]['desc'] = d.text
                    # print('found desc for method')
        if element.name == 'dl':
            last_class = element.attrs['class']
    print(f'finished page {page}')
    index.append({'name': article_name, 'page': page, 'contents': data})

with open('components.json', 'w') as f:
    json.dump(index, f)

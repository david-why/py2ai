from setuptools import setup

setup(
    name='py2ai',
    version='0.2',
    description='Create and modify AppInventor .aia projects with Python',
    author='david-why',
    packages=['py2ai'],
    package_data={'py2ai': ['lib.xml', '*.pyi']},
    install_requires=[]
)

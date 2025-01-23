from setuptools import setup, find_packages

setup(
    name='ambassador',
    version='1.0.0',
    description='Hybrid Penetration Testing Tool',
    author='Shay Giladi',
    author_email='shaygiladi97@gmail.com',
    packages=find_packages(include=['utils', 'menus', 'modules']),
    install_requires=[
        'tqdm',
        'platform',
        'shutil',
        'subprocess',
        'time',
        'os',
    ],
    entry_points={
        'console_scripts': [
            'ambassador = ambassador:main',
        ],
    },
)
from setuptools import setup

setup(
    name= 'pwHash',
    version = '0.1.0',
    packages = ['pwHash'],
    entry_points = {
        'console_scripts': [
            'pwHash = pwHash.__main__:hashThis'
        ]
    },
    install_requires = ['click']
    )

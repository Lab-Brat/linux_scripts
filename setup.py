from setuptools import setup

setup(
    name='admin',
    version='0.1.0',
    py_modules=['yourscript'],
    install_requires=[
        'Click',
	'paramiko',
	'requests',
    ],
    entry_points={
        'console_scripts': [
            'admin = admin:adm',
        ],
    },
)


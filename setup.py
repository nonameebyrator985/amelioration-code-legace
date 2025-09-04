from setuptools import setup

setup(
    name='amelioration_code_heire',
    version='0.1',
    packages=['src'],  # Updated packages list
    install_requires=[],
    entry_points={
        'console_scripts': ['ameliorer=main:main'],
    },
)
"""Setup file for data structures/ linkedlist file."""

from setuptools import setup


setup(
    name="Linked List",
    description="A project to setup linked lists.",
    version=0.1,
    author="Reggie & Rachael",
    author_email="rachael.wisecarver@gmail.com",
    license="MIT",
    py_modules=['linked_list.py'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': [
            "linked_list = linked_list:main"
        ]
    }
)
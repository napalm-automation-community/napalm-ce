"""setup.py file."""
from setuptools import setup, find_packages

__author__ = 'Hao Tang <thddaniel92@gmail.com>'

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

with open("README.md", "r") as fs:
    long_description = fs.read()

setup(
    name="napalm-ce",
    version="0.2.0",
    packages=find_packages(exclude=("test*",)),
    author="Hao Tang",
    author_email="thddaniel92@gmail.com",
    description="NAPALM driver for Huawei CloudEngine switches",
    license="Apache 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation-community/napalm-ce",
    include_package_data=True,
    install_requires=reqs,
)

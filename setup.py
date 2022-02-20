# Copyright (c) 2021 Åke Forslund
#
# This file is part of Mycroft Skills Manager
# (see https://github.com/MatthewScholefield/mycroft-light).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import sys
from setuptools import setup


with open("README.md", "r") as fh:
    long_desc = fh.read()


def load_requirements(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base_dir, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]


def required():
    """Load appropriate requirements file."""
    if sys.version_info[:2] > (3, 6):
        return load_requirements("requirements.txt")
    else:
        return load_requirements("requirements-old.txt")


setup(
    name='combo_lock',
    version='0.2.2',
    packages=['combo_lock'],
    package_data={
      '*': ['*.txt', '*.md']
    },
    include_package_data=True,
    install_requires=required(),
    url='https://github.com/forslund/combo-lock',
    license='Apache-2.0',
    author='Åke Forslund, JarbasAI',
    author_email='ake.forslund@gmail.com, '
                 'jarbasai@mailfence.com',
    description='A combined process and thread lock',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)

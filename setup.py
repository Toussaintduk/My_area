from setuptools import setup,find_packages
setup(
name='my_area',
version='0.1',
packages=find_packages(exclude=['tests*']),
license='MIT',
description='EDSA example python package',
long_description=open('README.MD').read(),
install_requires=['numpy'],
url='https://example.com',
author='Dukundimna Toussaint',
author_email='dukundesaint@gmail.com',



)
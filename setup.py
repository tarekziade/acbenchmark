import sys
from setuptools import setup, find_packages

install_requires = []
description = ''
classifiers = ["Programming Language :: Python",
               "License :: OSI Approved :: Apache Software License",
               "Development Status :: 5 - Production/Stable",
               "Programming Language :: Python :: 3 :: Only"]


setup(name='acbenchmark',
      version="0.1",
      packages=find_packages(),
      description=("acbenchmark"),
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers,
      install_requires=install_requires,
      entry_points="""
      [console_scripts]
      acb = acb.run_desktop:main
      """)

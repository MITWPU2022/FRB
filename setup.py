"""
setup.py -- setup script for use of packages.
"""
from setuptools import setup, find_packages

__version__ = '0.0.1'
#
# with open("README.md", "r") as fh:
#     long_description = fh.read()

entry_points = {
    'console_scripts' : [
        'watutil = FRB.search_FRB:cmd_tool',
        'rawutil = FRB.guppi:cmd_tool',
        'fil2h5 = FRB.fil2h5:cmd_tool',
        'h52fil = FRB.h52fil:cmd_tool',
        'h5diag = FRB.h5diag:cmd_tool',
        'bl_scrunch = FRB.bl_scrunch:cmd_tool',
        'matchfils = FRB.match_fils:cmd_tool',
        'bldice = FRB.dice:cmd_tool',
        'calcload = FRB.calcload:cmd_tool',
        'rawhdr = FRB.rawhdr:cmd_tool',
        'stax = FRB.stax:cmd_tool',
        'stix = FRB.stix:cmd_tool',
        'peek = FRB.peek:cmd_tool',
        'srcname = FRB.srcname:cmd_tool',
     ]
}

with open("requirements.txt", "r") as fh:
    install_requires = fh.readlines()

extras_require = {
      'full': [
          'pyslalib',
      ]
}

setup(name='FRB_Finder',
      version=__version__,
      description='Python package for FRB',
      long_description='long_description',
      long_description_content_type='text/markdown',
      license='',
      install_requires=install_requires,
      url='',
      author='',
      author_email='',
      entry_points=entry_points,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      classifiers=[
          'Development Status :: DEV',
          'Environment :: Console',
          'Natural Language :: English',
          'Operating System :: POSIX :: Windows 11',
          'Programming Language :: Python :: 3.8',
          'Intended Audience :: Research',
          'Topic :: CSE :: AIML',
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'pyslalib'],
      test_suite="FRBTEST",
)

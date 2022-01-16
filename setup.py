from setuptools import setup, find_packages
__version__ = '0.0.2'
#
# with open("README.md", "r") as fh:
#     long_description = fh.read()

entry_points = {
    'console_scripts' : [
        'search_FRB = FRB.search_FRB:cmd_tool',
     ]
}

with open("requirements.txt", "r") as fh:
    install_requires = fh.readlines()

extras_require = {
      'full': [
          'pyslalib',
      ]
}

setup(name='FRB',
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
          'Operating System :: Windows :: 11',
          'Programming Language :: Python :: 3.8',
          'Intended Audience :: Researcher',
          'Topic :: CSE :: AIML',
      ],
      #setup_requires=['pytest-runner'],
      #tests_require=['pytest', 'pyslalib'],
      #test_suite="FRBTEST",
)

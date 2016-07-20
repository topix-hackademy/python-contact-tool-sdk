import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except IOError:
    README = ''

version = "0.0.1"

#os.system('pip install ADDITIONAL-REQ')

setup(name='contactsdk',
      version=version,
      description="Python package used to interact with TOP-IX Contact Tool",
      long_description=README,
      author='alexcomu',
      license='MIT',
      zip_safe=False,
      packages=['contactsdk', ],
      entry_points={
          'console_scripts': [
              'contactsdk = contactsdk.main:main'
          ]
      },
      install_requires=[
          "configparser",
          "requests",
      ]
)



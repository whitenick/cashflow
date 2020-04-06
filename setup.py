from setuptools import setup 

setup(
   name='collect',
   version='1.0',
   description='A useful module',
   author='Nick White',
   author_email='nw.white22@gmail.com',
   packages=['collect'],  #same as name
   install_requires=['requests', 'flask'], #external packages as dependencies
)
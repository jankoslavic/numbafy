desc = """\
This a alpha package to lambdify SymPy expressions with Numba

For a showcase see: https://github.com/jankoslavic/numbafy/blob/master/Showcase.ipynb
=============

"""

#from distutils.core import setup, Extension
from setuptools import setup, Extension
setup(name='numbafy',
      version='0.51',
      author='Janko Slavič',
      author_email='janko.slavic@fs.uni-lj.si',
      url='https://github.com/jankoslavic/numbafy',
      py_modules=['numbafy'],
      long_description=desc,
      install_requires=['sympy']
      )

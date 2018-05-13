This a alpha package to lambdify SymPy expressions with Numba

For a showcase see: https://github.com/jankoslavic/numbafy/blob/master/Showcase.ipynb
=============

Simple example
..code-block:: python
    import sympy as sym
    from numba import jit

    a, b, c = sym.symbols('a, b, c')

    constants = {c: 1.4}

    expression = c * a**b
    parameters = (a, b)

    num = numbafy(expression=expression, parameters=parameters, constants=constants, use_cse=True)
    exec(num)
    result = numbafy_func(a=2.0, b=3.0)
    print(result)


|travis|

|binder| to test the *Showcase.ipynb*.

.. |binder| image:: http://mybinder.org/badge.svg 
   :target: http://mybinder.org:/repo/jankoslavic/numbafy
.. |travis| image:: https://travis-ci.org/openmodal/lvm_read.svg?branch=master
    :target: https://travis-ci.org/jankoslavic/numbafy


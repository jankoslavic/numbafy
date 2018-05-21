This a alpha package to lambdify SymPy expressions with Numba

For a showcase see: https://github.com/jankoslavic/numbafy/blob/master/Showcase.ipynb
=============

Simple example:

    import sympy as sym

    from numba import jit

    # this is a very basic example; numbafy shines with huge expression

    a, b, c = sym.symbols('a, b, c')

    constants = {c: 1.4}

    expression = c * a**b

    parameters = (a, b)

    num = numbafy(expression=expression, parameters=parameters, constants=constants, use_cse=True)

    exec(num)

    result = numbafy_func(a=2.0, b=3.0)

    print(result)

    >>> 11.2

For a more complete example with huge expression see the Showcase.ipynb.

For speed comparison see: https://twitter.com/jankoslavic/status/995748211313774592.


|binder| to test the *Showcase.ipynb*.

.. |binder| image:: http://mybinder.org/badge.svg
   :target: http://mybinder.org:/repo/jankoslavic/numbafy

This a alpha package to lambdify SymPy expressions with Numba

For a showcase see: https://github.com/jankoslavic/numbafy/blob/master/Showcase.ipynb
=============

Simple example

.. code-block:: python
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
    >>> 11.2

For a more complete example with huge expression see the Showcase.ipynb.


|binder| to test the *Showcase.ipynb*.

.. |binder| image:: http://mybinder.org/badge.svg
   :target: http://mybinder.org:/repo/jankoslavic/numbafy

# Python-Basics
Goes Over the Basics of Python With Lists, List Comprehension, Generators, and Classes.

Sample Runs:
>>> dict_extend({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400})
{'a': [100, 300], 'b': [200, 200], 'c': [300], 'd': [400]}
>>> dict_to_table({'T1': [1, 2, 3, 4], 'T2': [5, 6, 7, 8], 'T3': [9, 10, 11, 12]})
[('T1', 'T2', 'T3'), (1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
>>> list(suffixes((1, 2, 3, 4)))
[(1, 2, 3, 4), (2, 3, 4), (3, 4), (4,), ()]
>>> camel_case("t0_cAMeL_CaSe")
'toCamelCase'
>>> f1, f2, f3, f4 = Fraction(14, -25), Fraction(7, 9), Fraction(1, 3), Fraction(6, 5)
>>> print(f1.get_fraction())
(14, -25)
>>> print(f1)
14/-25
>>> f5 = -f1 * (f2 + f3) / f4; print(f5)
-2100.0/-4050.0
>>> f5.simplify(); print(f5)
14.0/27.0
>>> f5()
0.5185185185185185

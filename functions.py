import cmath
import statistics
import operator

_normal = statistics.NormalDist()

function_list = {
    "abs": abs,
    "arg": cmath.phase,
    "conj": operator.methodcaller("conjugate"),
    "Im": operator.attrgetter("imag"),
    "Re": operator.attrgetter("real"),
    "sgn": lambda x: 0 if x == 0 else (1 if x > 0 else -1),
    "sin": cmath.sin,
    "cosec": lambda x: 1 / cmath.sin(x),
    "csc": lambda x: 1 / cmath.sin(x),
    "cos": cmath.cos,
    "sec": lambda x: 1 / cmath.cos(x),
    "tan": cmath.tan,
    "cot": lambda x: 1 / cmath.tan(x),
    "sinh": cmath.sinh,
    "cosh": cmath.cosh,
    "tanh": cmath.tanh,
    "asin": cmath.asin,
    "arcsin": cmath.asin,
    "acos": cmath.acos,
    "arccos": cmath.acos,
    "atan": cmath.atan,
    "arctan": cmath.atan,
    "sqrt": cmath.sqrt,
    "ln": cmath.log,
    "lg": cmath.log10,
    "normcdf": _normal.cdf,
    "normpdf": _normal.pdf,
    "invnorm": _normal.inv_cdf,
}


symbols = '''
+
-
*
/
//
%
^
!
P
C
=
=>
&&
||
<
<=
>
>=
==
!=
<*
<==
>*
>==
===
!==
?
:
@
$
.
><
</
/>
<+>
;
'''
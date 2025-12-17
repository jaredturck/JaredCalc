import cmath, math
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
    "sin": math.sin,
    "cosec": lambda x: 1 / math.sin(x),
    "csc": lambda x: 1 / math.sin(x),
    "cos": math.cos,
    "sec": lambda x: 1 / math.cos(x),
    "tan": math.tan,
    "cot": lambda x: 1 / math.tan(x),
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "asin": math.asin,
    "arcsin": math.asin,
    "acos": math.acos,
    "arccos": math.acos,
    "atan": math.atan,
    "arctan": math.atan,
    "sqrt": math.sqrt,
    "ln": math.log,
    "lg": math.log10,
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
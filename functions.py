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

constants = {
    "zero": 0.0,
    "one": 1.0,
    "two": 2.0,
    "three": 3.0,
    "four": 4.0,
    "ten": 10.0,
    "half": 0.5,
    "onePointOne": 1.1,
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": math.inf,
    "nan": math.nan,
    "ln1_1": math.log(1.1),
    "ln2": math.log(2.0),
    "ln10": math.log(10.0),
    "sqrt2": math.sqrt(2.0),
    "sqrt_2pi": math.sqrt(2.0 * math.pi),
    "imag_i": 1j,
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
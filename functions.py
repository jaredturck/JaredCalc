import math
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
    "acosh": math.acosh,
    "asinh": math.asinh,
    "atan2": math.atan2,
    "atanh": math.atanh,
    "ceil": math.ceil,
    "comb": math.comb,
    "copysign": math.copysign,
    "degrees": math.degrees,
    "dist": math.dist,
    "erf": math.erf,
    "erfc": math.erfc,
    "exp": math.exp,
    "expm1": math.expm1,
    "fabs": math.fabs,
    "factorial": math.factorial,
    "floor": math.floor,
    "fmod": math.fmod,
    "frexp": math.frexp,
    "fsum": math.fsum,
    "gamma": math.gamma,
    "gcd": math.gcd,
    "hypot": math.hypot,
    "isclose": math.isclose,
    "isfinite": math.isfinite,
    "isinf": math.isinf,
    "isnan": math.isnan,
    "isqrt": math.isqrt,
    "lcm": math.lcm,
    "ldexp": math.ldexp,
    "lgamma": math.lgamma,
    "log": math.log,
    "log10": math.log10,
    "log1p": math.log1p,
    "log2": math.log2,
    "modf": math.modf,
    "nextafter": math.nextafter,
    "perm": math.perm,
    "pow": math.pow,
    "prod": math.prod,
    "radians": math.radians,
    "remainder": math.remainder,
    "trunc": math.trunc,
    "ulp": math.ulp,
    "cbrt": math.cbrt,
    "exp2": math.exp2,
    "sumprod": math.sumprod,
    "fma": math.fma,
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

symbols = {
    "!":   (12, "postfix"), # added factorial operator
    "$":   (12, "postfix"), # add currency symbol
    '£':   (12, "postfix"), # add currency symbol
    "^":   (11, "right"), # add power operator
    "**":  (11, "right"), # add power operator
    "@":   (10, "left"), # skip for now
    "</":  (10, "left"), # skip for now
    "/>":  (10, "left"), # skip for now
    "P":   (9, "left"), # add permutation operator
    "C":   (9, "left"), # add combination operator
    "*":   (8, "left"), # multiply operator
    "/":   (8, "left"), # divide operator
    "//":  (8, "left"), # floor division operator
    "%":   (8, "left"), # modulus operator
    ".":   (8, "left"), # multiply operator
    "><":  (8, "left"), # skip for now
    "+":   (7, "left"), # addition operator
    "-":   (7, "left"), # subtraction operator
    "<+>": (7, "left"), # skip for now
    "<":   (6, "left"), # added less than operator
    "<=":  (6, "left"), # added less than or equal to operator
    ">":   (6, "left"), # added greater than operator
    ">=":  (6, "left"), # added greater than or equal to operator
    "<*":  (6, "left"), # skip for now
    "<==": (6, "left"), # add strict less than or equal to operator
    ">*":  (6, "left"), # skip for now
    ">==": (6, "left"), # add strict greater than or equal to operator
    "==":  (5, "left"), # add equality operator
    "!=":  (5, "left"), # add inequality operator
    "===": (5, "left"), # add strict equality operator
    "!==": (5, "left"), # add strict inequality operator
    "&&":  (4, "left"),
    "||":  (3, "left"),
    "=":   (2, "right"),
    "=>":  (2, "right"),
    "?":   (1, "ternary"),
    ":":   (1, "ternary"),
    ";":   (0, "left"),
}
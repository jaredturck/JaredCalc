# import math
import cmath
import statistics
import operator
import time

def timeit(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.10f} seconds")
        return result

    return wrapper

class Func:
    PI = 3.141592653589793
    E = 2.718281828459045
    TAU = 6.283185307179586
    HALF_PI = 1.5707963267948966
    LN1_1 = 0.09531017980432493
    LN2 = 0.6931471805599453
    LN10 = 2.302585092994046
    SQRT2 = 1.4142135623730951
    SQRT_2PI = 2.5066282746310002

    @staticmethod
    def sinFn(x):
        ''' Compute sine using Taylor series expansion '''
        
        # Reduce to range [-π, π]
        if abs(x) > Func.PI:
            x = ((x + Func.PI) % (Func.TAU)) - Func.PI

        # Reduce to range [-π/2, π/2]
        if x > Func.HALF_PI:
            x = Func.PI - x
        elif x < -Func.HALF_PI:
            x = -Func.PI - x

        s = 0.0
        term = x
        n = 1
        x2 = x * x

        while True:
            p = s
            s += term
            if s == p:
                break

            term *= -x2 / ((n + 1) * (n + 2))
            n += 2

        return s

_normal = statistics.NormalDist()

function_list = {
    "abs": abs,
    "arg": cmath.phase,
    "conj": operator.methodcaller("conjugate"),
    "Im": operator.attrgetter("imag"),
    "Re": operator.attrgetter("real"),
    "sgn": lambda x: 0 if x == 0 else (1 if x > 0 else -1),
    "sin": Func.sinFn,
    "cosec": lambda x: 1 / Func.sinFn(x),
    "csc": lambda x: 1 / Func.sinFn(x),
    "cos": Func.cosFn,
    "sec": lambda x: 1 / Func.cosFn(x),
    "tan": Func.tanFn,
    "cot": lambda x: 1 / Func.tanFn(x),
    "sinh": Func.sinhFn,
    "cosh": Func.coshFn,
    "tanh": Func.tanhFn,
    "asin": Func.asinFn,
    "arcsin": Func.asinFn,
    "acos": Func.acosFn,
    "arccos": Func.acosFn,
    "atan": Func.atanFn,
    "arctan": Func.atanFn,
    "sqrt": Func.sqrtFn,
    "ln": Func.lnFn,
    "lg": Func.lgFn,
    "normcdf": _normal.cdf,
    "normpdf": _normal.pdf,
    "invnorm": _normal.inv_cdf,
    "acosh": Func.acoshFn,
    "asinh": Func.asinhFn,
    "atan2": Func.atan2Fn,
    "atanh": Func.atanhFn,
    "ceil": Func.ceilFn,
    "comb": Func.combFn,
    "copysign": Func.copysignFn,
    "degrees": Func.degreesFn,
    "dist": Func.distFn,
    "erf": Func.erfFn,
    "erfc": Func.erfcFn,
    "exp": Func.expFn,
    "expm1": Func.expm1Fn,
    "fabs": Func.fabsFn,
    "factorial": Func.factorialFn,
    "floor": Func.floorFn,
    "fmod": Func.fmodFn,
    "frexp": Func.frexpFn,
    "fsum": Func.fsumFn,
    "gamma": Func.gammaFn,
    "gcd": Func.gcdFn,
    "hypot": Func.hypotFn,
    "isclose": Func.iscloseFn,
    "isfinite": Func.isfiniteFn,
    "isinf": Func.isinfFn,
    "isnan": Func.isnanFn,
    "isqrt": Func.isqrtFn,
    "lcm": Func.lcmFn,
    "ldexp": Func.ldexpFn,
    "lgamma": Func.lgammaFn,
    "log": Func.logFn,
    "log10": Func.log10Fn,
    "log1p": Func.log1pFn,
    "log2": Func.log2Fn,
    "modf": Func.modfFn,
    "nextafter": Func.nextafterFn,
    "perm": Func.permFn,
    "pow": Func.powFn,
    "prod": Func.prodFn,
    "radians": Func.radiansFn,
    "remainder": Func.remainderFn,
    "trunc": Func.truncFn,
    "ulp": Func.ulpFn,
    "cbrt": Func.cbrtFn,
    "exp2": Func.exp2Fn,
    "sumprod": Func.sumprodFn,
    "fma": Func.fmaFn,
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
    "pi": Func.PI,
    "e": Func.E,
    "tau": Func.TAU,
    "ln1_1": Func.LN1_1,
    "ln2": Func.LN2,
    "ln10": Func.LN10,
    "sqrt2": Func.SQRT2,
    "sqrt_2pi": Func.SQRT_2PI,
    "imag_i": 1j,
}

symbols = {
    "!":   (12, "postfix"), # added factorial operator
    "$":   (12, "postfix"), # add currency symbol
    '£':   (12, "postfix"), # add currency symbol
    "^":   (11, "right"), # add power operator
    "**":  (11, "right"), # add power operator
    "@":   (10, "left"), # skip
    "</":  (10, "left"), # skip
    "/>":  (10, "left"), # skip
    "P":   (9, "left"), # add permutation operator
    "C":   (9, "left"), # add combination operator
    "*":   (8, "left"), # multiply operator
    "/":   (8, "left"), # divide operator
    "//":  (8, "left"), # floor division operator
    "%":   (8, "left"), # modulus operator
    ".":   (8, "left"), # multiply operator
    "><":  (8, "left"), # skip
    "+":   (7, "left"), # addition operator
    "-":   (7, "left"), # subtraction operator
    "<+>": (7, "left"), # skip
    "<":   (6, "left"), # added less than operator
    "<=":  (6, "left"), # added less than or equal to operator
    ">":   (6, "left"), # added greater than operator
    ">=":  (6, "left"), # added greater than or equal to operator
    "<*":  (6, "left"), # skip
    "<==": (6, "left"), # add strict less than or equal to operator
    ">*":  (6, "left"), # skip
    ">==": (6, "left"), # add strict greater than or equal to operator
    "==":  (5, "left"), # add equality operator
    "!=":  (5, "left"), # add inequality operator
    "===": (5, "left"), # add strict equality operator
    "!==": (5, "left"), # add strict inequality operator
    "&&":  (4, "left"), # added logical AND operator
    "||":  (3, "left"), # added logical OR operator
    "=":   (2, "right"),
    "=>":  (2, "right"),
    "?":   (1, "ternary"),
    ":":   (1, "ternary"),
    ";":   (0, "left"),
}

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
    def __init__(self):
        self.PI = 3.141592653589793
        self.E = 2.718281828459045
        self.TAU = 6.283185307179586
        self.HALF_PI = 1.5707963267948966
        self.LN1_1 = 0.09531017980432493
        self.LN2 = 0.6931471805599453
        self.LN10 = 2.302585092994046
        self.SQRT2 = 1.4142135623730951
        self.SQRT_2PI = 2.5066282746310002
    
    def expFn(self, x):
        ''' Compute exponential using Taylor series expansion '''
        
        k = int(round(x / self.LN2))
        r = x - k * self.LN2

        s = 1
        term = 1
        n = 1

        while True:
            p = s
            term *= r / n
            s += term
            if s == p:
                break

            n += 1
        
        return s * (2.0 ** k)

    def sinFn(self, x):
        ''' Compute sine using Taylor series expansion '''
        
        # Reduce to range [-π, π]
        if abs(x) > self.PI:
            x = ((x + self.PI) % (self.TAU)) - self.PI

        # Reduce to range [-π/2, π/2]
        if x > self.HALF_PI:
            x = self.PI - x
        elif x < -self.HALF_PI:
            x = -self.PI - x

        s = 0
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
    
    def cosFn(self, x):
        ''' Compute cosine as sin(x/2 - x) '''
        return self.sinFn(self.HALF_PI - x)

    def tanFn(self, x):
        ''' Compute tangent as sine divided by cosine '''
        return self.sinFn(x) / self.cosFn(x)

    def secFn(self, x):
        ''' Compute secant as reciprocal of cosine '''
        return 1 / self.cosFn(x)

    def cscFn(self, x):
        ''' Compute cosecant as reciprocal of sine '''
        return 1 / self.sinFn(x)

    def cotFn(self, x):
        ''' Compute cotangent as reciprocal of tangent '''
        return 1 / self.tanFn(x)

    def sinhFn(self, x):
        ''' Compute hyperbolic sine '''
        ex = self.expFn(x)
        return (ex - 1 / ex) / 2

    def coshFn(self, x):
        ''' Compute hyperbolic cosine '''
        ex = self.expFn(x)
        return (ex + 1 / ex) / 2

    def tanhFn(self, x):
        ''' Compute hyperbolic tangent '''
        ex2 = self.expFn(x * 2)
        return (ex2 - 1) / (ex2 + 1)

_normal = statistics.NormalDist()
functions = Func()

function_list = {
    "abs": abs,
    "arg": cmath.phase,
    "conj": operator.methodcaller("conjugate"),
    "Im": operator.attrgetter("imag"),
    "Re": operator.attrgetter("real"),
    "sgn": lambda x: 0 if x == 0 else (1 if x > 0 else -1),
    "sin": functions.sinFn,
    "cosec": lambda x: 1 / functions.sinFn(x),
    "csc": lambda x: 1 / functions.sinFn(x),
    "cos": functions.cosFn,
    "sec": lambda x: 1 / functions.cosFn(x),
    "tan": functions.tanFn,
    "cot": lambda x: 1 / functions.tanFn(x),
    "sinh": functions.sinhFn,
    "cosh": functions.coshFn,
    "tanh": functions.tanhFn,
    "asin": functions.asinFn,
    "arcsin": functions.asinFn,
    "acos": functions.acosFn,
    "arccos": functions.acosFn,
    "atan": functions.atanFn,
    "arctan": functions.atanFn,
    "sqrt": functions.sqrtFn,
    "ln": functions.lnFn,
    "lg": functions.lgFn,
    "normcdf": _normal.cdf,
    "normpdf": _normal.pdf,
    "invnorm": _normal.inv_cdf,
    "acosh": functions.acoshFn,
    "asinh": functions.asinhFn,
    "atan2": functions.atan2Fn,
    "atanh": functions.atanhFn,
    "ceil": functions.ceilFn,
    "comb": functions.combFn,
    "copysign": functions.copysignFn,
    "degrees": functions.degreesFn,
    "dist": functions.distFn,
    "erf": functions.erfFn,
    "erfc": functions.erfcFn,
    "exp": functions.expFn,
    "expm1": functions.expm1Fn,
    "fabs": functions.fabsFn,
    "factorial": functions.factorialFn,
    "floor": functions.floorFn,
    "fmod": functions.fmodFn,
    "frexp": functions.frexpFn,
    "fsum": functions.fsumFn,
    "gamma": functions.gammaFn,
    "gcd": functions.gcdFn,
    "hypot": functions.hypotFn,
    "isclose": functions.iscloseFn,
    "isfinite": functions.isfiniteFn,
    "isinf": functions.isinfFn,
    "isnan": functions.isnanFn,
    "isqrt": functions.isqrtFn,
    "lcm": functions.lcmFn,
    "ldexp": functions.ldexpFn,
    "lgamma": functions.lgammaFn,
    "log": functions.logFn,
    "log10": functions.log10Fn,
    "log1p": functions.log1pFn,
    "log2": functions.log2Fn,
    "modf": functions.modfFn,
    "nextafter": functions.nextafterFn,
    "perm": functions.permFn,
    "pow": functions.powFn,
    "prod": functions.prodFn,
    "radians": functions.radiansFn,
    "remainder": functions.remainderFn,
    "trunc": functions.truncFn,
    "ulp": functions.ulpFn,
    "cbrt": functions.cbrtFn,
    "exp2": functions.exp2Fn,
    "sumprod": functions.sumprodFn,
    "fma": functions.fmaFn,
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
    "pi": functions.PI,
    "e": functions.E,
    "tau": functions.TAU,
    "ln1_1": functions.LN1_1,
    "ln2": functions.LN2,
    "ln10": functions.LN10,
    "sqrt2": functions.SQRT2,
    "sqrt_2pi": functions.SQRT_2PI,
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

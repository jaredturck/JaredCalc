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
        self.QUARTER_PI = 0.7853981633974483
        self.LN1_1 = 0.09531017980432493
        self.LN2 = 0.6931471805599453
        self.LN10 = 2.302585092994046
        self.SQRT2 = 1.4142135623730951
        self.SQRT_2PI = 2.5066282746310002
    
    def lnFn(self, x):
        ''' Compute neural logarithm using talyor series expansion '''

        if x <= 0:
            raise ValueError('X must be positive for ln')
        
        result = 0.0
        while x >= 2.0:
            x *= 0.5
            result += self.LN2
        
        while x < 1.0:
            x *= 2.0
            result -= self.LN2
        
        if x > self.SQRT2:
            x *= 0.5
            result += self.LN2
        
        y = (x - 1) / (x + 1)
        y2 = y * y
        s = 0
        term = y
        n = 1

        while True:
            p = s
            s += term / n
            if s == p:
                break
            term *= y2
            n += 2
        
        return result + 2.0 * s
    
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
    
    def atanFn(self, x):
        ''' Compute arctangent using Taylor series expansion '''
        if x == 0:
            return 0
        
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        
        base = 0
        factor = 1

        if x > 1:
            x = 1 / x
            base = self.HALF_PI
            factor = -1
        
        limit = self.SQRT2 - 1

        if x > limit:
            x = (x - 1) / (x + 1)
            base += factor * self.QUARTER_PI
        
        s = 0
        term = x
        n = 1
        x2 = x * x

        while True:
            p = s
            s += term / n
            if s == p:
                break
            term *= -x2
            n += 2
        
        return sign * (base + factor * s)
    
    def asinFn(self, x):
        ''' Compute arcsine '''
        if x < -1 or x > 1:
            raise ValueError('X must be in range [-1, 1] for asin')
        if x == 1:
            return self.HALF_PI
        if x == -1:
            return -self.HALF_PI
        
        return self.atanFn(x / self.sqrtFn(1 - x * x))
    
    def acosFn(self, x):
        ''' Compute arccosine '''
        if x < -1 or x > 1:
            raise ValueError('X must be in range [-1, 1] for acos')
        return self.HALF_PI - self.asinFn(x)
    
    def sqrtFn(self, x):
        ''' Square root using Newton's method '''
        if x < 0:
            raise ValueError('X cannot be negative for sqrt')
        if x == 0:
            return 0.0
        
        y = max(x, 1)
        while True:
            p = y
            y = 0.5 * (y + x  / y)
            if y == p:
                break

        return y
    
    def factorialFn(self, x):
        ''' Compute factorial'''
        if x < 0:
            raise ValueError('X cannot be negative for factorial')
        if x <= 1:
            return 1
        n = 1
        for i in range(2, int(x) + 1):
            n *= i
        return n
    
    def gcdFn(self, a, b):
        ''' Compute greatest common divisor using Euclidean algorithm '''
        a = abs(a)
        b = abs(b)
        while b != 0:
            a, b = b, a % b
        return a
    
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
    
    def cosecFn(self, x):
        ''' Compute cosecant '''
        return self.cscFn(x)

    def expm1Fn(self, x):
        ''' Compute exp(x) '''
        return self.expFn(x) - 1

    def exp2Fn(self, x):
        ''' Compute 2 raised to the power x using expFn '''
        return self.expFn(x * self.LN2)
        
    def ldexpFn(self, x, i):
        ''' Compute x * (2 ** i) '''
        return x * (2 ** i)
    
    def logFn(self, x):
        ''' Compute natural logarithm '''
        return self.lnFn(x)

    def log10Fn(self, x):
        ''' Compute base-10 logarithm '''
        return self.lnFn(x) / self.LN10

    def log2Fn(self, x):
        ''' Compute base-2 logarithm '''
        return self.lnFn(x) / self.LN2

    def lgFn(self, x):
        ''' Compute base-10 logarithm '''
        return self.log10Fn(x)

    def log1pFn(self, x):
        ''' Compute natural logarithm of (1 + x) '''
        return self.lnFn(1 + x)
    
    def hypotFn(self, x, y):
        ''' Compute hypotenuse using sqrt(x^2 + y^2) '''
        return self.sqrtFn(x*x + y*y)
    
    def asinhFn(self, x):
        ''' Compute inverse hyperbolic sine '''
        return self.lnFn(x + self.sqrtFn(x * x + 1.0))
    
    def atanhFn(self, x):
        ''' Compute inverse hyperbolic tangent '''
        return 0.5 * self.lnFn((1.0 + x) / (1.0 - x))

    def acoshFn(self, x):
        ''' Compute inverse hyperbolic cosine '''
        return self.lnFn(x + self.sqrtFn(x - 1.0) * self.sqrtFn(x + 1.0))
    
    def radiansFn(self, deg):
        ''' Convert degrees to radians '''
        return deg * (self.PI / 180)
    
    def degreesFn(self, rad):
        ''' Convert radians to degrees '''
        return rad * (180 / self.PI)
    
    def fabsFn(self, x):
        ''' Compute absolute value '''
        return abs(x)
    
    def fmaFn(self, a, b, c):
        ''' Compute fused multiply-add: a * b + c '''
        return a*b + c
    
    def permFn(self, n, k):
        ''' Compute permutations P(n, k) '''
        return self.factorialFn(n) // self.factorialFn(n - k)
    
    def combFn(self, n, k):
        ''' Compute combinations C(n, k) '''
        return self.factorialFn(n) // (self.factorialFn(k) * self.factorialFn(n - k))
    
    def lcmFn(self, a, b):
        ''' Compute least common multiple '''
        return abs(a * b) // self.gcdFn(a, b)
    
    def powFn(self, x, y):
        ''' Compute x to power of y '''
        return x ** y
    
    def floorFn(self, x):
        ''' Compute floor of x '''
        i = int(x)
        return i if x >= 0 or x == i else i - 1
    
    def ceilFn(self, x):
        ''' Compute ceiling of x '''
        i = int(x)
        return i if x <= 0 or x == i else i + 1
    
    def sgnFn(self, x):
        ''' Compute sign of x '''
        if x > 0:
            return 1
        elif x < 0:
            return -1
        return 0
    
    def atan2Fn(self, x, y):
        ''' Compute arctangent two '''

        if x > 0:
            return self.atanFn(y / x)
        if x < 0:
            if y >= 0:
                return self.atanFn(y / x) + self.PI
            return self.atanFn(y / x) - self.PI
        
        if y > 0:
            return self.HALF_PI
        if y < 0:
            return -self.HALF_PI
    
    def copysignFn(self, x, y):
        ''' Returns abs(x) with sign of y '''
        ax = abs(x)
        return -ax if y < 0 else ax

_normal = statistics.NormalDist()
functions = Func()

function_list = {
    "abs": abs,
    "arg": functions.phase,
    "conj": operator.methodcaller("conjugate"),
    "Im": operator.attrgetter("imag"),
    "Re": operator.attrgetter("real"),
    "sgn": functions.sgnFn,
    "sin": functions.sinFn,
    "cosec": functions.cosecFn,
    "csc": functions.cscFn,
    "cos": functions.cosFn,
    "sec": functions.secFn,
    "tan": functions.tanFn,
    "cot": functions.cotFn,
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

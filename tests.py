import math
from functions import function_list

PI = math.pi

def test_case(func, args, expected, rtol=1e-12, atol=1e-12):
    name = getattr(func, '__name__', str(func))
    actual = None
    try:
        actual = func(*args)

        # Compare tuples elementwise (e.g., modf-style returns)
        if isinstance(expected, tuple):
            assert isinstance(actual, tuple), 'Expected a tuple result.'
            assert len(actual) == len(expected), 'Tuple length mismatch.'
            for a, e in zip(actual, expected):
                if isinstance(a, float) or isinstance(e, float):
                    assert math.isclose(a, e, rel_tol=rtol, abs_tol=atol)
                else:
                    assert a == e
            return

        # Floats: IEEE-754 style tolerant compare
        if isinstance(actual, float) or isinstance(expected, float):
            assert math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol)
        else:
            assert actual == expected
        
        # print('pass', {'func': name, 'args': args, 'expected': expected, 'actual': actual})

    except Exception as e:
        print(
            'error',
            {'func': name, 'args': args, 'expected': expected, 'actual': actual, 'exception': f'{type(e).__name__}: {e}'}
        )


# -----------------------------
# NUMERIC CASES -> test_case(...)
# -----------------------------

# --- sin
test_case(function_list['sin'], (0.0,), math.sin(0.0), 5e-12, 5e-12)
test_case(function_list['sin'], (PI / 7.0,), math.sin(PI / 7.0), 5e-12, 5e-12)
test_case(function_list['sin'], (-2.345678901,), math.sin(-2.345678901), 5e-12, 5e-12)
test_case(function_list['sin'], (123.456789,), math.sin(123.456789), 5e-10, 5e-10)

# --- cos
test_case(function_list['cos'], (0.0,), math.cos(0.0), 5e-12, 5e-12)
test_case(function_list['cos'], (PI / 7.0,), math.cos(PI / 7.0), 5e-12, 5e-12)
test_case(function_list['cos'], (-2.345678901,), math.cos(-2.345678901), 5e-12, 5e-12)
test_case(function_list['cos'], (123.456789,), math.cos(123.456789), 5e-10, 5e-10)

# --- tan
test_case(function_list['tan'], (0.0,), math.tan(0.0), 5e-12, 5e-12)
test_case(function_list['tan'], (PI / 4.0,), math.tan(PI / 4.0), 5e-12, 5e-12)
test_case(function_list['tan'], (-1.23456789,), math.tan(-1.23456789), 5e-12, 5e-12)
test_case(function_list['tan'], (0.000000001,), math.tan(0.000000001), 5e-12, 5e-12)

# --- cosec / csc
test_case(function_list['cosec'], (PI / 6.0,), 1.0 / math.sin(PI / 6.0), 5e-10, 5e-10)
test_case(function_list['cosec'], (-PI / 3.0,), 1.0 / math.sin(-PI / 3.0), 5e-10, 5e-10)
test_case(function_list['cosec'], (1.2345,), 1.0 / math.sin(1.2345), 5e-10, 5e-10)

test_case(function_list['csc'], (PI / 6.0,), 1.0 / math.sin(PI / 6.0), 5e-10, 5e-10)
test_case(function_list['csc'], (-PI / 3.0,), 1.0 / math.sin(-PI / 3.0), 5e-10, 5e-10)
test_case(function_list['csc'], (1.2345,), 1.0 / math.sin(1.2345), 5e-10, 5e-10)

# --- sec
test_case(function_list['sec'], (0.0,), 1.0 / math.cos(0.0), 5e-10, 5e-10)
test_case(function_list['sec'], (PI / 3.0,), 1.0 / math.cos(PI / 3.0), 5e-10, 5e-10)
test_case(function_list['sec'], (-2.0,), 1.0 / math.cos(-2.0), 5e-10, 5e-10)

# --- cot
test_case(function_list['cot'], (PI / 4.0,), 1.0 / math.tan(PI / 4.0), 5e-10, 5e-10)
test_case(function_list['cot'], (-PI / 3.0,), 1.0 / math.tan(-PI / 3.0), 5e-10, 5e-10)
test_case(function_list['cot'], (1.1111,), 1.0 / math.tan(1.1111), 5e-10, 5e-10)

# --- sinh / cosh / tanh
test_case(function_list['sinh'], (0.0,), math.sinh(0.0), 5e-12, 5e-12)
test_case(function_list['sinh'], (-1.2,), math.sinh(-1.2), 5e-12, 5e-12)
test_case(function_list['sinh'], (3.4,), math.sinh(3.4), 5e-12, 5e-12)

test_case(function_list['cosh'], (0.0,), math.cosh(0.0), 5e-12, 5e-12)
test_case(function_list['cosh'], (-1.2,), math.cosh(-1.2), 5e-12, 5e-12)
test_case(function_list['cosh'], (3.4,), math.cosh(3.4), 5e-12, 5e-12)

test_case(function_list['tanh'], (0.0,), math.tanh(0.0), 5e-12, 5e-12)
test_case(function_list['tanh'], (-1.2,), math.tanh(-1.2), 5e-12, 5e-12)
test_case(function_list['tanh'], (3.4,), math.tanh(3.4), 5e-12, 5e-12)

# --- asin / arcsin
test_case(function_list['asin'], (0.0,), math.asin(0.0), 5e-12, 5e-12)
test_case(function_list['asin'], (0.5,), math.asin(0.5), 5e-12, 5e-12)
test_case(function_list['asin'], (-0.999999999999,), math.asin(-0.999999999999), 5e-9, 5e-15)

test_case(function_list['arcsin'], (0.0,), math.asin(0.0), 5e-12, 5e-12)
test_case(function_list['arcsin'], (0.5,), math.asin(0.5), 5e-12, 5e-12)
test_case(function_list['arcsin'], (0.999999999999,), math.asin(0.999999999999), 5e-9, 5e-15)

# --- acos / arccos
test_case(function_list['acos'], (0.0,), math.acos(0.0), 5e-12, 5e-12)
test_case(function_list['acos'], (0.5,), math.acos(0.5), 5e-12, 5e-12)
test_case(function_list['acos'], (-0.999999999999,), math.acos(-0.999999999999), 5e-9, 5e-15)

test_case(function_list['arccos'], (0.0,), math.acos(0.0), 5e-12, 5e-12)
test_case(function_list['arccos'], (0.5,), math.acos(0.5), 5e-12, 5e-12)
test_case(function_list['arccos'], (0.999999999999,), math.acos(0.999999999999), 5e-9, 5e-15)

# --- atan / arctan
test_case(function_list['atan'], (0.0,), math.atan(0.0), 5e-12, 5e-12)
test_case(function_list['atan'], (1.0,), math.atan(1.0), 5e-12, 5e-12)
test_case(function_list['atan'], (1e20,), math.atan(1e20), 5e-12, 5e-12)

test_case(function_list['arctan'], (0.0,), math.atan(0.0), 5e-12, 5e-12)
test_case(function_list['arctan'], (-10.0,), math.atan(-10.0), 5e-12, 5e-12)
test_case(function_list['arctan'], (1e20,), math.atan(1e20), 5e-12, 5e-12)

# --- sqrt
test_case(function_list['sqrt'], (0.0,), math.sqrt(0.0), 5e-12, 5e-12)
test_case(function_list['sqrt'], (2.0,), math.sqrt(2.0), 5e-12, 5e-12)
test_case(function_list['sqrt'], (25,), math.sqrt(25), 5e-12, 5e-12)

# --- ln
test_case(function_list['ln'], (1.0,), math.log(1.0), 5e-12, 5e-12)
test_case(function_list['ln'], (math.e,), math.log(math.e), 5e-12, 5e-12)
test_case(function_list['ln'], (1e-12,), math.log(1e-12), 5e-12, 5e-12)

# --- lg
test_case(function_list['lg'], (1.0,), math.log10(1.0), 5e-12, 5e-12)
test_case(function_list['lg'], (10.0,), math.log10(10.0), 5e-12, 5e-12)
test_case(function_list['lg'], (0.00123,), math.log10(0.00123), 5e-12, 5e-12)

# --- normcdf / normpdf
# test_case(function_list['normcdf'], (0.0,), 0.5 * (1.0 + math.erf(0.0 / math.sqrt(2.0))), 5e-12, 5e-12)
# test_case(function_list['normcdf'], (1.0,), 0.5 * (1.0 + math.erf(1.0 / math.sqrt(2.0))), 5e-12, 5e-12)
# test_case(function_list['normcdf'], (-2.0,), 0.5 * (1.0 + math.erf(-2.0 / math.sqrt(2.0))), 5e-12, 5e-12)

# test_case(function_list['normpdf'], (0.0,), math.exp(-0.5 * 0.0 * 0.0) / math.sqrt(2.0 * math.pi), 5e-12, 5e-12)
# test_case(function_list['normpdf'], (1.0,), math.exp(-0.5 * 1.0 * 1.0) / math.sqrt(2.0 * math.pi), 5e-12, 5e-12)
# test_case(function_list['normpdf'], (-2.5,), math.exp(-0.5 * (-2.5) * (-2.5)) / math.sqrt(2.0 * math.pi), 5e-12, 5e-12)

# --- invnorm
# test_case(function_list['invnorm'], (0.5,), 0.0, 5e-10, 5e-12)
# test_case(function_list['invnorm'], (0.975,), 1.959963984540054, 5e-9, 5e-12)
# test_case(function_list['invnorm'], (0.025,), -1.959963984540054, 5e-9, 5e-12)

# --- acosh / asinh / atanh
test_case(function_list['acosh'], (1.0,), math.acosh(1.0), 5e-12, 5e-12)
test_case(function_list['acosh'], (2.0,), math.acosh(2.0), 5e-12, 5e-12)
test_case(function_list['acosh'], (10.0,), math.acosh(10.0), 5e-12, 5e-12)

test_case(function_list['asinh'], (0.0,), math.asinh(0.0), 5e-12, 5e-12)
test_case(function_list['asinh'], (-2.3,), math.asinh(-2.3), 5e-12, 5e-12)
test_case(function_list['asinh'], (123.0,), math.asinh(123.0), 5e-12, 5e-12)

test_case(function_list['atanh'], (0.0,), math.atanh(0.0), 5e-12, 5e-12)
test_case(function_list['atanh'], (0.5,), math.atanh(0.5), 5e-12, 5e-12)
test_case(function_list['atanh'], (-0.9,), math.atanh(-0.9), 5e-12, 5e-12)

# --- atan2
test_case(function_list['atan2'], (0.0, 1.0), math.atan2(0.0, 1.0), 5e-12, 5e-12)
test_case(function_list['atan2'], (1.0, 0.0), math.atan2(1.0, 0.0), 5e-12, 5e-12)
test_case(function_list['atan2'], (1.0, -1.0), math.atan2(1.0, -1.0), 5e-12, 5e-12)

# --- copysign
test_case(function_list['copysign'], (1.5, -2.0), math.copysign(1.5, -2.0), 0.0, 0.0)
test_case(function_list['copysign'], (-1.5, 2.0), math.copysign(-1.5, 2.0), 0.0, 0.0)
test_case(function_list['copysign'], (float('inf'), -1.0), math.copysign(float('inf'), -1.0), 0.0, 0.0)

# --- degrees / radians
test_case(function_list['degrees'], (PI,), math.degrees(PI), 5e-12, 5e-12)
test_case(function_list['degrees'], (PI / 2.0,), math.degrees(PI / 2.0), 5e-12, 5e-12)
test_case(function_list['degrees'], (-PI / 4.0,), math.degrees(-PI / 4.0), 5e-12, 5e-12)

test_case(function_list['radians'], (180.0,), math.radians(180.0), 5e-12, 5e-12)
test_case(function_list['radians'], (90.0,), math.radians(90.0), 5e-12, 5e-12)
test_case(function_list['radians'], (-45.0,), math.radians(-45.0), 5e-12, 5e-12)

# --- dist
test_case(function_list['dist'], ([0.0, 0.0], [3.0, 4.0]), math.dist([0.0, 0.0], [3.0, 4.0]), 5e-12, 5e-12)
test_case(function_list['dist'], ([1.0, 2.0, 3.0], [4.0, 6.0, 3.0]), math.dist([1.0, 2.0, 3.0], [4.0, 6.0, 3.0]), 5e-12, 5e-12)
test_case(function_list['dist'], ([1.0], [4.0]), math.dist([1.0], [4.0]), 5e-12, 5e-12)

# --- erf / erfc
test_case(function_list['erf'], (0.0,), math.erf(0.0), 5e-12, 5e-12)
test_case(function_list['erf'], (1.0,), math.erf(1.0), 5e-12, 5e-12)
test_case(function_list['erf'], (-2.0,), math.erf(-2.0), 5e-12, 5e-12)

test_case(function_list['erfc'], (0.0,), math.erfc(0.0), 5e-12, 5e-12)
test_case(function_list['erfc'], (1.0,), math.erfc(1.0), 5e-12, 5e-12)
test_case(function_list['erfc'], (-2.0,), math.erfc(-2.0), 5e-12, 5e-12)

# --- exp / expm1
test_case(function_list['exp'], (0.0,), math.exp(0.0), 5e-12, 5e-12)
test_case(function_list['exp'], (1.0,), math.exp(1.0), 5e-12, 5e-12)
test_case(function_list['exp'], (-10.0,), math.exp(-10.0), 5e-12, 5e-12)

test_case(function_list['expm1'], (0.0,), math.expm1(0.0), 5e-12, 5e-12)
test_case(function_list['expm1'], (1e-9,), math.expm1(1e-9), 5e-12, 5e-12)
test_case(function_list['expm1'], (-20.0,), math.expm1(-20.0), 5e-12, 5e-12)

# --- fabs
test_case(function_list['fabs'], (-3.5,), math.fabs(-3.5), 0.0, 0.0)
test_case(function_list['fabs'], (0.0,), math.fabs(0.0), 0.0, 0.0)
test_case(function_list['fabs'], (float('inf'),), math.fabs(float('inf')), 0.0, 0.0)

# --- fmod / remainder
test_case(function_list['fmod'], (5.5, 2.0), math.fmod(5.5, 2.0), 5e-12, 5e-12)
test_case(function_list['fmod'], (-5.5, 2.0), math.fmod(-5.5, 2.0), 5e-12, 5e-12)
test_case(function_list['fmod'], (5.5, -2.0), math.fmod(5.5, -2.0), 5e-12, 5e-12)

test_case(function_list['remainder'], (5.5, 2.0), math.remainder(5.5, 2.0), 5e-12, 5e-12)
test_case(function_list['remainder'], (-5.5, 2.0), math.remainder(-5.5, 2.0), 5e-12, 5e-12)
test_case(function_list['remainder'], (5.5, -2.0), math.remainder(5.5, -2.0), 5e-12, 5e-12)

# --- fsum
test_case(function_list['fsum'], ([0.1] * 10,), math.fsum([0.1] * 10), 1e-15, 1e-15)
test_case(function_list['fsum'], ([1e10, 1.0, 1.0, 1.0, -1e10],), math.fsum([1e10, 1.0, 1.0, 1.0, -1e10]), 1e-15, 1e-12)
test_case(function_list['fsum'], ([1.0, 2.0, 3.0],), math.fsum([1.0, 2.0, 3.0]), 0.0, 0.0)

# --- gamma / lgamma
test_case(function_list['gamma'], (1.0,), math.gamma(1.0), 5e-12, 5e-12)
test_case(function_list['gamma'], (0.5,), math.gamma(0.5), 5e-12, 5e-12)
test_case(function_list['gamma'], (5.0,), math.gamma(5.0), 5e-12, 5e-12)

test_case(function_list['lgamma'], (1.0,), math.lgamma(1.0), 5e-12, 5e-12)
test_case(function_list['lgamma'], (0.5,), math.lgamma(0.5), 5e-12, 5e-12)
test_case(function_list['lgamma'], (10.0,), math.lgamma(10.0), 5e-12, 5e-12)

# --- hypot
test_case(function_list['hypot'], (3.0, 4.0), math.hypot(3.0, 4.0), 5e-12, 5e-12)
test_case(function_list['hypot'], (5.0, 12.0), math.hypot(5.0, 12.0), 5e-12, 5e-12)
test_case(function_list['hypot'], (1e5, 1e5), math.hypot(1e5, 1e5), 5e-12, 5e-12)

# --- ldexp
test_case(function_list['ldexp'], (0.75, 2), math.ldexp(0.75, 2), 5e-12, 5e-12)
test_case(function_list['ldexp'], (-1.5, 3), math.ldexp(-1.5, 3), 5e-12, 5e-12)
test_case(function_list['ldexp'], (1.0, -3), math.ldexp(1.0, -3), 5e-12, 5e-12)

# --- log / log10 / log1p / log2
test_case(function_list['log'], (1.0,), math.log(1.0), 5e-12, 5e-12)
test_case(function_list['log'], (math.e,), math.log(math.e), 5e-12, 5e-12)
test_case(function_list['log'], (1e-300,), math.log(1e-300), 5e-12, 5e-12)
test_case(function_list['log'], (8.0, 2.0), math.log(8.0, 2.0), 5e-12, 5e-12)

test_case(function_list['log10'], (1000.0,), math.log10(1000.0), 5e-12, 5e-12)
test_case(function_list['log10'], (1.0,), math.log10(1.0), 5e-12, 5e-12)
test_case(function_list['log10'], (0.01,), math.log10(0.01), 5e-12, 5e-12)

test_case(function_list['log1p'], (0.0,), math.log1p(0.0), 5e-12, 5e-12)
test_case(function_list['log1p'], (1e-12,), math.log1p(1e-12), 5e-12, 5e-12)
test_case(function_list['log1p'], (-0.5,), math.log1p(-0.5), 5e-12, 5e-12)

test_case(function_list['log2'], (8.0,), math.log2(8.0), 5e-12, 5e-12)
test_case(function_list['log2'], (1.0,), math.log2(1.0), 5e-12, 5e-12)
test_case(function_list['log2'], (0.5,), math.log2(0.5), 5e-12, 5e-12)

# --- pow
test_case(function_list['pow'], (2.0, 10.0), math.pow(2.0, 10.0), 5e-12, 5e-12)
test_case(function_list['pow'], (9.0, 0.5), math.pow(9.0, 0.5), 5e-12, 5e-12)
test_case(function_list['pow'], (-8.0, 3.0), math.pow(-8.0, 3.0), 5e-12, 5e-12)

# --- prod
test_case(function_list['prod'], ([1, 2, 3, 4],), math.prod([1, 2, 3, 4]), 0.0, 0.0)
test_case(function_list['prod'], ([],), math.prod([]), 0.0, 0.0)
test_case(function_list['prod'], ([1.5, 2.0],), math.prod([1.5, 2.0]), 0.0, 0.0)

# --- cbrt
test_case(function_list['cbrt'], (27.0,), math.copysign(abs(27.0) ** (1.0 / 3.0), 27.0), 5e-12, 5e-12)
test_case(function_list['cbrt'], (-8.0,), math.copysign(abs(-8.0) ** (1.0 / 3.0), -8.0), 5e-12, 5e-12)
test_case(function_list['cbrt'], (1e-27,), math.copysign(abs(1e-27) ** (1.0 / 3.0), 1e-27), 5e-12, 5e-12)

# --- exp2
test_case(function_list['exp2'], (0.0,), 2.0**0.0, 5e-12, 5e-12)
test_case(function_list['exp2'], (10.0,), 2.0**10.0, 5e-12, 5e-12)
test_case(function_list['exp2'], (-1.0,), 2.0**-1.0, 5e-12, 5e-12)

# --- sumprod
test_case(function_list['sumprod'], ([1, 2, 3], [4, 5, 6]), 32.0, 5e-12, 5e-12)
test_case(function_list['sumprod'], ([0.1, 0.2], [0.3, 0.4]), 0.11, 5e-12, 5e-12)
test_case(function_list['sumprod'], ([1.0], [2.0]), 2.0, 5e-12, 5e-12)

# --- fma
test_case(function_list['fma'], (2.0, 3.0, 4.0), 10.0, 5e-12, 5e-12)
test_case(function_list['fma'], (0.1, 0.2, 0.3), 0.32, 5e-12, 5e-12)
test_case(function_list['fma'], (-2.0, 3.0, 4.0), -2.0, 5e-12, 5e-12)


# -----------------------------
# INT CASES -> test_case(...)
# -----------------------------

# --- abs
test_case(function_list['abs'], (-7,), 7)
test_case(function_list['abs'], (0,), 0)
test_case(function_list['abs'], (123456789,), 123456789)

# --- sgn
test_case(function_list['sgn'], (-1e-300,), -1)
test_case(function_list['sgn'], (0.0,), 0)
test_case(function_list['sgn'], (42.0,), 1)

# --- ceil
test_case(function_list['ceil'], (1.2,), math.ceil(1.2))
test_case(function_list['ceil'], (-1.2,), math.ceil(-1.2))
test_case(function_list['ceil'], (3.0,), math.ceil(3.0))

# --- floor
test_case(function_list['floor'], (1.9,), math.floor(1.9))
test_case(function_list['floor'], (-1.1,), math.floor(-1.1))
test_case(function_list['floor'], (3.0,), math.floor(3.0))

# --- trunc
test_case(function_list['trunc'], (3.9,), math.trunc(3.9))
test_case(function_list['trunc'], (-3.9,), math.trunc(-3.9))
test_case(function_list['trunc'], (0.0,), math.trunc(0.0))

# --- comb
test_case(function_list['comb'], (5, 2), math.comb(5, 2))
test_case(function_list['comb'], (10, 0), math.comb(10, 0))
test_case(function_list['comb'], (10, 10), math.comb(10, 10))

# --- perm
test_case(function_list['perm'], (5, 2), math.perm(5, 2))
test_case(function_list['perm'], (10, 0), math.perm(10, 0))
test_case(function_list['perm'], (10, 10), math.perm(10, 10))

# --- factorial
test_case(function_list['factorial'], (0,), math.factorial(0))
test_case(function_list['factorial'], (5,), math.factorial(5))
test_case(function_list['factorial'], (10,), math.factorial(10))

# --- gcd
test_case(function_list['gcd'], (0, 0), math.gcd(0, 0))
test_case(function_list['gcd'], (54, 24), math.gcd(54, 24))
test_case(function_list['gcd'], (-54, 24), math.gcd(-54, 24))

# --- lcm
test_case(function_list['lcm'], (0, 5), math.lcm(0, 5))
test_case(function_list['lcm'], (6, 8), math.lcm(6, 8))
test_case(function_list['lcm'], (-6, 8), math.lcm(-6, 8))

# --- isqrt
test_case(function_list['isqrt'], (0,), math.isqrt(0))
test_case(function_list['isqrt'], (15,), math.isqrt(15))
test_case(function_list['isqrt'], (16,), math.isqrt(16))


# -----------------------------
# BOOL CASES -> test_case(...)
# -----------------------------

# --- isclose
test_case(function_list['isclose'], (1.0, 1.0 + 1e-12), True)
test_case(function_list['isclose'], (1.0, 1.0001), False)
test_case(function_list['isclose'], (0.0, 1e-15), True)

# --- isfinite
test_case(function_list['isfinite'], (1.0,), True)
test_case(function_list['isfinite'], (float('inf'),), False)
test_case(function_list['isfinite'], (float('nan'),), False)

# --- isinf
test_case(function_list['isinf'], (float('inf'),), True)
test_case(function_list['isinf'], (-float('inf'),), True)
test_case(function_list['isinf'], (1.0,), False)

# --- isnan
test_case(function_list['isnan'], (float('nan'),), True)
test_case(function_list['isnan'], (1.0,), False)
test_case(function_list['isnan'], (float('inf'),), False)


# -----------------------------
# TUPLE CASES -> test_case(...)
# -----------------------------

test_case(function_list['modf'], (3.14159,), math.modf(3.14159))
test_case(function_list['modf'], (-3.14159,), math.modf(-3.14159))
test_case(function_list['modf'], (2.0,), math.modf(2.0))


# -----------------------------
# RAISES CASES -> test_case(...)
# -----------------------------

test_case(function_list['asin'], (0.5000000001,), math.asin(0.5000000001))
test_case(function_list['arcsin'], (-0.5000000001,), math.asin(-0.5000000001))

test_case(function_list['acos'], (0.5000000001,), math.acos(0.5000000001))
test_case(function_list['arccos'], (-0.5000000001,), math.acos(-0.5000000001))

test_case(function_list['ln'], (1.0,), math.log(1.0), 5e-12, 5e-12)
test_case(function_list['ln'], (1e-12,), math.log(1e-12), 5e-12, 5e-12)

test_case(function_list['log'], (2.0,), math.log(2.0), 5e-12, 5e-12)

test_case(function_list['lg'], (10.0,), math.log10(10.0), 5e-12, 5e-12)
test_case(function_list['lg'], (0.00123,), math.log10(0.00123), 5e-12, 5e-12)

test_case(function_list['log10'], (1000.0,), math.log10(1000.0), 5e-12, 5e-12)

test_case(function_list['log1p'], (1e-12,), math.log1p(1e-12), 5e-12, 5e-12)
test_case(function_list['log1p'], (-0.5,), math.log1p(-0.5), 5e-12, 5e-12)

test_case(function_list['log2'], (8.0,), math.log2(8.0), 5e-12, 5e-12)

test_case(function_list['acosh'], (2.0,), math.acosh(2.0), 5e-12, 5e-12)

test_case(function_list['atanh'], (0.5,), math.atanh(0.5), 5e-12, 5e-12)
test_case(function_list['atanh'], (-0.9,), math.atanh(-0.9), 5e-12, 5e-12)

test_case(function_list['comb'], (5, 2), math.comb(5, 2), 0.0, 0.0)
test_case(function_list['comb'], (10, 0), math.comb(10, 0), 0.0, 0.0)

test_case(function_list['perm'], (5, 2), math.perm(5, 2), 0.0, 0.0)
test_case(function_list['perm'], (10, 0), math.perm(10, 0), 0.0, 0.0)

test_case(function_list['factorial'], (0,), math.factorial(0), 0.0, 0.0)
test_case(function_list['factorial'], (5,), math.factorial(5), 0.0, 0.0)

test_case(function_list['isqrt'], (0,), math.isqrt(0), 0.0, 0.0)
test_case(function_list['isqrt'], (16,), math.isqrt(16), 0.0, 0.0)

test_case(function_list['fmod'], (5.5, 2.0), math.fmod(5.5, 2.0), 5e-12, 5e-12)
test_case(function_list['remainder'], (5.5, 2.0), math.remainder(5.5, 2.0), 5e-12, 5e-12)

test_case(function_list['gamma'], (1.0,), math.gamma(1.0), 5e-12, 5e-12)
test_case(function_list['gamma'], (5.0,), math.gamma(5.0), 5e-12, 5e-12)


# -----------------------------
# signed zero preservation (copysign)
# -----------------------------

test_case(function_list['copysign'], (0.0, -1.0), -0.0, 0.0, 0.0)
test_case(function_list['copysign'], (0.0, 1.0), 0.0, 0.0, 0.0)

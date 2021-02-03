import math
def bisect(f, a, b, expected_error, maxiter):
    ll = a
    ul = b
    i = 0
    error = 0
    x = 0
    while True:
        xold = x
        x = (ll+ul)/2
        i += 1
        if x != 0:
            error = abs(x-xold)*100/x
        test = f(ll)*f(x)
        # print(i, ll, ul, x, error, f(x))
        if test < 0:
            ul = x
        elif test > 0:
            ll = x
        else:
            error = 0
        if error < expected_error or i >= maxiter:
            return x, error, i, f(x)

def f(c, m=65, t=5, v=45):
    return (9.81*m/c)*(1-math.exp(-c*t/m))-v

def g(x):
    return (x**5-1)/math.cos(x) + x**2 +2

def H(x):
    return 5*math.sin(x-2)*math.exp(2*x)

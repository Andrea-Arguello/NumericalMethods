from sympy import Symbol, diff, lambdify
from sympy import cos, sin, pi
from sympy.functions import exp

def functionMaker(f, symbol):
    f_prima = f.diff(symbol)
    return lambdify(symbol, f), lambdify(symbol, f_prima)

def NR(funcion, symbol, x0, expected_error, maxiter):
    xr = x0
    i, error = 0, 0
    f, f_prima = functionMaker(funcion, symbol)
    while True:
        xold = xr
        xr = xold - f(xold)/f_prima(xold)
        if xr != 0:
            error = abs((xr-xold)/xr)*100
        print(i, xold, f(xold), f_prima(xold), error, xr)
        i+=1
        if error < expected_error or i >= maxiter:
            return i, xr, f(xr), f_prima(xr), error

def fixedpoint(g, x0, expected_error, maxiter):
    xr = x0
    i, error = 0, 0
    while True:
        xold = xr
        xr=g(xold)
        if xr != 0:
            error = abs((xr-xold)/xr)*100
        print(i, xold, g(xold), error, xr)
        i+=1
        if error < expected_error or i >= maxiter:
            return i, xr, g(xr), error

x = Symbol('x')
## NR examples
#f = exp(x)-3*x**2
g = exp(-x)-cos(x)-3*x**4

#print(NR(f, x, 0, 0.001, 10))
#print(NR(f, x, 1, 0.001, 10))

print(NR(g,x,-1,0.1,10))

## FP
## f(x) = x**3 - 2*x - 3
# g, g_prima = functionMaker((x**3 - 3)/2, x) #no funcionó, diverge
g, g_prima = functionMaker((2*x + 3)**(1/3), x)

_, xr, _, _ = fixedpoint(g,1,1,10)

print(fixedpoint(g,1,1,10), g_prima(xr))

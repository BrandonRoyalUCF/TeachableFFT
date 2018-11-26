import math
#__add__, mult, sub, mod, truediv, lt (less than), getitem, contains,

class Complex:
    a = 0.0
    bi = 0.0
    
    def __init__(this, a, b=0.0):
        this.a = a
        this.bi = b
        return
    
    def __mul__(this, that):
        newA = this.a * that.a - this.bi * that.bi
        newB = this.a * that.bi + this.bi * that.a
        return Complex(newA, newB)

    def __add__(this, that):
        newA = this.a + that.a
        newB = this.bi + that.bi;
        return Complex(newA, newB)

    def __sub__(this, that):
        newA = this.a - that.a
        newB = this.bi - that.bi;
        return Complex(newA, newB)

    def __repr__(this):
        return "{:.4f}".format(this.a) + "+" + "{:.4f}".format(this.bi) + "i" 

def evenAndOddIndices(A):
    E = []
    O = []
    for i in range(0, len(A)):
        if i % 2 == 0:
            E.append(A[i])
        else:
            O.append(A[i])
    return [E,O]

def rootsOfUnity(n):
    w = []
    angle = 2 * math.pi / n
    for i in range(0, n):
        w.append(Complex(math.cos(angle * i), math.sin(angle * i)))
    return w

############################

def fft(A):
    n = len(A)
    
    # base
    if n == 1:
        return A[:]

    # recursion
    [E, O] = evenAndOddIndices(A)
    E = fft(E)
    O = fft(O)

    # roots
    w = rootsOfUnity(n)

    result = []
    for k in range(0, n):
        kPrev = k % (n//2)
        result.append(E[kPrev] + O[kPrev] * w[k])

    return result

############################

def toComplex(A):
    C = []
    for i in range(0, len(A)):
        C.append(Complex(A[i]))
    return C

def mult(A, B):
    C = []
    for i in range(0, len(A)):
        C.append(A[i]* B[i])
    return C

# arr1 = [1,2,3,2,0,0,0,0]
# arr1 = [0,0,0,0,1,2,3,2]
# arr2 = [0,0,0,0,3,3,0,7]
# f1 = fft(toComplex(arr1))
# f2 = fft(toComplex(arr2))
# f12 = mult(f1, f2)
# back = fft(f12)
# for i in range(0, len(back)):
#   back[i] = back[i] * Complex(0.125, 0)
# back



    

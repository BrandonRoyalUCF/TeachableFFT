##############################################################################################
# COT5405 Final Project Code
# Team Members: Steven Zielinski, Derek Goodwin, Brandon Royal, Eric Ly,
#               Tyler VanHaren, Amon Al-Khatib
# Project: Teachable FFT
##############################################################################################

import math
#__add__, mult, sub, mod, truediv, lt (less than), getitem, contains,

class Complex:
    
    #Given that a complex number is expressed as 'a + bi' each complex has 
    #Class attributes: a = represents the 'a' from the equation above
    #                 bi = represents the 'bi' from the equation above
    a = 0.0
    bi = 0.0
    
    #initializes a complex number
    #a is a required parameter and b is optional
    def __init__(this, a, b=0.0):
        this.a = a
        this.bi = b
        return
    
    #Definitition: multiplies two complex numbers
    #Parameters: this = first complex number
    #            that = second complex number
    #Returns: a new complex number which represents the result of the multiplication
    def __mul__(this, that):
        newA = this.a * that.a - this.bi * that.bi
        newB = this.a * that.bi + this.bi * that.a
        return Complex(newA, newB)

    #Definition: adds two complex numbers
    #Parameters: this = first complex number
    #            that = second complex number
    #Returns: a new complex number which represents the result of the addition
    def __add__(this, that):
        newA = this.a + that.a
        newB = this.bi + that.bi;
        return Complex(newA, newB)

    #Definition: subtract one complex number from the other
    #Parameters: this = first complex number
    #            that = second complex number
    #Returns: a new complex number which represents the result of the subtraction
    def __sub__(this, that):
        newA = this.a - that.a
        newB = this.bi - that.bi;
        return Complex(newA, newB)

    #Definition: returns the a string version of a complex number for visualization
    #Parameters: this = the complex number being visualized
    #Returns: a string representation of the complex number
    def __repr__(this):
        return "{:.4f}".format(this.a) + "+" + "{:.4f}".format(this.bi) + "i" 

#Definition: Given an input sequence, splits the input into two sequences such that all even
#            indexes are inserted into a new sequence in order and all odd indexes are inserted
#            into a new sequence in order.
#Parameters: A = an array of complex numbers
#Returns: E = the numbers from the even indexes of the input array 
#         O = the numbers from the odd indexes of the input array
def evenAndOddIndices(A):
    E = []
    O = []
    for i in range(0, len(A)):
        if i % 2 == 0:
            E.append(A[i])
        else:
            O.append(A[i])
    return [E,O]

#Definition: Generates n numbers such that w[1] raised to the k power is w[k]
#            w[n] is the same as w[0]
#Parameters: n = the amount of numbers generated
#Returns: w = an array of the generated numbers that follows the rule stated above
def rootsOfUnity(n):
    w = []
    angle = 2 * math.pi / n
    for i in range(0, n):
        w.append(Complex(math.cos(angle * i), math.sin(angle * i)))
    return w

############################

#Definition: Main fast Fourier transform function. Uses the helper functions to computer the
#            discrete Fourier transform of the input sequence.
#Parameters: A = an array of complex numbers
#Returns: result = the result of the FFT algorithm performed on the input
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

#Definition: Converts each integer in an array into a complex number representation
#Parameters: A = an array of intergers
#Returns: C = an array of complex numbers 
def toComplex(A):
    C = []
    for i in range(0, len(A)):
        C.append(Complex(A[i]))
    return C

#Definition: Multiplies each index of two arrays together
#Parameters: A = the first array
#            B = the second array
#Returns: C = a new array in which each index i of C is the product of A[i] and B[i]
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



    

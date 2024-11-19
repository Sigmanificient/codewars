"""kata url: https://www.codewars.com/kata/5c94b5bac29a2e37dfde5780."""

import string as s
B=s.digits+s.ascii_letters
def convert(n,f,t,k=0,o=""):
    for c in n:k=k*f+B.index(c)
    while k:o+=B[k%t];k//=t
    return o[::-1] or B[0]
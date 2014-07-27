"""
* A Pythagorean triplet is a set of three natural numbers, 
* a < b < c, for which, a2 + b2 = c2
* 
* For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
* 
* There exists exactly one Pythagorean triplet for which 
* a + b + c = 1000.
* Find the product abc.

"""

"""
Since a<b<c and a+b+c = 1000 and a,b,c are elements of N, it must be that
    c >= 335
    therefore
    a >= 335/b
    b >= 335/a
"""

"""
It then follows that:
    a+b = 1000 - c
    a+b <= 665
    a, b <= 665
"""

c_range = range( 335, 1000 )
answer = []

for c in c_range:
    b_range = range( 1, min((c+1), 665) )
    for b in b_range:
        a = 1000 - b - c
        if a <= 0 or a >= b:
            continue;
        asq = a*a
        bsq = b*b
        csq = c*c
        absq = asq+bsq
        if absq == csq:
            answer.append(a)
            answer.append(b)
            answer.append(c)
            break;

print answer
product = reduce( lambda x, y: x*y, answer)
print product










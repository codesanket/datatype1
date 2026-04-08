#1.Write a Python function to find the maximum of three numbers.
a=int(input('enter any number:'))
b=int(input('enter any number:'))
c=int(input('enter any number:'))

def max_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else :
        return c

result=max_number(a,b,c)
print('greater number is:',result)

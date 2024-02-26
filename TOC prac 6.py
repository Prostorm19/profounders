# Design a program for accepting decimal number divisible by 2
def stateq0(n):
    if n=='':
        print("string accepted")
    else:
        if n[0]=='0':
            stateq0(n[1:])
        elif n[0]=='1':
            stateq1(n[1:])

def stateq1(n):
    if n=='':
        print("string not accepted")
    else:
        if n[0]=='0':
            stateq0(n[1:])
        elif n[0]=='1':
            stateq1(n[1:])

n=input("Enter a binary number: ")
stateq0(n)
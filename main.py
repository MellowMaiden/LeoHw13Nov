print("Hello Stephen, This is Leo's homework.")
def number(a,b,c):
    delta=(b**2-4*a*c)**(1/2)
    return int(delta.real)
a=int(input("tell me a:"))
b=int(input("tell me b:"))
c=int(input("tell me c:"))
def root(a,b,c):
    delta = (b ** 2 - 4 * a * c) ** (1 / 2)
    if delta.real>= 0:
        anwser1 = (-b + delta) / (2 * a)
        anwser2 = (-b - delta) / (2 * a)
        if int(anwser1.real)==int(anwser2.real):
                return int(anwser1.real)
        else:
                return (int(anwser1.real), int(anwser2.real))
    else:
        return None
if number(a,b,c)>0:
    print("This equation have 2 real root.")
    line = f"The equation of {a}x^2+{b}x+{c}=0 roots are: {root(a, b, c)}"
    line=line.replace("1x","x")
    line=line.replace("+-","-")
    line=line.replace("++","+")
    print(line)
elif number(a,b,c)==0:
    print("This equation have 1 real root.")
    line = f"The equation of {a}x^2+{b}x+{c}=0 root is: {root(a, b, c)}"
    line=line.replace("1x","x")
    line=line.replace("+-","-")
    line=line.replace("++","+")
    print(line)

else:
    print("This equation have no real root")




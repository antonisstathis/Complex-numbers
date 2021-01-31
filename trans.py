import math

def transc(complex1):
    m=complex1["measure"]
    c=complex1["corner"]
    corner=math.radians(c)
    if c==0:
        real=m
        im=0
    if c==180:
        real=(-1)*m
        im=0
    if c==90:
        real=0
        im=m*math.sin(corner)
    if c==270:
        real=0
        im=m*math.sin(corner)
    if c!=0 and c!=180 and c!=90 and c!=270:
        real=m*math.cos(corner)
        im=m*math.sin(corner)
    print("Real="+str(real)+" Imaginary="+str(im))
    print("Measure="+str(m)+" Corner="+str(c))
    complex1["real"]=real
    complex1["im"]=im

def transp(complex1):
    x=complex1["real"]
    y=complex1["im"]
    d=math.sqrt(x*x+y*y)
    if  x>0 and y>0:
        c=math.degrees(math.atan(y/x))
    if x<0 and y>0:
        c=180+math.degrees(math.atan(y/x))
    if x<0 and y<0:
        c=180+math.degrees(math.atan(y/x))
    if x>0 and y<0:
        c=360+math.degrees(math.atan(y/x))
    if x==0 and y>0:
        c=90
    if x==0 and y<0:
        c=270
    if x>0 and y==0:
        c=0
    if x<0 and y==0:
        c=180
    if x==0 and y==0:
        d=0
        c=0
    print("Real="+str(x)+" Imaginary="+str(y))
    print("Measure="+str(d)+" Corner="+str(c))
    complex1["measure"]=d
    complex1["corner"]=c

def enterp(complex1):
    m=float(input("Enter measure: "))
    c=float(input("Enter corner: "))
    complex1["measure"]=m
    complex1["corner"]=c
    transc(complex1)

def enterc(complex1):
    x=float(input("Enter real part: "))
    y=float(input("Enter imaginary part: "))
    complex1["real"]=x
    complex1["im"]=y
    transp(complex1)

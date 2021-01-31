def add(complex1,complex2,complex3):
    real1=complex1["real"]
    im1=complex1["im"]
    real2=complex2["real"]
    im2=complex2["im"]

    real3=real1+real2
    im3=im1+im2
    complex3["real"]=real3
    complex3["im"]=im3

def mul(complex1,complex2,complex3):

    m1=complex1["measure"]
    c1=complex1["corner"]
    m2=complex2["measure"]
    c2=complex2["corner"]

    m3=m1*m2
    c3=c1+c2
    if c3==360:
        c3=0
    if c3>360:
        c3=360-c3
    complex3["measure"]=m3
    complex3["corner"]=c3

def div(complex1,complex2,complex3):
    m1 = complex1["measure"]
    c1 = complex1["corner"]
    m2 = complex2["measure"]
    c2 = complex2["corner"]
 
    if m2==0:
        print("Division impossible: second complex number is zero.")
    if m2!=0:
        m3 = m1 / m2
        c3 = c1 - c2
        if c3 == 360:
            c3 = 0
        if c3 < 0:
            c3 = 360 + c3
        complex3["measure"] = m3
        complex3["corner"] = c3

def zparallel(complex1,complex2,complex3):

    real1 = complex1["real"]
    im1 = complex1["im"]
    real2 = complex2["real"]
    im2 = complex2["im"]
    real = real1 * real2 + (-1) * im1 * im2
    im = (real1 * im2 + im1 * real2)
    print("real part=" + str(real) + " imaginary part=" + str(im))

    if (input("Enter 'c' to continue:")) == 'c' and (real1!=0 or im1!=0) and (real2!=0 or im2!=0):
        real3 = real1 + real2
        im3 = im1 + im2
        print("real part=" + str(real3) + " imaginary part=" + str(im3))

        real4 = real * real3 + (-1) * im * ((-1) * im3)
        im4 = (real * (-1) * im3 + im * real3)
        print("real part=" + str(real4) + " imaginary part=" + str(im4))

        result = real3 * real3 + im3 * im3
        print("result=" + str(result))

        real5 = real4 / result
        im5 = im4 / result
        print("real part=" + str(real5) + " imaginary part=" + str(im5))
        complex3["real"] = real5
        complex3["im"] = im5
        print("Final result:")
    else:
        print("zp function impossible: you entered zero complex number.")

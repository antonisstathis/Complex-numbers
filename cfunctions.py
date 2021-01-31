def add(complex1, complex2, complex3):
    real1 = complex1["real"]
    im1 = complex1["im"]
    real2 = complex2["real"]
    im2 = complex2["im"]

    real3 = real1 + real2
    im3 = im1 + im2
    complex3["real"] = real3
    complex3["im"] = im3


def mul(complex1, complex2, complex3):
    m1 = complex1["measure"]
    c1 = complex1["corner"]
    m2 = complex2["measure"]
    c2 = complex2["corner"]

    m3 = m1 * m2
    c3 = c1 + c2
    if c3 == 360:
        c3 = 0
    if c3 > 360:
        c3 = 360 - c3
    complex3["measure"] = m3
    complex3["corner"] = c3


def div(complex1, complex2, complex3):
    m1 = complex1["measure"]
    c1 = complex1["corner"]
    m2 = complex2["measure"]
    c2 = complex2["corner"]

    if m2 == 0:
        print("Division impossible: second complex number is zero.")
    if m1 == 0:
        complex3["measure"]=0
        complex3["corner"]=0
    if m2 != 0 and m1 != 0:
        m3 = m1 / m2
        c3 = c1 - c2
        if c3 == 360:
            c3 = 0
        if c3 < 0:
            c3 = 360 + c3
        complex3["measure"] = m3
        complex3["corner"] = c3


def zparallel(complex1, complex2, complex3):
    real1 = complex1["real"]
    im1 = complex1["im"]
    real2 = complex2["real"]
    im2 = complex2["im"]

    if (real1!=0 or im1!=0) and (real2!=0 or im2!=0):
        real = real1 * real2 + (-1) * im1 * im2
        im = (real1 * im2 + im1 * real2)

        real3 = real1 + real2
        im3 = im1 + im2

        real4 = real * real3 + (-1) * im * ((-1) * im3)
        im4 = (real * (-1) * im3 + im * real3)

        result = real3 * real3 + im3 * im3

        real5 = real4 / result
        im5 = im4 / result
        complex3["real"] = real5
        complex3["im"] = im5
        print("Final result:")
    else:
        print("zp function impossible: you entered zero complex number.")

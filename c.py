from trans import enterp,enterc,transp,transc
from cproduct import add,mul,div,zparallel

complex1={
  "real": 0.0,
  "im": 0.0,
  "measure": 0.0,
  "corner": 0.0
  }

complex2={
  "real": 0.0,
  "im": 0.0,
  "measure": 0.0,
  "corner": 0.0
}

complex3={
  "real": 0.0,
  "im": 0.0,
  "measure": 0.0,
  "corner": 0.0
}

com=[complex1,complex2]

x="go"
while x=="go":
    for i in range(2):
        choice=input("Enter form:")    
        if choice=='p':
            enterp(com[i])
        if choice=='c':
            enterc(com[i])

    print("Enter: 'add' or 'mul' or 'div' or 'zp'")
    choice=input("Enter function:")
    if choice=="add":
        add(complex1,complex2,complex3)
        transp(complex3)
    if choice=="mul":
        mul(complex1,complex2,complex3)
        transc(complex3)
    if choice=="div":
        div(complex1,complex2,complex3)
        transc(complex3)
    if choice=="zp":
        zparallel(complex1,complex2,complex3)
        transp(complex3)

    x=input("Enter 'go' or 'exit':")
    print("\n\n")

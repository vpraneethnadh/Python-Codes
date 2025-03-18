def compoundInterest(p,t,r):
    r1 = r/100
    amount = p*(1+r1)**t
    ci = amount - p
    print(ci)

compoundInterest(10000,10.25,5)
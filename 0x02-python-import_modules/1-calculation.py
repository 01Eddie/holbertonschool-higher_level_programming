#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    ad = cal.add(a, b)
    su = cal.sub(a, b)
    mu = cal.mul(a, b)
    di = cal.div(a, b)
    print("{} + {} = {:d}".format(a,b, ad))
    print("{} - {} = {:d}".format(a,b, su))
    print("{} * {} = {:d}".format(a,b, mu))
    print("{} / {} = {:d}".format(a,b, di))

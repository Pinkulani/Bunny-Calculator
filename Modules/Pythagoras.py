def Pythagoras():
    print("Put 0 for value you want to calculate (2**2 + 0 = 5**2)")
    A = float(input("Value of A: "))
    B = float(input("Value of B: "))
    C = float(input("Value of C: "))
    match A:
        case 0:
            # A is unknown
            print((C**2) - (B**2))
        
        case _:
            match B:
                case 0:
                    # B is unknown
                    print((C**2) - (A**2))

                case _:
                    # C is unknown
                    print((A**2) + (B**2))
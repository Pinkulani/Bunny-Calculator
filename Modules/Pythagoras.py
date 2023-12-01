# @Pinkulani 1.12.2023

def Pythagoras():
    print("Put 0 for value you want to calculate (2**2 + 0 = 5**2)")
    A = float(input("Value of A: "))
    B = float(input("Value of B: "))
    C = float(input("Value of C: "))
    # Result sacrifices Memory instead of CPU resources
    match A:
        case 0:
            # A is unknown
            Result = (C ** 2) - (B ** 2)
            if Result >= 0:
                print(Result ** 0.5)
            else:
                print("No solution for real numbers!")
        
        case _:
            match B:
                case 0:
                    # B is unknown
                    Result = (C ** 2) - (A ** 2)
                    if Result >= 0:
                        print(Result ** 0.5)
                    else:
                        print("No solution for real numbers!")

                case _:
                    # C is unknown
                    print(((A ** 2) + (B ** 2)) ** 0.5)

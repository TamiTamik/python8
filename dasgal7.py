def gurvan_tal(a: int,b: int,c: int) -> bool:
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

a,b,c = [int (x) for x in input().split()]
if gurvan_tal(a,b,c):
    print("gurvaljin yes")
else:
    print("gurvaljin no")

    
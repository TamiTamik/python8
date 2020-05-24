def gurvan_tal(a: int,b: int,c: int) -> bool:
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

is_triangle = gurvan_tal(13,15,12)
print(is_triangle)
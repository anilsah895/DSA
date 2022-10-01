
def gcd(x, y):
    while y!=0:
        x, y = y, x%y
        return y

 
if __name__ == '__main__':
    sm = int(input())
    big = int(input())
    val = gcd(sm, big)
    print(val)








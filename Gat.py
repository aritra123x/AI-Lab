def bin(n):
    if n == 0 or n == 1:
        return str(n)
    else:
        return bin(n // 2) + str(n % 2)

def dec(n):
    k = 0
    for i in range(len(n)): 
        k += int(n[i]) * (2 ** (len(n) - i - 1)) 
    return k

def OR(a, b):
    return '1' if a == '1' or b == '1' else '0'

if __name__ == "__main__":
    print('Enter a b:')
    lst = list(map(int, input().split()))
    a = lst[0]
    b = lst[1]
    bina = bin(a)
    binb = bin(b)
    
    # Make both binary strings of equal length
    max_len = max(len(bina), len(binb))
    bina = bina.zfill(max_len)
    binb = binb.zfill(max_len)
    
    print("Binary A:", bina)
    print("Binary B:", binb)
    
    # Perform OR operation bit by bit
    bin_or = ''.join(OR(bina[i], binb[i]) for i in range(max_len))
    
    print("Binary OR Result:", bin_or)
    
    # Convert OR result to decimal
    dec_or = dec(bin_or)
    print("Decimal OR Result:", dec_or)

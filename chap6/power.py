# Exercise 6.4

def is_power(a,b):
    if a==1:
        return True
    if a%b==0:
        return is_power(a/b,b)
    return False

print(is_power(18**2+1,18))
print(is_power(18**2,18))

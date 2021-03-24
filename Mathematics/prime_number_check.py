# 1 is not a prime number
# 2 is the only prime number among even numbers

def check_prime(num): # only one number check
   
    prime=[2]
    
    if num < 2:
        return False
    elif num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
            break
    else: # position is important!
        return True
    

print(check_prime(1)) # False
print(check_prime(2)) # True
print(check_prime(3)) # True
print(check_prime(9)) # False
print(check_prime(15)) # False
print(check_prime(67)) # True

# 1 is not a prime number
# 2 is the only prime number among even numbers

def count_prime(num):
    
    prime=[2]
    
    if num < 2:
        return 0

    for i in range(3,num+1,2): # exclude even numbers
        
        for j in range(3,i,2):# up to i-1
            if i % j == 0:
                break
        else: # position is important
            prime.append(i)
    print(prime)
    return len(prime)

print(count_prime(100)) # 25
print(count_prime(10)) # 4
print(count_prime(2)) # 1
print(count_prime(1)) # 0



def count_prime2(num):
    
    prime=[]

    if num < 2:
        return 0

    for i in range(1, num+1): # exclude even numbers
        
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else: # position is important
                prime.append(i)
    return prime

print(count_prime2(100))
print(count_prime2(10)) 
print(count_prime2(2)) 
print(count_prime2(1)) 



def check_prime_interval(num1, num2): # all the prime numbers within an interval
    
    prime=[]

    for i in range(num1, num2+1): # exclude even numbers
        
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else: # position is important
                prime.append(i)
    return prime

print(check_prime_interval(1,10))
print(check_prime_interval(900,1000))
             

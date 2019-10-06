# 412. Fizz Buzz

# Write a program 
# that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and 
# for the multiples of five output “Buzz”. 
# For numbers which are multiples of both three and five output “FizzBuzz”.

# My solution
# 1) What data type I want to return ? 
# - input : a number
# - output(returned vablue) : array with number and string
# - need a storage(=a new variable) to store a new output/retured value : yes
# - iteration need? : yes
# Process 0 : return / a new variable
# Process 1 : iteration - start / finish / i += 1
# Process 2 : set a range - while line 
# Process 3 : conditionals/methods - div by 3 or 5 "fizz" and "buzz" and "fizzbuzz"

# @param {Integer} n
# @return {String[]}
def fizz_buzz(n)
    new_arr = []

    i = 1
    while i <= n
        if i % 3 == 0 && i % 5 != 0
           new_arr << "Fizz"
        elsif i % 5 == 0 && i % 3 != 0
            new_arr << "Buzz"
        elsif i % 3 == 0 && i % 5 == 0
            new_arr << "FizzBuzz"
        else 
            new_arr << i.to_s # How to change data type "Number" to "String"
        end
        i += 1
    end 
    return new_arr
    
end

print fizz_buzz(15)

def fizzBuzz(n)
    arr = []

    (1..n).each do |num|
        if num % 3 == 0 && num % 5 != 0 
            arr << "Fizz" 
    
        elsif num % 3 != 0 && num % 5 == 0 
            arr << "Buzz"

        elsif num % 3 == 0 && num % 5 == 0 
            arr << "FizzBuzz"
        
        else 
            arr << num.to_s
        end
    end
    return arr  
end 

puts fizzBuzz(15)
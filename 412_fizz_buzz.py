class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        new_arr = []

        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 != 0:
                new_arr.append("Fizz")
            elif i % 5 == 0 and i % 3 != 0:
                new_arr.append("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                new_arr.append("FizzBuzz")
            else:
                new_arr.append(str(i)) # How to change data type "Number" to "String"
            i += 1
        return new_arr


        
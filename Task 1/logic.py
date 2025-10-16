class FizzBuzz:
    def get_value(self,number:int)->str:
        if number %3==0 and number %5==0:
            return "FizzBuzz"
        elif number %3==0:
            return "Fizz"
        elif number %5==0:
            return "Buzz"
        else:
            return str(number)
    
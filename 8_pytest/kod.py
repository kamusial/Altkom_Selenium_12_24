def fizzbuzz(number):
    if isinstance(number, (int, float)) and number > 0:
        number = int(number)
        if number % 15 == 0:
            return 'FizzBuzz'
        elif number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
        return number
    return None
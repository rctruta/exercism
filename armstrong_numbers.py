# Determines if a number is an Armstrong number.
def is_armstrong_number(number):
    """
    An Armstrong number is a number that is the sum of its own digits,
    each raised to the power of the number of digits.
    """
    if number != int(number):
        raise TypeError("Wrong input type")          
    length = len(str(number))
    return sum([int(digit)**length for digit in str(number)]) == number

        

          

    

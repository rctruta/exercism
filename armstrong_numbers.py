def is_armstrong_number(number):

    if number != int(number):

        raise TypeError("Wrong input type")
          
    length = len(str(number))

    return sum([int(digit)**length for digit in str(number)]) == number

        

          

    

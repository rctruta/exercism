class Luhn:
    def __init__(self, card_num):
        card_num = card_num.replace(" ", "")
        if len(card_num) >= 2 and card_num.isdigit(): 
            self.card_num = [int(digit) for digit in card_num] 
        else:
            self.card_num = []

    def valid(self):
        """
        Given a number determine whether or not it is valid per the Luhn formula.

        The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, 
        such as credit card numbers and Canadian Social Insurance Numbers.
        """
        if self.card_num == []:
            return False
        check_sum = 0
        index = 0
        for digit in self.card_num[::-1]:
            if index % 2 != 0:
                digit *= 2 
                if digit > 9:
                    digit -= 9
            check_sum += digit
            index += 1
        return check_sum % 10 == 0    


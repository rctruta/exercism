def validate_input(base, digits):
    for digit in digits:
        if digit >= base or digit < 0:
            raise ValueError("digit out of range")

def rebase(input_base, digits, output_base):
    """
    Convert a number, represented as a sequence of digits in one base, to any other base.
    Implement general base conversion. 
    Given a number in base a, represented as a sequence of digits, convert it to base b.
    """
    validate_input(input_base, digits)
    if input_base == output_base:
        return "".join(str(digit) for digit in digits)
    return from_base10(output_base, to_base10(input_base, digits))

def to_base10(base, digits):
    if (base != int(base)) or (base < 2):
        raise ValueError("Incorrect base")
    if base == 10:
        return int("".join(str(digit) for digit in digits))

    result = 0
    pos = len(digits)
    digits = digits[::-1]
    while pos > 0:
        result += digits[pos-1] * (base**(pos-1))
        pos -= 1
    return result

def from_base10(base, number):
    if (base != int(base)) or (base < 2):
        raise ValueError("Incorrect base")
    if number < base:
        return [number]
    result = []

    quot = number
    while quot >= base:
        digit = quot % base
        result.append(digit)
        quot = quot // base
    result.append(quot)
    return result[::-1]

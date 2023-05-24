'''

Given the two integer values of a fraction, numerator and denominator, implement a 
function that returns the fraction in string format. If the fractional part repeats, 
enclose the repeating part in parentheses.

------------------
PATTERN: HASH MAP
------------------

'''










def fraction_to_decimal(numerator, denominator):
    if numerator == 0 : return 0

    result = ""
    r_dict = {}

    if (numerator < 0 ) ^ (denominator < 0) :
        result += "-"

    numerator = abs(numerator)
    denominator = abs(denominator)

    # quotient = numerator//denominator
    # remainder = numerator % denominator
    # result += str(quotient)

    quotient = numerator / denominator
    remainder = (numerator % denominator) * 10
    result += str(int(quotient))

    if remainder != 0 : result += "."
    elif remainder == 0 : return result

    while remainder != 0 :
        if str(remainder) not in r_dict :
            r_dict[str(remainder)] = len(result)

            quotient = remainder / denominator
            result += str(int(quotient))
            remainder = (remainder % denominator) * 10
        else :
            # length = r_dict[str(remainder)]
            # start = len(result) - length
            start = r_dict[str(remainder)]
            result = result[:start] + "(" + result[start: len(result)] + ")"
            return result


    return result



'''

def fraction_to_decimal(numerator, denominator):
    result, hash_map = "", {}
    if numerator == 0:
        return '0'

    if (numerator < 0) ^ (denominator < 0):
        result += '-'

        numerator = abs(numerator)
        denominator = abs(denominator)

    quotient = numerator / denominator
    remainder = (numerator % denominator) * 10
    result += str(int(quotient))

    if remainder == 0:
        return result
    else:
        result += "."
        while remainder != 0:
            if remainder in hash_map.keys():
                beginning = hash_map.get(remainder)
                left = result[0: beginning]
                right = result[beginning: len(result)]
                result = left + "(" + right + ")"
                return result

            hash_map[remainder] = len(result)
            quotient = remainder / denominator
            result += str(int(quotient))
            remainder = (remainder % denominator) * 10
        return result

'''













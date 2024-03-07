def is_valid_pin_codes(pin_codes):
    if not pin_codes:
        return False
    digit_set = set('1234567890')
    for pin in pin_codes:
        if type(pin) != str:
            return False
        elif len(pin) != 4:
            return False
        elif set(pin) - digit_set:
            return False
    count_of_pin_codes = len(pin_codes)
    pin_codes_set = set(pin_codes)
    count_of_pin_codes_in_set = len(pin_codes_set)
    if count_of_pin_codes != count_of_pin_codes_in_set:
        return False
    return True

print(is_valid_pin_codes(['1101', '9034', '0011']))

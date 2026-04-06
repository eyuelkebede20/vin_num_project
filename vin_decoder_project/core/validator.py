def validate_check_digit(vin):
    if len(vin) != 17:
        return False

    transliteration = {
        'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
        'J':1,'K':2,'L':3,'M':4,'N':5,'P':7,'R':9,
        'S':2,'T':3,'U':4,'V':5,'W':6,'X':7,'Y':8,'Z':9
    }
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    
    total = 0
    for i in range(17):
        char = vin[i].upper()
        if char.isdigit():
            val = int(char)
        elif char in transliteration:
            val = transliteration[char]
        else:
            return False 
        
        total += val * weights[i]
        
    remainder = total % 11
    expected_check_digit = 'X' if remainder == 10 else str(remainder)
    
    return vin[8].upper() == expected_check_digit
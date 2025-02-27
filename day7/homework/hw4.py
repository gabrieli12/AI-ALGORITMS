def func(text):
    number_to_char = {
        1: 'a', 
        2: 'b', 
        3: 'c', 
        4: 'd', 
        5: 'e', 
        6: 'f', 
        7: 'g', 
        8: 'h', 
        9: 'i', 
        10: 'j',
        11: 'k', 
        12: 'l', 
        13: 'm', 
        14: 'n', 
        15: 'o', 
        16: 'p', 
        17: 'q', 
        18: 'r', 
        19: 's', 
        20: 't',
        21: 'u', 
        22: 'v', 
        23: 'w', 
        24: 'x', 
        25: 'y', 
        26: 'z',
        27: 'A', 
        28: 'B', 
        29: 'C', 
        30: 'D', 
        31: 'E', 
        32: 'F', 
        33: 'G', 
        34: 'H', 
        35: 'I', 
        36: 'J',
        37: 'K', 
        38: 'L', 
        39: 'M', 
        40: 'N', 
        41: 'O', 
        42: 'P', 
        43: 'Q', 
        44: 'R', 
        45: 'S', 
        46: 'T',
        47: 'U', 
        48: 'V', 
        49: 'W', 
        50: 'X', 
        51: 'Y', 
        52: 'Z',
        53: '?', 
        54: '.', 
        55: ',', 
        56: '!', 
        57: "'"
    }


    final_str = ""
    
    
    text = text.split()
    each_char = []
    
    decimal_numbers = []
    
    for element in text:
        each_char.append(element.split('.'))
         
    
    number = 0
    for element in each_char:
        temporary_word = []
        for char in element:
            for i in range(1, len(char) + 1):
                number += int(char[-i]) * (2**(i-1))
                
            temporary_word.append(number)
            number = 0
            
        decimal_numbers.append(temporary_word)
        temporary_word = []
    
    
    for element in decimal_numbers:
        temporary_char_word = ""
        for char in element:
            temporary_char_word += number_to_char[char]
        
        final_str += temporary_char_word + " "
        
    print(final_str[:-1])


text = """11101.1.1110 11001.1111.10101 10010.101.1.100 10100.1000.1001.10011.110101"""
func(text)
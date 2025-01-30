# დაწერეთ და გაუშვით პროგრამა, რომელსაც რიცხვები გადაყავს ერთი პოზიციური სისტემიდან მეორეში ჩაშენებული ფუნქციების გამოყენების გარეშე. პროგრამა მინიმუმ უნდა მუშაობდეს 2, 4, 10, 16 ფუძის მქონე სისტემებისთვის.



def converter(num, initial_system, final_system):        
    decimal = 0
    hex_decimal = {
        'A': 10, 
        'B': 11, 
        'C': 12,
        'D': 13, 
        'E': 14,
        'F': 15,
    }
    
    hex_decimal2 = {
        '10': 'A', 
        '11': 'B', 
        '12': 'C',
        '13': 'D', 
        '14': 'E',
        '15': 'F',
    }
    
    
    if initial_system != '16':
        for i in range(len(num)):
            decimal += int(num[i]) * int(initial_system)**(len(num)-(i+1))
    else:
        for i in range(len(num)):
            if num[i] not in '0123456789':
                decimal += hex_decimal.get(num[i]) * 16**(len(num)-(i+1))
            else:
                decimal += int(num[i]) * 16**(len(num)-(i+1))
          
    final_result = ''   
             
    if final_system != 16:
        while decimal > 0:
            print(f'{decimal // final_system} : remainder {decimal % final_system}')    
            final_result += str(decimal % final_system)
            decimal = decimal // final_system
    else:
        while decimal > 0:
            if str(decimal % final_system) not in '0123456789':
                final_result += hex_decimal2.get(str(decimal % final_system))
            else:
                final_result += str(decimal % final_system)
                
            
            decimal = decimal // final_system
                

    return final_result[::-1]
        
        
print(converter('D59', '16', 16))


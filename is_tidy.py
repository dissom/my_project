number='1234576'

def is_special_number(number: int) -> str:
    num_str=str(number)

    for i in range(1,len(num_str)):
        if num_str[i] < num_str[i-1]:
            return False
        
    return True    

print (is_special_number(number))
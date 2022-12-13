import re

def check_consequitivenumbers(numericpasswrd): 
    num = re.findall(r'\d+', numericpasswrd)
    
    counter = 0
    

    for numbers in num:
        length = len(numbers)
        if length >= 3:
            for i in range(length-1):
                first_digit = numbers[i]
                second_digit = numbers[i + 1]
                if int(second_digit) - int(first_digit) == 1:
                    counter += 1
    print (counter)
    if counter >= 2:
        print("consecutive!")
        
# Test the function with a few example passwords
password = "abc678"
check_consequitivenumbers(password)  # Should print "consecutive!"

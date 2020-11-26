#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

def find_prime():
    'Evaluate if the number is prime or not'
    print (find_prime.__doc__)
    try:
        n = int(input('Enter the number: ')) # Accepting the nuber from user
        if n > 1:
            for i in range (2,n): 
                if (n % i == 0): # Checking if number is positive
                    print(n,' is not a prime number')
                    return False
                else:
                    print(n,' is a prime number')
                    return True
        elif n == 1: # Checking if number is 1
            print('1 is a natural number')
            return False
        else:
            print('Number should be greater than 0')
            return False
    except ValueError:
        print('Input should be in number format')
        return False

def validate_happy_number():
    'Evaluate if the number is happy or not'
    print (validate_happy_number.__doc__)
    
    try:
        n = int(input('Enter the number: ')) # Accepting the nuber from user
        if n < 0: # Checking if number is positive
            print('Number should be positive and greater than 0')
        else:   
            value = n
            while n != 0: # Looping until the result is a single digit number
                num = n
                result=0
                while num!=0: # Looping single digit and squaring its sum
                    digit = num%10
                    result = result + (digit ** 2)
                    num = num//10 
                if (len(str(result))== 1 and result == 1):
                    print(value, ' is a happy number')
                    return True
                elif (len(str(result))>1 and result != 1):
                    n =  result
                elif (len(str(result))== 1 and result != 1):
                    print(value, ' is a sad number')
                    return False     
    except ValueError:
        print('Input should be in number format')
        return False

def validate_happy_prime_number():
    'Evaluate if the number is happy and prime or not'
    print (validate_happy_prime_number.__doc__)
    
    try:
        n = int(input('Enter the number: ')) # Accepting the nuber from user
        if n < 0: # Checking if number is positive
            print('Number should be positive and greater than 0')
        elif n == 1: # Checking if number is equal to 1
            print('1 is a natural number')
            return False
        else: 
            for i in range (2,n):
                if (n % i == 0): # Checking if number is divisible by any other number
                    print(n,' is not a prime number')
                    return False
                else: 
                    value = n
                    while n != 0: # Looping until the result is a single digit number
                        num = n
                        result=0
                        while num!=0:  # Looping single digit and squaring its sum
                            digit = num%10
                            result = result + (digit ** 2)
                            num = num//10 
                        if (len(str(result))== 1 and result == 1):
                            print(value, ' is a happy and a prime number')
                            return True
                        elif (len(str(result))>1):
                            n =  result
                        elif (len(str(result))== 1 and result != 1):
                            print(value, ' is a sad and a prime number')
                            return False     
    except ValueError:
        print('Input should be in number format')
        return False

def find_number_happy_and_sad(n):
    try:
        if n < 0: # Checking if number is positive
            print('Number should be positive and greater than 0')
        elif n == 1: # Checking if number is equal to 1
            print('1 is a natural number')
            return False
        else: 
            for i in range (2,n):
                if (n % i == 0): # Checking if number is divisible by any other number
                    return False
                else: 
                    while n != 0: # Looping until the result is a single digit number
                        num = n
                        result=0
                        while num!=0:  # Looping single digit and squaring its sum
                            digit = num%10
                            result = result + (digit ** 2)
                            num = num//10 
                        if (len(str(result))== 1 and result == 1):
                            return True
                        elif (len(str(result))>1):
                            n =  result
                        elif (len(str(result))== 1 and result != 1):
                            return False     
    except:
        print('Error')
        return False
 
def return_100_happy_prime_number():
    'Returns the list of first 100 happy prime numbers'
    print (return_100_happy_prime_number.__doc__)
    range_num = 0
    n = 3
    lst = []
    try:
        while range_num < 101: # Execute loop for 100 numbers
            for i in range (2,n):
                if (n % i == 0): # Checking if number is prime or not
                    break
            else:
                if find_number_happy_and_sad(n) is True: # Call find_number_happy_and_sad function to check if number is happy
                    lst.append(n)  # Appends number to the list
                    range_num = range_num + 1
            n = n + 1
        print(lst)
    except:
        print('Error')
        return False

def return_100_sad_prime_number():
    'Returns the list of first 100 sad prime numbers'
    print (return_100_sad_prime_number.__doc__)
    range_num = 0
    n = 3
    lst = []
    try:
        while range_num < 101: # Execute loop for 100 numbers
            for i in range (2,n):
                if (n % i == 0): # Checking if number is prime or not
                    break
            else:
                if find_number_happy_and_sad(n) is False: # Call find_number_happy_and_sad function to check if number is sad
                    lst.append(n) # Appends number to the list
                    range_num = range_num + 1
            n = n + 1
        print(lst)
    except:
        print('Error')
        return False

if __name__ == "__main__":
    print(find_prime())# Trigger find_prime function
    print(validate_happy_number())# Trigger validate_happy_number function
    print(validate_happy_prime_number())# Trigger validate_happy_prime_number function
    return_100_happy_prime_number()# Trigger return_100_happy_prime_number function
    return_100_sad_prime_number()# Trigger return_100_sad_prime_number function
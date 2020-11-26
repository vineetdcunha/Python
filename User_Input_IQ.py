#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

def evaluate_iq():
    'Evaluate the grade of the person based on their IQ'
    print (evaluate_iq.__doc__)
    x = input('Enter your first name: ') # Accepting first name value from user
    y = input('Enter your last name: ') # Accepting last name value from user
    z = input('Enter your IQ: ') # Accepting IQ value from user

    if len(x.strip()) != 0 and len(y.strip()) != 0 and len(z.strip()) != 0: # Check if input value is null
        try:
            if (int(z) <= 90): # Define condition for D category
                print (x,' ',y,', your grade is D')
            elif int(z) > 90 and int(z) <= 110: # Define condition for C category
                print (x,' ',y,', your grade is C')
            elif int(z) > 110 and int(z) <= 130: # Define condition for B category
                print (x,' ',y,', your grade is B')
            elif int(z) > 130: # Define condition for first category
                print (x,' ',y,', you are a Liar')
        except ValueError: # exception block
            print('IQ value should be in number format')
        except:
            print('Incorrect Input')
    else:
        print('Enter your name and IQ')

if __name__ == "__main__":
    evaluate_iq() # Trigger evaluate_iq function
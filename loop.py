# Write a program that repeatedly prompts a user for integer numbers until the user
# enters 'done'. Once 'done' is entered, print out the largest and smallest of the 
# numbers. If the user enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and 
# match the output below.

small=None
large=None
while True:
    inp = input('Enter a number: ')
    if inp == "done":
        break
    else:
        try:
            inp = int(inp)
            if small == None:
                small = inp
                large = inp
            if inp<small:
                small = inp
            if inp>large:
                large = inp
        except:
            print('Invalid input')
            continue

print('Maximum is',large)
print('Minimum is',small)

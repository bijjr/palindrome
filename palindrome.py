#Normal Mode

import re
import sys

def reverse(arg):
    if len(arg) <= 1:
        return True
    return arg[0] == arg[-1] and reverse(arg[1:-1])

def regex(arg):
    pattern = '[^A-Za-z]'
    string = re.sub(pattern, '', arg.lower())
    if string[0] != string[-1]:
        return False
    return reverse(string)

def is_palindrome(user_input):
    if len(user_input) <= 1:
        return True
    return regex(user_input)

def main():
    user_input = input("Enter a string> ")

if __name__ == "__main__":
    main()


#Advanced

def regex(arg):
    pattern = '[^A-Za-z]'
    string = re.sub(pattern, '', arg.lower())

def is_palindrome(user_input):
    pattern = '[^A-Za-z]'
    old_string = re.sub(pattern, '', user_input.lower())
    new_string =''
    for i in old_string[::-1]:
        new_string += i
    if new_string == old_string:
        print("{} is a palindrome".format(user_input))
        return True
    else:
        print("{} is not a palindrome".format(user_input))
        return False

def main():
    #try to add regex here??
    user_input = input("Enter a string? ")
    return is_palindrome(user_input)

if __name__ == '__main__':
    main()

#Epic Mode
def regex(arg):
    pattern = '[^A-Za-z]'
    new_line = re.sub(pattern, '', arg.lower())
    print('cleaned     ' + new_line)
    return reverse(new_line)

def reverse(arg):
    if len(arg) <= 1:
        return True
    return arg[0] == arg[-1] and reverse(arg[1:-1])

def is_palindrome(arg):
    if len(arg) <= 1:
        print("{} is a palindrome".format(arg))
        return True
    elif regex(arg):
        print("{} is a palindrome".format(arg))
        return True
    else:
        print("{} is not a palindrome".format(arg))
        return False

def main():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            #line = old_line
            print(line,end='  ')
            is_palindrome(line)

if __name__ == '__main__':
    main()

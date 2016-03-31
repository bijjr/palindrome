import re

def reverse_string(string):
    if len(string) == 0:
        return ''
    return reverse_string(string[1:]) + string[0]

def is_palindrome(user_input):
    pattern = '[^A-Za-z]'
    string = re.sub(pattern, '', user_input.lower())
    print("This is the lower " + string)
    backward_input = reverse_string(string)
    print(backward_input + " is the backwards string")
    print(string + " is the regular string")
    if backward_input == string:
        return True
    else:
        return False

def main():
    user_input = input("Enter a word/sentence > ")
    is_palindrome(user_input)

if __name__ == "__main__":
    main()

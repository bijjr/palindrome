##Normal Mode

Your goal for tonight is to write a program that, when run, asks the user to input some text. It can be a phrase, a sentence, or multiple sentences. After it is entered, your program will let the user know if it is a palindrome or not by printing "is a palindrome" or "is not a palindrome" in the output.

Letter casing and punctuation do not matter when testing a palindrome. All of the following are valid palindromes:

stunt nuts
Lisa Bonet ate no basil.
A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!
Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.

##Requirements

Write your main() function to ask the user for a word/sentence, pass it into the is_palindrome function, and state whether or not the the sentence is palindromic.
Write your is_palindrome function using recursion.
Your program must pass all of the tests provided in palindrome_test.py. You should be able to run this with python palindrome_test.py.
You need a function named is_palindrome that takes a string and returns a boolean (True or False). Your program must use this function.

##Advanced Mode (optional)

Complete all of the requirements of Normal Mode.
Make an iterative version of your is_palindrome function (using loops instead of recursion), and ensure it passes the tests too.

##Notes

You may want to use the re.sub function to strip out punctuation and spaces. A regular expression pattern you can use to match all non-alphabetical characters is r'[^A-Za-z]'.

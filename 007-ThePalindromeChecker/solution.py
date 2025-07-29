import re

def is_palindrome(phrase: str):
    normalized_phrase = re.sub(r'[^a-zA-Z0-9]', '', phrase).lower()
    
    if normalized_phrase[::-1] == normalized_phrase:
        print(f'"{phrase}" is a palindrome.')
    else:
        print(f'"{phrase}" is not a palindrome.') 

is_palindrome("Was it a car or a cat I saw?")
"""
Project Milestone: Password Strength
Author: Melissa A. Vieira

"""
import os

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    target_file = file_path if os.path.exists(file_path) else filename

    word_to_check = word if case_sensitive else word.lower()

    try:
        with open(target_file, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                line_word = line.strip()
                if not case_sensitive:
                    line_word = line_word.lower()
                if line_word == word_to_check:
                    return True
    except FileNotFoundError:
        return False

def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False 

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity


def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    if len(password) < min_length:
            print("Password is too short and is not secure.")
            return 1
    
    if len(password) > strong_length:
            print("Password is long, length trumps complexity this is a good password.")
            return 5

    complexity = word_complexity(password)
    return 1 + complexity

def main ():
    user_password = ""
    while user_password.lower() != "q":
        user_password = input("Digit a password to test or 'q' to closed: ")
        if user_password.lower() != "q":
            strength = password_strength(user_password)
            print(f"Password strength: {strength}")
if __name__ == "__main__":
    main()


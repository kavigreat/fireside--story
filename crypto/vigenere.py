from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    init =""
    letter_in_keyword = 0
    for i in range(len(text)):
        if text(i) .isalpha():
            init += rotate_character(text[i], alphabet_position(key[letter_in_keyword % len(key)]))
            letter_in_keyword+=1       
            
        else:
            init += text[i]
        return init
def main():
    message = input("type a message:\n")        

    
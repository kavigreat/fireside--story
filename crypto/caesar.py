from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
        init = " "
        for letter in text:
            init += rotate_character(letter, rot)
        return init

def main():
    message=input("Type a message:\n")
    rotation=int(input("Rotate by:\n"))  
    print(encrypt(message,rotation))  

if __name__ == "__main__":
    main()

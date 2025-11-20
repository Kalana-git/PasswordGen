import random
import string
import pyfiglet

all_char = string.ascii_letters + string.digits + string.punctuation
def RandomString(num_of_char):
    string = "".join(random.choice(all_char) for _ in range(num_of_char))
    return string

def BigBanner(text, font="standard"):
    ascii_banner = pyfiglet.figlet_format(text, font=font)
    print(ascii_banner)

def SmallBanner(text, font="small"):
    ascii_banner = pyfiglet.figlet_format(text, font=font)
    print(ascii_banner)

BigBanner("Password Generator", font="slant")
SmallBanner("Created by Kalana", font="mini")

num_of_char = int(input("How many characters do you want in your password? "))
print(f"Password: {RandomString(num_of_char=num_of_char)}")
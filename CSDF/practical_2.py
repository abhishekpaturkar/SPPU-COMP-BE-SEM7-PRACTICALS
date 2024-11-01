import random
import string
from captcha.image import ImageCaptcha
import PIL.Image
import IPython.display as display

def generate_Captcha():
    # Generate random string
    random_string = string.digits + string.ascii_lowercase
    captcha_text = ''.join(random.choice(random_string) for _ in range(5))
    
    # Generate Captcha from text
    image = ImageCaptcha(width=400, height=200)
    image.generate(captcha_text)
    
    # Save Captcha image and display it
    image.write(captcha_text, "CSDF/content/captcha.png")
    img = PIL.Image.open("CSDF/content/captcha.png")
    display.display(img)
    img.show()
    
    return captcha_text

def verify_Captcha():
    flag = False
    while flag != True:
        captcha_text = generate_Captcha()
        # print(captcha_text)
        user_input = input("Enter CAPTCHA Text \n")
        if user_input == captcha_text:
            print("\nCaptcha Verified Successfully")
            flag = True
        else:
            print("\nInvalid Captcha Entry!!!!!!!!!!!!!!!!!!")

def main():
    verify_Captcha()

if __name__ == "__main__":
    main()
"""
Code Explanation:

1. Import Statements:
   - random: For generating random characters
   - string: Provides string constants
   - ImageCaptcha: For creating CAPTCHA images
   - PIL.Image: For image handling
   - IPython.display: For displaying images

2. generate_Captcha() function:
   - Creates a random 5-character string using digits and lowercase letters
   - Generates a CAPTCHA image (400x200 pixels)
   - Saves the image as "captcha.png"
   - Displays the image
   - Returns the CAPTCHA text

3. verify_Captcha() function:
   - Runs in a loop until correct CAPTCHA is entered
   - Generates new CAPTCHA using generate_Captcha()
   - Takes user input and compares with CAPTCHA text
   - Prints success or error message

4. main() function:
   - Entry point of the program
   - Calls verify_Captcha()

5. Program execution:
   - Checks if script is run directly
   - Calls main() if true
"""
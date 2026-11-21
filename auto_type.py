
import pyautogui
import time

# Read code from a file
with open("code.txt", "r", encoding="utf-8") as file:
    code = file.read()

print("Click inside your code editor within 5 seconds...")
time.sleep(5)

# Type the code character by character
pyautogui.write(code, interval=0.05)

print("Typing completed!")

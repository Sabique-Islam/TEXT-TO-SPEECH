# FOR WINDOWS
import pyttsx3
if __name__ == '__main__':
    print("Welcome to Text to Speech version 1.0 by Sabique... ")
    print("Type 'end' to terminate the program.")
    while True:
        x = input("Enter what you want the system to speak:- ").lower()
        if x == "end":
            print("SEE YOU SOON :)")
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()



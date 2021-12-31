#Program to display ansi art. Make sure you have pyfiglet installed
#if you do not have it installed run: pip install pyfiglet to install it
import pyfiglet

#get the list of available fonts
fonts = pyfiglet.FigletFont.getFonts() + list(str())

#show options
print("|-------Ascii Art Program------|")
print("| Select Options               |")
print("| 1. Show list of fonts        |")
print("| 2. Convert text to ascii art |")
print("| 3. Quit                      |")
print("--------------------------------")

while True:
    #take input from user
    selection = input("Enter your choice(1/2/3): ")

    #prints the list of available fonts
    if selection == '1':
        print(fonts)
        
    #converts text to ascii art
    elif selection == '2':
        text=input("Enter text: ")
        fontsel=input("Choose the font you'd like: ")
        out = pyfiglet.figlet_format(text, fontsel)
        print(out)

    #quits the program
    elif selection == '3':
        break

    #ask if they want to continue the program, if not, break the loop
    #and quit the program
    next_design = input("Do another one? (yes/no): ")
    if next_design == "no":
        break

else:
    print("Invalid input")


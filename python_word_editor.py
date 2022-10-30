
# Welcome the user
print("=================================\n")
print("     Python Word Editor\n")
print("=================================\n")

print("1) Create a file\n")
print("2) Open a file\n\n")
print("=================================\n")
user_selection = input(
    "Enter a number option and press ENTER or type 'q' to quit\n")

# Allow user to generate text and save it to a file
if (user_selection == "1"):

    current_text = input("Start typing:  ")
    file_name = input("Enter file name and press ENTER:")+".txt"
    try:
        text_file = open(file_name, "x")
        text_file.write(str(current_text))
        text_file.close()
    except FileExistsError:
        print("File already exists")
    finally:
        print("Good bye")

    # User opens an existing file and displays cotnent
elif (user_selection == "2"):

    file_name = input("Enter file name plus the extenstion: ")
    try:
        text_file = open(file_name, "r")
        print(text_file.read())
    except FileNotFoundError:
        print("File Not Found")
    finally:
        print("Good bye")

elif (user_selection == "q"):
    print("Good bye")
else:
    print("Invalid Input")

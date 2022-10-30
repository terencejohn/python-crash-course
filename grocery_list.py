# Initial program menu
user_Selection = ""
while user_Selection != "quit":
    print("==========================")
    print("      Grocery List        ")
    print("==========================")

    print("Please select from these options\n")
    print("1) View Grocery List")
    print("2) Remove Groceries")
    print("Q) To quit\n")
    selected_Option = input("Please enter your selection: ")

    groceries = ["Apples", "Avocados", "Bananas", "Berries", "Cherries", "Grapefruit", "Grapes", "Kiwis", "Lemons", "Melon", "Nectarines", "Oranges", "Peaches", "Pears", "Plums"
                 ]

    if (selected_Option == "1"):
        # Display grocery list
        print("\n")
        for item in groceries:
            print(item+"\n")

    elif (selected_Option == "2"):
        # Remove items from the grocery list
        print("\n")
        delete_Successful = "false"
        while (delete_Successful != "true"):

            deleted_Item = input(
                "Enter in the grocery item you wish to delete and press ENTER: ")
            try:
                groceries.remove(deleted_Item)
                print("\n")
                delete_Successful = "true"
            except:
                print("\n")
                print("Invalid item. Try again \n")

            finally:
                for item in groceries:
                    print(item+"\n")

    elif (selected_Option.lower() == "q"):
        user_Selection = "quit"

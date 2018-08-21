def main():
    in_file = open("book_list.csv", "r")
    first_line = in_file.readline()
    print(first_line)
    print("Welcome to Reading Tracker 1.0 by James Elgey")
    #TODO load up csv file
    print("This is the menu: \nOption 1 \nOption 2 \nOption 3")
    user_choice = get_user_choice()
    while user_choice != 'q':
        if user_choice == 'l':
            print("List all books")
        elif user_choice == 'a':
            print("Add new book")
        elif user_choice == 'm':
              print("Mark as read")
        else:
            print("Invalid choice")
        user_choice = get_user_choice()
    print("Thank you for using us")
    #TODO save csv file


def get_user_choice():
    user_choice = input("What would you like to do?")
    user_choice = user_choice.lower()
    return user_choice


main()
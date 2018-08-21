def main():
    str_count = 0
    book_dict = {}
    in_file = open("book_list.csv", "r")
    print("Welcome to Reading Tracker 1.0 by James Elgey")
    #TODO load up csv file
    print("Menu: \nL - List all books \nA - Add a new book \nM - Mark a book as completed \nQ - Quit")
    user_choice = get_user_choice()
    while user_choice != 'q':
        if user_choice == 'l':
            number = 1
            for line in in_file:
                word_str = 0
                book_information = line.split(",")
                book_dict[number] = book_information
                for char in book_information[0]:
                    word_str = word_str + 1
                    if word_str > str_count:
                        str_count = word_str
                number = number + 1
            for item in book_dict:
                print(item)
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
BOOK_NAMES = {}
BOOK_AUTHOR = {}
BOOK_PAGE = {}
BOOK_STATUS = {}

def main():
    TITLE_NUMBER = 0
    AUTHOR_NUMBER = 0
    in_file = open("book_list.csv", "r")
    print("Welcome to Reading Tracker 1.0 by James Elgey")
    #TODO load up csv file
    print("Menu: \nL - List all books \nA - Add a new book \nM - Mark a book as completed \nQ - Quit")
    user_choice = get_user_choice()
    while user_choice != 'q':
        if user_choice == 'l':
            number = 0
            for line in in_file:
                title_count = 0
                author_count = 0
                book_information = line.split(",")
                book_information[-1] = book_information[-1].strip()
                for char in book_information[0]:
                    title_count = title_count + 1
                    if title_count > TITLE_NUMBER:
                        TITLE_NUMBER = title_count
                for char in book_information[1]:
                    author_count = author_count + 1
                    if author_count > AUTHOR_NUMBER:
                        AUTHOR_NUMBER = author_count
                if book_information[3] == "r":
                    book_information[3] = "*"
                elif book_information[3] == "c":
                    book_information[3] = " "
                BOOK_NAMES[number] = book_information[0]
                BOOK_AUTHOR[number] = book_information[1]
                BOOK_PAGE[number] = book_information[2]
                BOOK_STATUS[number] = book_information[3]
                number = number + 1
            for x in range(number):
                print("{} {}. {:{}} by {:{}} {} pages".format(BOOK_STATUS[x], x + 1, BOOK_NAMES[x], TITLE_NUMBER + 2, BOOK_AUTHOR[x], AUTHOR_NUMBER + 2, BOOK_PAGE[x]))
            print("{} books.".format(number))
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
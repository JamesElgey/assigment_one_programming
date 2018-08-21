BOOK_NAMES = {}
BOOK_AUTHOR = {}
BOOK_PAGE = {}
BOOK_STATUS = {}

def main():
    TITLE_NUMBER = 0
    AUTHOR_NUMBER = 0
    PAGE_COUNT = 0
    MAND_BOOK_COUNT = 0
    in_file = open("book_list.csv", "r")
    print("Welcome to Reading Tracker 1.0 by James Elgey")
    #TODO load up csv file
    print("Menu: \nL - List all books \nA - Add a new book \nM - Mark a book as completed \nQ - Quit")
    user_choice = get_user_choice()
    while user_choice != 'q':
        AUTHOR_NUMBER, MAND_BOOK_COUNT, PAGE_COUNT, TITLE_NUMBER, number = convert_file_into_dict(AUTHOR_NUMBER,
                                                                                                  MAND_BOOK_COUNT,
                                                                                                  PAGE_COUNT,
                                                                                                  TITLE_NUMBER, in_file)
        if user_choice == 'l':
            for x in range(number):
                print("{} {}. {:{}} by {:{}} {} pages".format(BOOK_STATUS[x], x + 1, BOOK_NAMES[x], TITLE_NUMBER + 2, BOOK_AUTHOR[x], AUTHOR_NUMBER + 2, BOOK_PAGE[x]))
            print("{} books.".format(number))
            print("You need to read {} pages in {} books.".format(PAGE_COUNT, MAND_BOOK_COUNT))
        elif user_choice == 'a':
            print("Add new book")
        elif user_choice == 'm':
              print("Mark as read")
        else:
            print("Invalid choice")
        user_choice = get_user_choice()
    print("Thank you for using us")
    #TODO save csv file


def convert_file_into_dict(AUTHOR_NUMBER, MAND_BOOK_COUNT, PAGE_COUNT, TITLE_NUMBER, in_file):
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
            PAGE_COUNT = PAGE_COUNT + int(book_information[2])
            MAND_BOOK_COUNT = MAND_BOOK_COUNT + 1
        elif book_information[3] == "c":
            book_information[3] = " "
        BOOK_NAMES[number] = book_information[0]
        BOOK_PAGE[number] = int(book_information[2])
        BOOK_AUTHOR[number] = book_information[1]
        BOOK_STATUS[number] = book_information[3]
        number = number + 1
    return AUTHOR_NUMBER, MAND_BOOK_COUNT, PAGE_COUNT, TITLE_NUMBER, number


def get_user_choice():
    user_choice = input("What would you like to do?")
    user_choice = user_choice.lower()
    return user_choice


main()
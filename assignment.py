BOOK_NAMES = {}
BOOK_AUTHOR = {}
BOOK_PAGE = {}
BOOK_STATUS = {}

def main():
    in_file = open("book_list.csv", "r")
    print("Welcome to Reading Tracker 1.0 by James Elgey")
    #TODO load up csv file
    print("Menu: \nL - List all books \nA - Add a new book \nM - Mark a book as completed \nQ - Quit")
    user_choice = get_user_choice()
    number = 0
    TITLE_NUMBER = 0
    AUTHOR_NUMBER = 0
    PAGE_COUNT = 0
    MAND_BOOK_COUNT = 0
    AUTHOR_NUMBER, MAND_BOOK_COUNT, PAGE_COUNT, TITLE_NUMBER, number = convert_file_into_dict(number, AUTHOR_NUMBER,
                                                                                              MAND_BOOK_COUNT,
                                                                                              PAGE_COUNT,
                                                                                              TITLE_NUMBER, in_file)
    while user_choice != 'q':
        if user_choice == 'l':
            for x in range(number):
                print("{} {}. {:{}} by {:{}} {:5} pages".format(BOOK_STATUS[x], x + 1, BOOK_NAMES[x], TITLE_NUMBER + 2, BOOK_AUTHOR[x], AUTHOR_NUMBER, BOOK_PAGE[x]))
            print("{} books.".format(number))
            print("You need to read {} pages in {} books.".format(PAGE_COUNT, MAND_BOOK_COUNT))
        elif user_choice == 'a':
            print("Add new book")
            new_book_name = input("What is the title of the book?")
            new_book_author = input("What is the name of the author?")
            new_book_pages = input("How many pages does the book have?")
            new_book_status = input("What is the status of the book?")
            BOOK_NAMES[number] = new_book_name
            BOOK_AUTHOR[number] = new_book_author
            BOOK_PAGE[number] = new_book_pages
            BOOK_STATUS[number] = new_book_status
            number = number + 1
        elif user_choice == 'm':
              print("Mark as read")
        elif user_choice == 'p':
            print(BOOK_NAMES[4])
            print(BOOK_AUTHOR[4])
            print(BOOK_PAGE[4])
            print(BOOK_STATUS[4])
        else:
            print("Invalid choice")
        user_choice = get_user_choice()
    out_file = open("book_list.csv", "w")
    for x in range(number):
        if BOOK_STATUS[x] == "*":
            BOOK_STATUS[x] = "r"
        elif BOOK_STATUS[x] == " ":
            BOOK_STATUS[x] = "c"
        out_file_str = BOOK_NAMES[x] + "," + BOOK_AUTHOR[x] + "," + str(BOOK_PAGE[x]) + "," + BOOK_STATUS[x] + "\n"
        print(out_file_str)
        out_file.write(str(out_file_str))
    out_file.close()
    print("Thank you for using us")


def convert_file_into_dict(number, AUTHOR_NUMBER, MAND_BOOK_COUNT, PAGE_COUNT, TITLE_NUMBER, in_file):
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
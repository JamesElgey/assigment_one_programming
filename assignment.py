def main():
    in_file = open("book_list.csv", "r")
    print("Welcome to Reading Tracker 1.0 by James Elgey")
    #TODO load up csv file
    print("Menu: \nL - List all books \nA - Add a new book \nM - Mark a book as completed \nQ - Quit")
    user_choice = get_user_choice()
    book_name_dict = {}
    book_author_dict = {}
    book_page_dict = {}
    book_status_dict = {}
    number = 0
    title_number = 0
    author_number = 0
    page_count = 0
    man_book_count = 0
    book_name_dict, book_author_dict, book_page_dict, book_status_dict, number, author_number, man_book_count, page_count, title_number = convert_file_into_dict(book_name_dict, book_author_dict,
                                                                                              book_page_dict, book_status_dict,
                                                                                              number, author_number,
                                                                                              man_book_count,
                                                                                              page_count,
                                                                                              title_number, in_file)
    while user_choice != 'q':
        if user_choice == 'l':
            for x in range(number):
                print("{} {}. {:{}} by {:{}} {:5} pages".format(book_status_dict[x], x + 1, book_name_dict[x], title_number + 2, book_author_dict[x], author_number, book_page_dict[x]))
            print("{} books.".format(number))
            print("You need to read {} pages in {} books.".format(page_count, man_book_count))
        elif user_choice == 'a':
            new_book_name = input("What is the title of the book?")
            new_book_author = input("What is the name of the author?")
            new_book_pages = input("How many pages does the book have?")
            new_book_status = input("What is the status of the book?")
            book_name_dict[number] = new_book_name
            book_author_dict[number] = new_book_author
            book_page_dict[number] = new_book_pages
            book_status_dict[number] = new_book_status
            number = number + 1
        elif user_choice == 'm':
              print("Mark as read")
        else:
            print("Invalid choice")
        user_choice = get_user_choice()
    out_file = open("book_list.csv", "w")
    for x in range(number):
        if book_status_dict[x] == "*":
            book_status_dict[x] = "r"
        elif book_status_dict[x] == " ":
            book_status_dict[x] = "c"
        out_file_str = book_name_dict[x] + "," + book_author_dict[x] + "," + str(book_page_dict[x]) + "," + book_status_dict[x] + "\n"
        out_file.write(str(out_file_str))
    out_file.close()
    print("Thank you for using us")


def convert_file_into_dict(book_name_dict, book_author_dict, book_page_dict, book_status_dict, number, author_number, man_book_count, page_count, title_number, in_file):
    for line in in_file:
        title_count = 0
        author_count = 0
        book_information = line.split(",")
        book_information[-1] = book_information[-1].strip()
        for char in book_information[0]:
            title_count = title_count + 1
            if title_count > title_number:
                title_number = title_count
        for char in book_information[1]:
            author_count = author_count + 1
            if author_count > author_number:
                author_number = author_count
        if book_information[3] == "r":
            book_information[3] = "*"
            page_count = page_count + int(book_information[2])
            man_book_count = man_book_count + 1
        elif book_information[3] == "c":
            book_information[3] = " "
        book_name_dict[number] = book_information[0]
        book_author_dict[number] = book_information[1]
        book_page_dict[number] = int(book_information[2])
        book_status_dict[number] = book_information[3]
        number = number + 1
    return book_name_dict, book_author_dict, book_page_dict, book_status_dict, number, author_number, man_book_count, page_count, title_number


def get_user_choice():
    user_choice = input("What would you like to do?")
    user_choice = user_choice.lower()
    return user_choice


main()
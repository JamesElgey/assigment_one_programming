#TODO error check when adding books, all new books are required
def main():
    in_file = open("book_list.csv", "r")
    print("Welcome to Reading Tracker 1.0 by James Elgey")
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
            list_book_list(author_number, book_author_dict, book_name_dict, book_page_dict, book_status_dict,
                           man_book_count, number, page_count, title_number)
        elif user_choice == 'a':
            book_name_validity = False
            book_author_validity = False
            page_validity = False
            while book_name_validity != True:
                new_book_name = input("Title:")
                while len(new_book_name) < 1:
                    print("Input cannot be blank")
                    new_book_name = input("Title:")
                book_name_validity = True
            while book_author_validity != True:
                new_book_author = input("Author:")
                while len(new_book_author) < 1:
                    print("Input cannot be blank")
                    new_book_author = input("Author:")
                book_author_validity = True
            while page_validity != True:
                try:
                    new_book_pages = int(input("Pages:"))
                    while new_book_pages < 1:
                        print("Number must be above 0")
                        new_book_pages = int(input("Pages:"))
                    page_validity = True
                except ValueError:
                    print("Invalid input; enter a valid number")
            new_book_status = "*"
            book_name_dict[number] = new_book_name
            book_author_dict[number] = new_book_author
            book_page_dict[number] = new_book_pages
            book_status_dict[number] = new_book_status
            number = number + 1
            print("{} by {}, ({} pages) added to Reading Tracker".format(new_book_name, new_book_author, new_book_pages))
        elif user_choice == 'm':
            if man_book_count == 0:
                print("No required books!")
            else:
                list_book_list(author_number, book_author_dict, book_name_dict, book_page_dict, book_status_dict,
                           man_book_count, number, page_count, title_number)
                marked = False
                while marked != True:
                    try:
                        book_mark_number = int(input("Enter the number of a book to mark as completed:"))
                        book_mark_number = book_mark_number - 1
                        while book_mark_number > number:
                            print("Invalid number")
                            book_mark_number = int(input("Enter the number of a book to mark as completed:"))
                        marked = True
                    except ValueError:
                        print("Not a valid integer!")
                if book_status_dict[book_mark_number] == "*":
                    book_status_dict[book_mark_number] = " "
                    page_count = page_count - book_page_dict[book_mark_number]
                    man_book_count = man_book_count - 1
                    print(book_name_dict[book_mark_number], "by", book_author_dict[book_mark_number], "completed!")
                else:
                    print("That book is already completed!")
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


def list_book_list(author_number, book_author_dict, book_name_dict, book_page_dict, book_status_dict, man_book_count,
                   number, page_count, title_number):
    for x in range(number):
        print("{} {}. {:{}} by {:{}} {:5} pages".format(book_status_dict[x], x + 1, book_name_dict[x], title_number + 2,
                                                        book_author_dict[x], author_number, book_page_dict[x]))
    print("{} books.".format(number))
    if man_book_count == 0:
        print("No books left to read. Why not add a book?")
    else:
        print("You need to read {} pages in {} books.".format(page_count, man_book_count))


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
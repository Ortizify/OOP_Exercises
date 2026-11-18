
import menu
import data


def main():
    print("Welcome to the Student Management System!")

    try:
        data.import_students()
    except FileNotFoundError:
        print("No previous student data found. Starting with an empty list.")

    menu.show_menu()


if __name__ == "__main__":
    main()

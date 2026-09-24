from validator import validate_plate_number
from decoder import decode_plate
from utils import display_result
from database import show_database


def main():

    while True:

        print("\n" + "=" * 45)
        print("      PAK Car Plate Number Decoder")
        print("=" * 45)
        print("1. Decode Plate Number")
        print("2. Show Database")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            plate = input("\nEnter Plate Number (Example: LHR-1234): ")

            valid, prefix, number = validate_plate_number(plate)

            if not valid:
                print(" Invalid Plate Format.")
                continue

            result = decode_plate(prefix)

            if result:
                city, province = result
                display_result(plate.upper(), city, province, number)
            else:
                print(" Registration Code Not Found.")

        elif choice == "2":
            show_database()

        elif choice == "3":
            print("\nThank you for using PAK Car Plate Number Decoder.")
            break

        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
# Owen Mills
# student_information.py
# This app asp for student information and see if they qualify for honor roll or the dean's list.

def main():

    while True:

        # Get the student's first name
        first_name = input("Enter the students's first name or enter 'ZZZ' to exit. ")
        if first_name == "ZZZ":
            break

        # Get the student's last name
        last_name = input("Enter the student's last name. ")
        
        # Get the student's gpa
        gpa = float(input(f"Enter {first_name} {last_name}'s gpa. "))

        # Calculate to see if the student is eligable for either list
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has mad the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not make the Dean's List or the Honor Roll.")


if __name__ == "__main__":
    main()

        
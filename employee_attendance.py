from datetime import datetime

FILE_NAME = "attendance.txt"

employees = {}


# 1. Load data from file
def load_data():
    global employees

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                data = line.strip().split("|")

                if data[0] == "EMP":
                    emp_id = data[1]
                    name = data[2]

                    employees[emp_id] = {
                        "name": name,
                        "attendance": []
                    }

                elif data[0] == "ATT":
                    emp_id = data[1]

                    if emp_id in employees:
                        employees[emp_id]["attendance"].append({
                            "date": data[2],
                            "status": data[3]
                        })

    except FileNotFoundError:
        pass


# 2. Save data to file
def save_data():

    with open(FILE_NAME, "w") as file:

        for emp_id, details in employees.items():

            file.write(
                f"EMP|{emp_id}|{details['name']}\n"
            )

            for record in details["attendance"]:

                file.write(
                    f"ATT|{emp_id}|{record['date']}|{record['status']}\n"
                )


# 3. Add employee
def add_employee():

    name = input("Enter employee name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    emp_id = 101

    while "E" + str(emp_id) in employees:
        emp_id += 1

    emp_id = "E" + str(emp_id)

    employees[emp_id] = {
        "name": name,
        "attendance": []
    }

    save_data()

    print("Employee added:", emp_id, "|", name)


# 4. Mark attendance
def mark_attendance():

    emp_id = input("Enter Employee ID: ").upper().strip()

    if emp_id not in employees:
        print("Employee", emp_id, "not found.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    for record in employees[emp_id]["attendance"]:

        if record["date"] == date:
            print("Attendance for", date, "is already marked.")
            return

    status = input(
        "Enter status (P = Present, A = Absent, L = Leave): "
    ).upper().strip()

    if status not in ["P", "A", "L"]:
        print("Invalid status. Enter P, A or L.")
        return

    employees[emp_id]["attendance"].append({
        "date": date,
        "status": status
    })

    save_data()

    print("Attendance marked successfully!")


# 5. Show attendance report
def show_report():

    emp_id = input("Enter Employee ID: ").upper().strip()

    if emp_id not in employees:
        print("Employee", emp_id, "not found.")
        return

    details = employees[emp_id]

    present = 0
    absent = 0
    leave = 0

    for record in details["attendance"]:

        if record["status"] == "P":
            present += 1

        elif record["status"] == "A":
            absent += 1

        elif record["status"] == "L":
            leave += 1

    total = present + absent + leave

    print(f"{details['name']}: Present {present} | Absent {absent} | Leave {leave}")

    if total == 0:
        print("Attendance: 0.00% (no records)")
    else:
        percentage = (present / total) * 100
        print(f"Attendance: {percentage:.2f}%")

# 6. Main menu
def main():

    load_data()

    while True:

        print("\n===== EMPLOYEE ATTENDANCE SYSTEM =====")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. Show Attendance Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            show_report()

        elif choice == "4":
            save_data()
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()
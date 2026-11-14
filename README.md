# Employee Attendance System

**Name:** Gopika Sahu

**ERP:** RU-26-01700

**Section:** 1L

**Project:** PS 32, Employee Attendance System

## 📖 About This Project

> A small console program that works like a digital attendance register for a company or class.

Most attendance is still tracked on paper or in scattered spreadsheets, which makes it easy to lose track of who was in and who was not. This project keeps everything in one place. You add employees, mark each one as **Present**, **Absent** or **On Leave** for a given date, and then check a report that shows how often they attended.

The program is built to run from the terminal with no setup beyond Python 3. All data is saved automatically, so the records are still there the next time you open it.

✅ **Add** employees with auto-generated IDs (`E101`, `E102`, ...)

📝 **Mark** daily attendance, with protection against duplicate dates

📊 **Report** each employee's counts and attendance percentage

💾 **Save** everything to `attendance.txt`, so nothing is lost when you close the program

> 💡 Start it up tomorrow and everyone is still there.

## 🧠 Language and Concepts

**Language:** Python 3, run from the console. No GUI and no extra installs are needed.

**Concepts used:**

- **Dictionaries:** Each employee is stored as a dictionary, and all employees sit in one dictionary keyed by their ID (`E101`, `E102`, and so on). This makes it quick to find someone by ID. Each attendance record is also a small dictionary with a `date` and a `status`.
- **Lists:** Each employee's attendance is kept in a list of records. The program loops through that list to check for duplicate dates and to count Present, Absent and Leave.
- **Conditions:** `if`, `elif` and `else` decide the menu choice, check whether an ID exists, validate the date and status, and pick the right message to print.
- **Loops:** A `while True` loop keeps the menu running until the user chooses Exit. `for` loops read the file line by line and count records for the report.
- **Functions:** The code is split into small functions such as `add_employee()`, `mark_attendance()` and `show_report()`. Each one does one job, which makes the program easier to read and test.
- **File handling:** `open()` reads `attendance.txt` at startup and writes it after every change. The `with` statement makes sure the file closes properly.
- **String formatting:** f-strings such as `f"{percentage:.2f}"` print the percentage with two decimal places.
- **The `datetime` module:** Used to check that a date really exists. It is the only module this program imports. The PS lists only dictionaries, lists, conditions and file handling, so check whether your teacher allows it.
## Files

- `employee_attendance.py`: the whole program in one file
- `attendance.txt`: created automatically when data is first saved
- `README.md`: this file
- `SUMMARY.md`: project statement, implementation, test cases and conclusion
- `screenshots/`: terminal screenshots of each test case

## How to Run

1. Make sure Python 3 is installed.
2. Put `employee_attendance.py` in a folder.
3. Open a terminal in that folder and run:

   ```
   python employee_attendance.py
   ```

4. Pick an option from the menu and follow the prompts. Choose 4 to save and exit.

## The Menu

```
1. Add Employee
2. Mark Attendance
3. Show Attendance Report
4. Exit
```

## How to Use It

- **Add an employee.** Type a name. The program gives the next free ID, starting from E101.
- **Mark attendance.** Enter the employee ID, a date in `YYYY-MM-DD` format, and a status: `P` for Present, `A` for Absent or `L` for Leave.
- **Show a report.** Enter an ID to see the Present, Absent and Leave counts and the attendance percentage.

## Rules the Program Checks

- The employee ID must already exist. Lowercase is accepted, since the program converts it to uppercase.
- The date must be a real date in `YYYY-MM-DD` format, so `2026-13-45` is rejected.
- The status must be `P`, `A` or `L`.
- Each employee can have only one record per date. A second entry for the same date is rejected.
- A blank name is not allowed.

## How the Data is Stored

Each employee and each attendance record gets its own line in `attendance.txt`:

```
EMP|E101|Aman
ATT|E101|2026-08-01|P
ATT|E101|2026-08-02|P
ATT|E101|2026-08-03|A
ATT|E101|2026-08-04|L
```

The first line of each employee starts with `EMP` and holds the ID and name. Every record below it starts with `ATT` and holds the ID, date and status. Please don't edit this file by hand. If it gets messed up, delete it and start again.

## The Percentage

```
Attendance % = Present ÷ (Present + Absent + Leave) × 100
```

If there are no records, the report shows `0.00% (no records)` instead of dividing by zero.

## Testing

I tested the program in this order, on a fresh `attendance.txt`:

1. Add an employee named `Aman`. He should get E101.
2. Show the report for E101 before marking anything. It should show zeros.
3. Try a wrong employee ID, a bad date like `2026-13-45`, and a bad status like `X`. Each should show an error and save nothing.
4. Mark `2026-08-01` P, `2026-08-02` P, `2026-08-03` A and `2026-08-04` L. Then try `2026-08-02` P again, which should be rejected. The report should show Present 2, Absent 1, Leave 1 and 50.00%.

## Known Limits

- Weekends and holidays are not checked. Any valid
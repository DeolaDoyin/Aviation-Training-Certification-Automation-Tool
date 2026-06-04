import sqlite3
from datetime import datetime, timedelta

DATABASE = "aviation_certifications.db"


def add_personnel(name, department):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO personnel(name, department)
        VALUES (?, ?)
    """, (name, department))

    conn.commit()
    conn.close()

    print("Personnel added successfully.")


def add_certification(personnel_id, cert_name, issue_date, validity_years):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO certifications
        (personnel_id, certification_name, issue_date, validity_years)
        VALUES (?, ?, ?, ?)
    """, (personnel_id, cert_name, issue_date, validity_years))

    conn.commit()
    conn.close()

    print("Certification added successfully.")


def check_certification_status():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.name,
            p.department,
            c.certification_name,
            c.issue_date,
            c.validity_years
        FROM personnel p
        JOIN certifications c
        ON p.id = c.personnel_id
    """)

    records = cursor.fetchall()

    print("\nCERTIFICATION STATUS REPORT")
    print("=" * 70)

    for record in records:
        name, dept, cert_name, issue_date, validity_years = record

        issue_date_obj = datetime.strptime(issue_date, "%Y-%m-%d")

        expiry_date = issue_date_obj + timedelta(days=365 * validity_years)

        today = datetime.today()

        days_remaining = (expiry_date - today).days

        if days_remaining < 0:
            status = "🔴 EXPIRED"

        elif days_remaining <= 30:
            status = "🟡 EXPIRING SOON"

        else:
            status = "🟢 ACTIVE"

        print(f"""
Name: {name}
Department: {dept}
Certification: {cert_name}
Issue Date: {issue_date}
Expiry Date: {expiry_date.date()}
Days Remaining: {days_remaining}
Status: {status}
--------------------------------------------------------
""")

    conn.close()


def menu():
    while True:
        print("""
AVIATION CERTIFICATION TRACKER

1. Add Personnel
2. Add Certification
3. View Status Report
4. Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            name = input("Name: ")
            department = input("Department: ")
            add_personnel(name, department)

        elif choice == "2":
            personnel_id = int(input("Personnel ID: "))
            cert_name = input("Certification Name: ")
            issue_date = input("Issue Date (YYYY-MM-DD): ")
            validity_years = int(input("Validity (Years): "))

            add_certification(
                personnel_id,
                cert_name,
                issue_date,
                validity_years
            )

        elif choice == "3":
            check_certification_status()

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()

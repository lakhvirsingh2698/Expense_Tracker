from src.database.db_connection import connect_db

def main():
    conn = connect_db()
    print("Connected to MySQL successfully!")

if __name__ == "__main__":
    main()


from src.database.db_connection import connect_db

def main():
    conn = connect_db()
    print("Connected to MySQL successfully!")

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (title, amount, category, expense_date) VALUES (%s, %s, %s, %s)",
        ("Test Expense", 100.0, "Test", "2026-03-09")
    )
    conn.commit()
    print("Test record added!")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

from src.database.db_connection import connect_db

def main():
    connection = connect_db()
    cursor = connection.cursor()

    # Insert a test expense
    cursor.execute(
        "INSERT INTO expenses (title, amount, category, expense_date) VALUES (%s, %s, %s, %s)",
        ("Groceries", 500.00, "Food", "2026-03-09")
    )
    connection.commit()
    print("Inserted a test expense!")

    # Fetch and print all expenses
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
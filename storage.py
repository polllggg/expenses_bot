import sqlite3

new_storage = sqlite3.connect("new_database.db")
hand = new_storage.cursor()

def create_table():
    new_string = """
            CREATE TABLE IF NOT EXISTS expenses(
                id integer PRIMARY KEY AUTOINCREMENT,
                amount integer,
                category text,
                date text
    
            )"""
    hand.execute(new_string)
    new_storage.commit()


def add_expense(amount, category, date):
    adding = """
    INSERT INTO expenses(amount, category, date)
    VALUES(?, ?, ?)
    """
    hand.execute(adding, (amount, category, date))
    new_storage.commit()


def get_expenses_by_date(date):
    getting_date = """
        SELECT * FROM expenses WHERE date = ?
        """
    hand.execute(getting_date, (date,))
    return hand.fetchall()


def get_expenses_by_month(date):
    getting_month = """
        SELECT * FROM expenses WHERE date LIKE ?
        """
    hand.execute(getting_month, (date,))
    return hand.fetchall()

def get_stats():
    sum_of_stats = """
    SELECT category,SUM(amount) AS total
    FROM expenses
    GROUP BY category;
    """
    hand.execute(sum_of_stats)
    return hand.fetchall()

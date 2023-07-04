# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3
from sqlite3 import Error

conn = None
def create_connection(db_file):
    """ create a database connection to a SQLite database """

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    #finally:
    #    if conn:
     #       conn.close()

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM meteo10")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')
    #create_connection(r"D:\sqlite\testdb.db")
    try:
        conn = sqlite3.connect(r"D:\sqlite\testdb.db")

        print(sqlite3.version)

    except Error as e:
        print(e)

    cursor = conn.execute("SELECT * from meteo10")

    for row in cursor:
     print ("ID = ", row[0],"  ",row[1],row[2])

    conn.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

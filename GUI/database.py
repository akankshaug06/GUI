import sqlite3


def create_table():
    connection = sqlite3.connect('user.db')  # file open
    cursor = connection.cursor()  # putting a cursor
    # insert update delete
    cursor.execute('CREATE TABLE IF NOT EXISTS userInfo(email TEXT, fname TEXT, lname TEXT, gender INTEGER, age INTEGER)')
    connection.commit()  # save
    connection.close()  # close


def insert(email, fname, lname, gender, age):
    connection = sqlite3.connect('user.db')  # file open
    cursor = connection.cursor()  # putting a cursor
    # insert update delete
    cursor.execute('INSERT INTO userInfo VALUES(?, ?, ?, ?, ?)', (email, fname, lname, gender, age))
    connection.commit()  # save
    connection.close()  # close


def select(email):
    connection = sqlite3.connect('user.db')  # file open
    cursor = connection.cursor()  # putting a cursor
    # insert update delete
    cursor.execute('SELECT * FROM userInfo  WHERE email=?', (email,))
    data = cursor.fetchall()
    connection.commit()  # save
    connection.close()  # close
    return data


def delete(email):
    connection = sqlite3.connect('user.db')  # file open
    cursor = connection.cursor()  # putting a cursor
    # insert update delete
    cursor.execute('DELETE FROM userInfo WHERE email=?', (email,))
    connection.commit()  # save
    connection.close()  # close


def select_all():
    connection = sqlite3.connect('user.db')  # file open
    cursor = connection.cursor()  # putting a cursor
    # insert update delete
    cursor.execute('SELECT * FROM userInfo')
    data = cursor.fetchall()
    connection.commit()  # save
    connection.close()  # close
    return data


# create_table()

# insert('shubham.vishwakarma@gmail.com','Shubham', 'Vishwakarms', 1, 25)
# insert('amanupadhyay32@gmail.com', 'Aman','Upadhyay', 1, 24)
# print(select('amanupadhyay32@gmail.com'))
# delete('amanupadhyay32@gmail.com')

# print(select_all())
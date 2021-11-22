import sqlite3

def main(command):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(command)
        result = cursor.fetchall()
        name = []
        for i in range(len(cursor.description)-1):
            name.append(cursor.description[i][0])
        data = []
        for i in result:
            print(i)
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error ==>"+ str(error))
    
    finally:
        if(connection):
            connection.close()

if __name__ == '__main__':
    
    
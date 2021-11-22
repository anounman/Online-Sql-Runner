import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
    
app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])
def sql():
        try:
            command = ''
            if request.method == "POST":
                command = request.form.get("msg")
                print("\n\n"+command+"\n\n")
            if command == '':
                command = "select * from Customers;"
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute(command)
            result = cursor.fetchall()
            name = []
            for i in range(len(cursor.description)):
                name.append(cursor.description[i][0])
            data = []
            for i in result:
                data.append(i)
            connection.commit()
            cursor.close()
            if(connection):
                connection.close()
            return render_template('index.html' , len_of_name=len(name), len_of_data=len(data),name=name, data=data , error='')
        except sqlite3.Error as error:
            error = str(error)
            return render_template('index.html' , error=str(error))
if __name__ == '__main__':
    app.run(debug=True)
    
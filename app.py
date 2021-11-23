import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash , redirect

import os
app = Flask(__name__)

if os.name == 'nt':
    os.system("copy '.\database (1).db' .\database.db")
else:
    os.system("cp './database (1).db' './database.db'")
@app.route('/' , methods=['GET', 'POST'])
def sql(command = ''):
        try:
            if request.method == "POST":
                command = request.form.get("msg")
            if command == '':
                command = "select * from Customers;"
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            # print(str(command))
            cursor.execute(str(command))
            result = cursor.fetchall()
            if result:
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
            if result:
                return render_template('index.html' , len_of_name=len(name), len_of_data=len(data),name=name, data=data , command=str(command) , error='')
            else:
                return render_template('index.html' , len_of_name=0, len_of_data=0,name=[], data=[] , command=str(command) , error='')
        except sqlite3.Error as error:
            error = error
            return render_template('index.html' , error=error)
@app.route('/Customers')
def Customers():
    return sql("select * from Customers;")
@app.route('/Categories')
def Categories():
    return sql("select * from Categories;")
@app.route('/Employees')
def Employees():
    return sql("select * from Employees;")
@app.route('/Orders')
def Orders():
    return sql("select * from Orders;")

if __name__ == '__main__':
    app.run(debug=True)
    
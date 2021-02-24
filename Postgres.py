# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:32:34 2021

@author: SEAN.SH.CHEN
"""
# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('home.html')

# if __name__ == '__main__':
#     # app.debug = True
#     app.run()
import os
import psycopg2
class main():
    def __init__(self, Text):
        self.return_value=""
        self.return_value+="\n__init__\n"
        self.Text=Text.split("\n")
        self.Text.pop(0)
        if Text[1].upper=="W":
            self.write()
        elif Text[1].upper=="R":
            self.read()
        else:
            self.return_value+="No this type "+Text[1]
            return self.return_value
    def write(self):
        self.return_value+="write\n"
        for i in self.Text:
            self.return_value+=i+"\n"
        return self.return_value
    def read(self):
        self.return_value+="read\n"
        for i in self.Text:
            self.return_value+=i+"\n"
        return self.return_value

# DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a linebot0223').read()[:-1]

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# cursor = conn.cursor()

# SQL_order = '''CREATE TABLE warehouse(
#             item VARCHAR (50) UNIQUE NOT NULL,
#             count NUMERIC (50) NOT NULL,
#             unit VARCHAR (3) ,
#             date DATE NOT NULL
#         );'''
# SQL_order = "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'warehouse';"
# SQL_order = "SELECT * FROM warehouse;"
# SQL_order = "INSERT INTO warehouse (item, count, unit, date) VALUES ('雞蛋', 2, '顆', '2021-02-24');"
# SQL_order = '''DROP TABLE IF EXISTS Warehouse'''
# cursor.rowcount
# cursor.execute(SQL_order)

# data = []
# while True:
#     temp = cursor.fetchone()
# cursor.fetchall()
#     if temp:
#         data.append(temp)
#     else:
#         break
# print(data)

# conn.commit()

# cursor.close()
# conn.close()

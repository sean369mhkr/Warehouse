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
import datetime
now=datetime.datetime.now()
date=now.strftime("%Y/%m/%d")
class main():
    def __init__(self, Text):
        self.return_value=""
#        self.return_value+="\n__init__\n"
        self.Text=Text.split("\n")
        self.Text.pop(0)
        DATABASE_URL = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.cursor = self.conn.cursor()
    def add(self):
        for i in self.Text:
            inputdata=i.split(" ")
            item=inputdata[0]
            count=inputdata[1]
            unit=inputdata[2]
            SQL_order = f"SELECT * FROM warehouse WHERE item='{item}';"
            self.cursor.execute(SQL_order)
            temp=self.cursor.fetchone()
            if temp==None:
                SQL_order = f"INSERT INTO warehouse (item, count, unit, date) VALUES ('{item}',{count}, '{unit}', '{date}');"            
            else:
                count=str(float(temp[1])+float(count))
                SQL_order = f"UPDATE warehouse SET count = {count} WHERE item ='{item}'"
            try:
                self.cursor.execute(SQL_order)
                self.conn.commit()
                self.return_value+="Success"
            except:
                self.return_value+="Fail\n"
                self.return_value+="例子:雞蛋 2 顆\n"
                break
        self.cursor.close()
        self.conn.close()
        return self.return_value
            
    def reduce(self):
        pass
#        self.return_value+="write\n"
#        for i in self.Text:
#            self.return_value+=i+"\n"
#        return self.return_value
    def read(self):
        SQL_order = "SELECT * FROM warehouse;"
        self.cursor.execute(SQL_order)
        temp=self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        for i in temp:
            self.return_value+=' '.join(map(str, i))
            self.return_value+="\n"
        return self.return_value
#        self.return_value+="read\n"
#        for i in self.Text:
#            self.return_value+=i+"\n"
#        return self.return_value
    def ntype(self):
        self.return_value+="No this type"
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

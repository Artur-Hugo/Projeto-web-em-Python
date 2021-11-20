from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__) 
app.config.from_object('config')

#utilizaremos o flask para gerenciar o banco de dados db
db = SQLAlchemy(app)

migrate = Migrate(app, db)

#para poder usar os comandos de SqLite
manager = Manager(app)
manager.add_command('db', MigrateCommand)

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='root')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS restaurante")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)



import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
empdata = pd.read_csv(r'C:\Users\artur\Desktop\heroku\Consumir a API em python\app\Fast_Food_Restaurants_US.csv',index_col=False, delimiter = ',')
empdata.head()

try:
    conn = msql.connect(host='localhost', user='root',  
                        password='root')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("USE RESTAURANTE;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE IF NOT EXISTS comercio(codigo int(4) AUTO_INCREMENT,address varchar(255),categories varchar(255),city varchar(255),country varchar(255),latitude varchar(255),longitude varchar(255),name varchar(255),postalCode varchar(255),province varchar(255),websites varchar(255),PRIMARY KEY (codigo));")
        print("Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = 'INSERT INTO comercio (address,categories,city,country,latitude,longitude,name,postalCode,province,websites) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)

from app.controllers import default

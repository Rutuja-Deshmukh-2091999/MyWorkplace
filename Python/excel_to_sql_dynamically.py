import mysql.connector
import pandas as pd
from os import walk
import os
from mysql.connector import Error

dir_path = r"C:\Users\User\Downloads\Source"
for(dirpath,dirnames,filenames) in walk(dir_path):
    for file in filenames:
        os.chdir(dir_path)
        open(file)
        fs = pd.read_excel(file, sheet_name='Sheet1')
        columns = fs.columns.values
        str1 = ""
        col1 = ""

        for col in columns:
            str1 += col + ' VARCHAR(500)'
            str1 += ','
            col1 += col + ','
        col1 = col1.rstrip(',')
        finallist1 = str1.rstrip(',')
        tb = (str(file))
        tb1 = tb.strip('.xlsx')
        try:
            connection = mysql.connector.connect(host='localhost',
                                            database='new_test',
                                            user='root',
                                            password='root')

            constring = ('CREATE TABLE IF NOT EXISTS '+tb1+' ('+finallist1+')');
            cursor = connection.cursor()
            cursor.execute(constring)
            row = fs.values
            row = list(row)
            cursor.execute('TRUNCATE TABLE '+tb1+'')
            connection.commit()

            for i in row:
                i1 = list(i)
                print(i1)
                str4 = str(i1[0])
                insertstr = ('INSERT into '+tb1+' ('+col1+') VALUES ( '+','.join(['%s'] * len(columns))+' )')
                cursor.execute(insertstr,i1)
                connection.commit()

            str1 = ""
            tb1 = ""
            finallist1 = ""
            tb = ""


        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


print("Successfull")
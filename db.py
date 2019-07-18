
import mysql.connector
import csv


mydatabase = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity')
cursor = mydatabase.cursor()
csv_data = csv.reader(open('modify.csv'))
for row in csv_data:
	cursor.execute('INSERT INTO dataTable(User, URL, Title) VALUES (%s, %s, %s)', row)

mydatabase.commit()
cursor.close()










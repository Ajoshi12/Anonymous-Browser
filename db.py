
import mysql.connector 
import csv #import csv file

#connect to database using db parameters
mydb = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity')
curs = mydb.cursor() #used to traverse database line by line
csv_data1 = csv.reader(open('user1.csv')) #open csv file for data transfer
next(csv_data1) #skip header row of csv file
csv_data2 = csv.reader(open('user2.csv'))
next(csv_data2)
csv_data3 = csv.reader(open('user3.csv'))
next(csv_data3)
csv_data4 = csv.reader(open('user4.csv'))
next(csv_data4)
csv_data5 = csv.reader(open('user5.csv'))
next(csv_data5)
#traverse through each row in csv file
for row in csv_data1:
	#insert csv data into database table
	curs.execute('INSERT INTO dataTable(User, URL, Title) VALUES (%s, %s, %s)', row)
for row in csv_data2:
	curs.execute('INSERT INTO dataTable(User, URL, Title) VALUES (%s, %s, %s)', row)
for row in csv_data3:
	curs.execute('INSERT INTO dataTable(User, URL, Title) VALUES (%s, %s, %s)', row)
for row in csv_data4:
	curs.execute('INSERT INTO dataTable(User, URL, Title) VALUES (%s, %s, %s)', row)
for row in csv_data5:
	curs.execute('INSERT INTO dataTable(User, URL, Title) VALUES (%s, %s, %s)', row)
curs.close()
mydb.commit()
mydb.close() #close cursor and database connection












import mysql.connector 
import csv #import csv file

#connect to database using db parameters
mydb = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity')
curs = mydb.cursor() #used to traverse database line by line
csv_data = csv.reader(open('modify.csv')) #open csv file for data transfer
next(csv_data) #skip header row of csv file
#traverse through each row in csv file
for row in csv_data:
	#insert csv data into database table
	curs.execute('INSERT INTO dataTable(User, URL, Title) VALUES (%s, %s, %s)', row)
curs.close()
mydb.commit()
mydb.close() #close cursor and database connection











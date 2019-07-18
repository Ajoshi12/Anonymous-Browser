# from flask import Flask, render_template
# from flask_mysqldb import MySQL
import mysql.connector
import csv
# app = Flask(__name__)

mydatabase = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity')
cursor = mydatabase.cursor()
csv_data = csv.reader(open('new.csv'))
for row in csv_data:
	cursor.execute('INSERT INTO dataTable(User, URL, Title) VALUES (%s, %s, %s)', row)
	# print (row)
mydatabase.commit()
cursor.close()

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'crowdAnn'
# app.config['MYSQL_PASSWORD'] = 'cmps115!'
# app.config['MYSQL_DB'] = 'CrowdSourcedAnonymity'

# mysql = MYSQL(app)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == "POST":
#     	#Get form data
#         # details = request.form
#         # name = details['name']
#         # email = details['email']
#         csv_data = csv.reader(file('test.csv'))
#         cursor = mysql.connection.cursor()
#         for row in csv_data:
#             cursor.execute("INSERT INTO userHistory(User, URL, Title) VALUES (%s, %s, %s)", row)
#         fetchdata = cursor.fetchall()
#         cursor.close()
#         mysql.connection.commit()
#     return render_template('index.html', data = fetchdata)
# if __name__ == '__main__':
# 	app.run(debug=True)



from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import csv
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'crowdAnn'
app.config['MYSQL_PASSWORD'] = 'cmps115!'
app.config['MYSQL_DB'] = 'CrowdSourcedAnonymity'

mysql = MYSQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        csv_data = csv.reader(file('test.csv'))
        cursor = mysql.connection.cursor()
        for row in csv_data:
            cursor.execute("INSERT INTO userHistory(User, URL, Title) VALUES (%s, %s, %s)", row)
        mysql.connection.commit()
        cursor.close()


if __name__ == '__main__':
    app.run()
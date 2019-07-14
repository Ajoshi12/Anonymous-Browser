from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import csv
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        csv_data = csv.reader(file('test.csv'))
        cursor = mysql.connection.cursor()
        for rows in csv_data:
            cursor.execute("INSERT INTO MyUsers(url,title, visited_on, visited_count, typed_count, referrer, visit_ID , profile,url_length,transition_type, transition_qualifiers) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
        mysql.connection.commit()
        cursor.close()


if __name__ == '__main__':
    app.run()

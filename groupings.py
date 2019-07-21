
import mysql.connector
from mysql.connector import errorcode
import csv
import random

distinct_users = []
try:

# don't know if I need to reconnect again since aishu didn't close the connection
mydatabase = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity')

cursor = mydatabase.cursor()
sql_select_Query = "select distinct User from dataTable"
records = cursor.fetchall() # runs the select statement to get all distinct users
for row in records:
       distinct_users.append(row)
cursor.close()

except Error as e :
    print ("Error while connecting to MySQL", e)

 # distinct_users list should have all the users rn
 ###################################################################################

 # next step is to randomize
randomUsers = []
 while distinct_users is not []:
     #  randomize the order
    pick = random.choice(distinct_users)
    randomUsers.append(pick) # adds the random pick to our random ordered list
    distinct_users.remove(pick) # remove the random pick from distinct_users

#########################After randomizing now we have to create groups####################
Random_list = [data_list[i:i+4] for i in range(0, len(data_list), 4)]
#########################################################################################
# this creates an list of lists of size 4  but I think OUR CSV NEEDS MULPTIPLE OF 4 USERS IN ORDER FOR THIS TO WORK!!!!!!!!!!!!!!!!!!
#########################################################################################
for i in range(len(Random_list)):
    for j in range(len(Random_list[i])):
        creating_CSV(Random_list[i][j],"Randomized_History.csv")
              
SELECT mydatabase = mysql.connector.connect, host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity"
FROM  csv.writer( SELECT user )
as "cursor.execute" filename;

def creating_CSV(ID,filename)
    try:
        mydatabase = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity')
        cursor = mydatabase.cursor(prepared=True)
        sql_select_query = """select * from dataTable where user = %s"""
        cursor.execute(sql_select_query, (ID, ))
        record = cursor.fetchall()
        with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # writing into the csv file
        for row in records:
            csvwriter.writerow(row + ',')
        cursor.close()

    except Error as e :
        print ("Error while in db when creating csv file", e)

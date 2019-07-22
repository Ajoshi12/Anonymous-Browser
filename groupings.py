import mysql.connector
from mysql.connector import Error
import csv
import random

distinct_users = []
try:
    # connect to database and select User from db table
    mydatabase = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity') 
    cursor = mydatabase.cursor()
    sql_select_Query = "select User from dataTable"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall() # runs the select statement to get all distinct users
    for row in records:
        distinct_users.append(row) # add each User to distinct_users list
    cursor.close()

except Error as e:
    print ("Error while connecting to MySQL", e)

finally:
    #close database connection
    if(mydatabase.is_connected()):
        mydatabase.close()

    # distinct_users list should have all the users now
 ###################################################################################

# randomize users
randomUsers = []
while distinct_users != []:
    #  pick a random user in list
    pick = random.choice(distinct_users)
    print(randomUsers)
    randomUsers.append(pick) # adds the random pick to our random ordered list
    distinct_users.remove(pick) # remove the random pick from distinct_users

#########################After randomizing now we have to create groups####################
Random_list = [randomUsers[i:i+4] for i in range(0, len(randomUsers), 4)]
#########################################################################################
# this creates our groups 
# now we have to create a csv file for each group 
for i in range(len(Random_list)):
    for j in range(len(Random_list[i])):
        creating_CSV(Random_list[i][j],"Randomized_History.csv")

def creating_CSV(ID, filename):
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
        mydatabase.close()

    except Error as e:
        print ("Error while in db when creating csv file", e)

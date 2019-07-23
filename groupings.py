import mysql.connector
from mysql.connector import Error
import csv
import random

random_csv = open("Random_history.csv", "w+")
random_csv.write("URL\n")
distinct_users = []
try:
    # connect to database and select User from db table
    mydatabase = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity')
    cursor = mydatabase.cursor()
    sql_select_Query = "select distinct User from dataTable"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall() # run the select statement to get all distinct users
    for row in records:
        distinct_users.append(row) # add each User to distinct_users list
    cursor.close()

except Error as e:
    print ("Error while connecting to MySQL", e)

finally:
    # close database connection
    if(mydatabase.is_connected()):
        mydatabase.close()

# distinct_users list should have all the users now
###################################################################################

# randomize users
randomUsers = []
while distinct_users != []:
    # pick a random user in list
    pick = random.choice(distinct_users)
    randomUsers.append(pick) # add the random pick to our random ordered list
    distinct_users.remove(pick) # remove the random pick from distinct_users

#########################After randomizing now we have to create groups####################
Random_list = [randomUsers[i:i+4] for i in range(0, len(randomUsers), 4)]
#########################################################################################
# function to create csv file
def creating_CSV(Random_list, i,filename):
    # this loop takes account of each member in the group
    for j in range(len(Random_list[i])):
        ID = Random_list[i][j]
        # connect to database and get all user data
        mydatabase = mysql.connector.connect(host='localhost', user='crowdAnn', password='cmps115!', database='CrowdSourcedAnonymity')
        cursor = mydatabase.cursor()
        sql_select_query = """select * from dataTable where user = %s order by rand() limit 3"""
        cursor.execute(sql_select_query, ID)
        record = cursor.fetchall()
        # get the urls of the users and put it in file
        for n in range(len(record)):
            for m in range(len(record[n])):
                if("http" in record[n][m]):
                    filename.write(record[n][m]+"\n")

# create a csv file for each group
for i in range(len(Random_list)):
    creating_CSV(Random_list, i,random_csv)

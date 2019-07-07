#!/usr/bin/python
import csv

banned = ['air']
def rm_ban(csv_file):
    columns = []
    rows = []
    with open(csv_file,'r') as open_file:
        csv_read = csv.reader(open_file)
        for row in csv_read:
            url = row[0]
            for ban in banned:
                if((ban in url) == False):
                    rows.append(row)
    with open(csv_file,'w') as write_file:
        csv_write = csv.writer(write_file)
        #for row in rows:
        csv_write.writerows(rows)      
rm_ban("test.csv")

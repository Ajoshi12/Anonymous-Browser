#!/usr/bin/python
import csv 
banned = {'https://timesofindia.indiatimes.com':'https://timesofindia.times.com'}
def rm_ban(csv_file):
    columns = []
    rows = []
    with open(csv_file,'r') as open_file:
        csv_read = csv.reader(open_file)
        for row in csv_read:
            url = row[0]
            #parse url up till end of .com - call it main_url
            main_index = url.find('.com') + 4
            main_url = url[:main_index]
            if(banned.get(main_url) == None):
                rows.append(row)
    with open(csv_file,'w') as write_file:
        csv_write = csv.writer(write_file)
        #for row in rows:
        csv_write.writerows(rows)      
rm_ban("sent.csv")

#!/usr/bin/python
import csv 
#banned url to remove from csv file
banned = {'https://www.msn.com':'https://www.msn.com'}
def rm_ban(csv_file):
    columns = []
    rows = []
    #scan through urls in csv file
    with open(csv_file,'r') as open_file:
        csv_read = csv.reader(open_file)
        for row in csv_read:
            url = row[1]
            #parse url up till end of .com - call it main_url
            main_index = url.find('.com') + 4
            main_url = url[:main_index]
            if(banned.get(main_url) == None):
                rows.append(row)
    #write the urls back into csv file
    with open(csv_file,'w') as write_file:
        csv_write = csv.writer(write_file)
        #for row in rows:
        csv_write.writerows(rows)      
rm_ban("user2.csv") #call ban function on this csv file


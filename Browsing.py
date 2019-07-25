import csv
import webbrowser
import random
import time
def visit_sites(csv_file):
    #read csv file
    with open(csv_file,'r') as open_file:
        csv_read = csv.reader(open_file)
        next(csv_read)
        next(csv_read)
        #iterate through rows in csv file
        for row in csv_read:
            skip_test_number = random.randint(1,10)
            print(skip_test_number)
            #skip random urls
            if(skip_test_number > 7):
                print("Skipping this iteration!")
                continue
            url_to_visit = row[0] #pick the url from the row of the csv file
            print("Now visiting", url_to_visit)
            #wait for some time before opening new url
            time_to_sleep = random.randint(1,5)
            time.sleep(time_to_sleep)
            #open url in web browser
            webbrowser.open(url_to_visit)

visit_sites('test.csv') #call function on csv file
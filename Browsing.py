import csv
import webbrowser
import random
import time
def visit_sites(csv_file):
    with open(csv_file,'r') as open_file:
        csv_read = csv.reader(open_file)
        next(csv_read)
        next(csv_read)
        for row in csv_read:
            skip_test_number = random.randint(1,10)
            print(skip_test_number)
            if(skip_test_number > 7):
                print("Skipping this iteration!")
                continue
            url_to_visit = row[0]
            print("Now visiting", url_to_visit)
            time_to_sleep = random.randint(1,5)
            time.sleep(time_to_sleep)
            webbrowser.open(url_to_visit)

visit_sites('test.csv')
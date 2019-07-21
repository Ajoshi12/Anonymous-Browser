import csv
import webbrowser
def visit_sites(csv_file):
    with open(csv_file,'r') as open_file:
        csv_read = csv.reader(open_file)
        row_count = sum(1 for row in csv_read)
        counter = 2
        for row in csv_read:
            url_to_visit  = row[0]
            main_index = url.find('.com') +_4
            main_url = url[:main_index]
            print("The url we are visiting is")
            print(main_url)
            if (counter % 2 == 0):
                webbrowser.open(main_url)
            counter = counter + 1

visit_sites('test.csv')
webbrowser.open('www.google.com')
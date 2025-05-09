# importing csv module
import csv

# csv file name
filename = "results.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
modrem=0
# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    #if row==2:
        
    # parsing each column of a row
    for col in row:
        if(col==2):
            col=0
            print("%10s" % col, end=" "),
        else:
            print("%10s" % col, end=" "),
    print('\n')
    hasattr
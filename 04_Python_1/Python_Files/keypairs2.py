import csv

csv_columns = ['First & Last Name','Job Title','Company']

name = str(input("First & Last Name: "))
job_title = str(input("Job Title: "))
company = str(input("Company: "))

dict = [ {"First & Last Name": name,
"Job Title":  job_title, 
"Company": company} ]

csv_file = "Names.csv"
try:
    with open(csv_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict:
            writer.writerow(data)
except IOError:
    print("I/O error")

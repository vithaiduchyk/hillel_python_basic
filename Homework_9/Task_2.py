import csv

names_csv = 'names.csv'
emails_csv = 'emails.csv'

with open(names_csv, 'r', newline='') as input_file, open(emails_csv, 'w', newline='') as emails_csv:
    reader = csv.reader(input_file)
    writer = csv.writer(emails_csv)
    next(reader)

    for row in reader:
        email = row[2]
        writer.writerow([email])

print(f'Emails extracted and written to', {emails_csv})

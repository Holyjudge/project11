import csv
import os



import smtplib as s
test_dict={'anshul': 'anshulguptadps2@gmail.com','aparna':'aparnajha2003@gmail.com','ada':'adarshnr2020@gmail.com','aman':'amankumarjha@gmail.com','arvind':'arvind@gmail.com'}

f=open('Attendance.csv','r')
reader=csv.reader(f)
people={}

for row in reader:
    people[row[0]] = {'name':row[0]}

result2=list(people.items())
print(result2)



# printing original dictionary
#print("The original dictionary is : " + str(test_dict))

# Using items() + list comprehension + dict()
# Remove multiple keys from dictionary
res = dict([(key, val) for key, val in
            test_dict.items() if key not in result2])

result=list(res.values())
print(result)

EMAIL_ADD='anshulguptadps2@gmail.com'
EMAIL_PAS='lsqhngbwftpszbfu'

with s.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADD,EMAIL_PAS)
    #contacts=['anshulguptadps@gmail.com','adarshnr2020@gmail.com','abhiseksahoo57556@gmail.com','aparnajha2003@gmail.com']
    contacts=result
    subject='NHCE Academics Department'
    body='Your ward has not attended python class today'
    msg=f'subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADD,contacts,msg)

from datetime import date
from datetime import time
from datetime import datetime 
import csv
name = input("Greetings Buddy! Please enter your name: ")
print("Hello!",name)

project_id = input("Kindly enter your project id: ")
print("Great!")
 
kick_start = input( "Are you ready to start working now ?  Type Yes or No : ")
start_project = datetime.now()
if kick_start == "Yes" :
    print("Project Started at ", start_project, "ALL THE BEST! Kindly come back when you're done.")
else:
    print("Please come back when ready")


completion = input("Hello again! Are you done with the day's work? Type Yes or No : ")

end_project = datetime.now()

print("Project brought to completion at ", end_project, ",Kudos!" ) 

time_difference = end_project-start_project


time_conv = time_difference.seconds
time_elapsed = float(time_conv/3600)
print("Time taken to complete this project is" , time_elapsed , "hours")
amount_earned = time_elapsed * 5
print("The amount of money accrued today is " "$ ",amount_earned)


#myData = [[start_project, end_project, time_elapsed, amount_earned]]
#myFile = open('NanaWages.csv', 'a')
#with myFile:
#    writer = csv.writer(myFile)
#    writer.writerows(myData)

with open('Nana_Earnings.csv','a',newline = '') as f:
    fieldnames = ['Project_id','Kick_Start','End','Time_taken','Amount_Accrued']
    writer = csv.DictWriter(f,fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'Project_id':project_id,'Kick_Start':start_project,'End':end_project,'Time_taken':time_elapsed,'Amount_Accrued':amount_earned})      
    f.close()

  
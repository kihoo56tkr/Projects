import win32com.client
import openpyxl
from datetime import datetime, timedelta
 
#today = "2024-07-10 09:26:37"
#formatdt = '%Y-%m-%d %H:%M:%S'
 
#temp = datetime.strptime(today,formatdt)
#today = datetime.strptime(today,formatdt)
today = datetime.today()
today_day = today.strftime("%d")
today_month = today.strftime("%B")
today_month2 = int(today.strftime("%m"))
today_year = int(today.strftime("%Y"))
 
first_day_todaymonth = datetime(today_year, today_month2, 1)
print("First day of Today's Month: ", first_day_todaymonth)
 
yesterday = first_day_todaymonth - timedelta(days = 1)
yesterday = yesterday.strftime("%d %B %Y")
print("Last day of Quarter: ", yesterday)
 
temp = datetime.today()
 
number_of_days = 2
for i in range(2):
    temp += timedelta(days = 1)
    if temp.strftime("%A") == "Saturday" or temp.strftime("%A") == "Sunday":
        number_of_days += 1
 
stop = True       
while stop:
    temp1 = today + timedelta(days = number_of_days)
    if temp1.strftime("%A") == "Saturday" or temp1.strftime("%A") == "Sunday":
        number_of_days += 1
    else:
        stop = False
deadline = today + timedelta(days = number_of_days)
deadline_day = deadline.strftime("%A")
deadline = deadline.strftime("%d %B %Y")
print("Today: ", today)
print("Deadline: ", deadline, " (", deadline_day, ")")
 
outlook=win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox=outlook.GetDefaultFolder(6)
 
message = inbox.Items
message2 = message.GetLast()
subject = message2.Subject
body=message2.Body
date=message2.SentOn.date()
sender=message2.Sender
attachments=message2.Attachments
 
Quarter = dict(January=4, February=4, March=4, April=1, May=1, June=1, July=2, August=2, September=2, October=3, November=3, December=3)
if Quarter[today_month] == 4:
    today_year -= 1
 
# Check whether Email has been sent out before
send_email = True
Subjectemail = ' - ' + str(Quarter[today_month]) + "Qtr" + str(today_year)
for email in message:
    if email.Subject == Subjectemail:
        send_email = False
 
if send_email == True:
    # Creating Dataframe
    file = openpyxl.load_workbook(r'C:\Users\.xlsx')
    sheet_name = ''
    worksheet = file[sheet_name]
    emails = []
    column_index = 12 # need to change based on where they put keyword col
    for cell in worksheet.iter_cols(min_col = column_index, max_col = column_index, values_only = True):
        for email in cell[1:]:
            if email not in emails and email != None:
               emails.append(email)
    emails = ';'.join(emails)
    link = ""
    style = f"""
        <div style='padding: 10px;'>
        <span style='color: #000000; font-family: Calibri; font-size: 14px'>{"Dear"}
        </div> <br>
        </span><span style='font-weight: bold; color: #FF0000; font-family: Calibri; font-size: 14px'>{"Please update this link for data as of " + yesterday}
                {" (or Q" + str(Quarter[today_month]) + " " + str(today_year) + ")"}
        <u>{" by " + deadline}</u>
        </span><span style='font-weight: bold; color: #000000; font-family: Calibri; font-size: 14px'>{', and we will extract the necessary inputs from the link on ' + deadline_day + " (end of day), "}
                {deadline + "."}
        </div> <br>
        </span><span style='font-family: Calibri; font-size: 14px'><a href = {link}>https://</a>
        </span><span style='font-weight: bold; color: #000000; font-family: Calibri; font-size: 14px'>{" - "}
        </div> <br>
        </span><span style='font-family: Calibri; font-size: 14px'>{"Rgds"}
        </div>
        <span style='font-family: Calibri; font-size: 14px'>{"Name"}
        </div>
        <span style='font-size: 12px; color: #000000'>{"-"}      
        """
    # Send Email
    ol=win32com.client.Dispatch("outlook.application")
    olmailitem=0x0 #size of the new email
    newmail=ol.CreateItem(olmailitem)
    newmail.Subject= '[For  - ' + str(Quarter[today_month]) + "Qtr" + str(today_year)
    newmail.To= emails
    newmail.CC= '' # Change to User Email
    newmail.HTMLBody = style
    newmail.Send()
    print("DONE sending")
else:
    print("Email " + Subjectemail + " has been sent before!")
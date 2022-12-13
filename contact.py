
  
"""These project involves in taking student details as input and stores in a json_file
    """
  
# Import date class from datetime module
from datetime import datetime
import json
information={}  
   
file_c=open("contact_inform.json","a")

name=input("enter the name of the student :")
Mobile_no=int(input("enter the mobile no"))
email=input("enter the email")
Address=input("enter adress of the student")
Date_S= datetime.now()


formatted_datetime = Date_S.isoformat()
json_datetime = json.dumps(formatted_datetime)


details=(Mobile_no,email,Address,json_datetime)



information[name] =details

file_c.write((json.dumps(information)))
  
with open('contact_inform.json') as f:
   data = json.load(f)
   print(data)
   










from firebase import firebase
firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
#collecting details from the doctor
name = input("Enter doctor name :") 
age = input("Enter doctor age :") 
dob = input("Enter doctor dob :") 
edu = age = input("Enter doctor specialization :") 
result=firebase.put('/hospital-management-syst-bd8b0/Doctors',name,{'name':name,'age':age,'dob':dob,'edu':edu,})
print(result)

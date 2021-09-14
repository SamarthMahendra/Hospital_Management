from firebase import firebase
firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
id = input("Enter  patient id : ") 
print(id) 
val1 = input("Enter  patient  name :") 
print(val1) 
val2 = input("Enter your age : ") 
print(val2) 
val3 = input("Enter your symtoms :") 
print(val3) 
val4 = input("Enter your doctor : 1. john 2.cooper : ") 
print(val4) 

result=firebase.put('/hospital-management-syst-bd8b0/Patient',id,{'name':val1,'age':val2,'sym':val3,'doc':val4})
if val4 == '1' :

 result=firebase.put('/hospital-management-syst-bd8b0/Appointment/new/1',id,val1)

if val4 == '2' :
 result=firebase.put('/hospital-management-syst-bd8b0/Appointment/new/2',id,val1)
# result=firebase.post('/hospital-management-syst-bd8b0/Patient',data) ********pip install python-firebase******
print(result)
print("appointment successful")
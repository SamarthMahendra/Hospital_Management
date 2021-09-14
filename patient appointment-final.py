from firebase import firebase
firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
#collecting patient details
id = input("Enter  patient id : ") 
name = input("Enter  patient  name :") 
age = input("Enter your age : ") 
sym = input("Enter your symtoms :") 
dept = input("Enter your department : 1.Cardiology 2.Emergency department 3.General Physician 4.Gynecology 5.Nuerology 6.Oncology 7.Orthopaedics 8.Rheumatology: ") 
#getting the right doctor from the department
str='/hospital-management-syst-bd8b0/Department/'+ dept
val4 = firebase.get(str, 'doctor')
print("Patient Id :")
print(id) 
print("Patient Name :")
print(name) 
print("Patient age :")
print(age) 
print("Symtoms :")
print(sym)
print("Department :")
print(dept) 
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Assigned doctor :")
print(val4)
#writing to patient
result=firebase.put('/hospital-management-syst-bd8b0/Patient',id,{'name':name,'age':age,'sym':sym,'doc':val4})
#writing to appointment
str2='/hospital-management-syst-bd8b0/Appointment/new/'+val4
result=firebase.put(str2,id,name)
print(result)
print("appointment successful")
#12
# u need pip install python-firebase

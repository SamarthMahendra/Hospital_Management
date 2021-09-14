from firebase import firebase
firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
print("welcome doctor" )
val4 = input(" 1. john  2. cooper : ") 
if val4=='1' :
 print("Welcome doctor john")   
 result = firebase.get('/hospital-management-syst-bd8b0/Appointment/1', '')
if val4=='2' :
 print("Welcome doctor cooper")  
 result = firebase.get('/hospital-management-syst-bd8b0/Appointment/2', '')
print(result)

pname = input(" Name of the patient u want to treat :") 
pres = input(" Write prescription and medication :")

result2=firebase.put('/hospital-management-syst-bd8b0/Pres',pname,{'prescription':pres})




print(result2)
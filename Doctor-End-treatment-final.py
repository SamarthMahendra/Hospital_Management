#doctor-end interface
from firebase import firebase
firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
#collecting details
print("welcome doctor" )
val4 = input(" Enter Your Name Doctor ") 
#collecting the appointments under the doctor
str='/hospital-management-syst-bd8b0/Appointment/new/'+val4
result = firebase.get(str, '')
print(result)
#writing the prescription
pname = input(" Name of the patient u want to treat :") 
id = input(" Name of the patient id:") 
pres = input(" Write prescription and medication :")
#hello2

#writing the prescription to the database
result=firebase.put('/hospital-management-syst-bd8b0/Pres',pname,{'prescription':pres})
#writing the appointment to old records
str2='/hospital-management-syst-bd8b0/Appointment/old/'+val4
result2=firebase.put(str2,id,pname)
#deleting the appointment from new appointments
str3='/hospital-management-syst-bd8b0/Appointment/new/'+val4+'/'
result3=firebase.delete(str3,id)
print(result)
print(result2)
print(result3)
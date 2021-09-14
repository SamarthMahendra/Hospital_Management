 
from firebase import firebase
firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
dept = input("Enter  Department: ") 
doc = input("Enter doctor  name :") 
result2=firebase.put('/hospital-management-syst-bd8b0/Department',dept,{'doctor':doc})
print(result2)
#12
from firebase import firebase
firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
val = input(" Enter your name:") 
str1='/hospital-management-syst-bd8b0/Pres/'
str2=val
str3 =str1+str2;

result = firebase.get(str3, '')
print(result)
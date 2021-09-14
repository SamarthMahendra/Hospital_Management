from firebase import firebase

firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
id = input("Enter your id : ") 
print(id) 
val1 = input("Enter your name :") 
print(val1) 
val2 = input("Enter your age : ") 
print(val2) 
val3 = input("Enter your symtoms :") 
print(val3) 
val4 = input("Enter your doctor : 1. john 2.cooper : ") 
print(val4) 

#data={
  #   id: {
    
   #          'Name':val1,
   #          'age':val2,
   #          'sym':val3,
   #          'doc':val4
   #  }

#}
result=firebase.put('/hospital-management-syst-bd8b0/Patient',id,{'name':val1,'age':val2,'sym':val3,'doc':val4})
result=firebase.put('/hospital-management-syst-bd8b0/App',val4,{id:val1})
# result=firebase.post('/hospital-management-syst-bd8b0/Patient',data) *********pip install python-firebase********
print(result)
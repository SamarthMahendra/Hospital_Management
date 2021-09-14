from firebase import firebase
firebase = firebase.FirebaseApplication("https://hospital-management-syst-bd8b0.firebaseio.com/" ,None)
firebase.put('/hospital-management-syst-bd8b0/Patient')
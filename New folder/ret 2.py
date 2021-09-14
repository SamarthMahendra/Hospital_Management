from firebase_admin import db
ref = db.reference('patient')
print(ref.get())
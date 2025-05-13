import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendance-fddb7-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "099900":
        {
            "name": "Will Smith",
            "major": "Acting",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "C",
            "year": 4,
            "last_attendance_time": "2025-05-12 00:54:34"

        },
    "221105":
        {
            "name": "Harshit Nagar",
            "major": "B.Tech",
            "starting_year": 2023,
            "total_attendance": 8,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2025-05-12 00:54:34"

        },
    "264045":
        {
            "name": "Rohit Sharma",
            "major": "Cricketer",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2025-05-12 00:54:34"

        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "CEO",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2025-05-12 00:54:34"

        },
    "030302":
        {
            "name": "Swati N",
            "major": "Graphics",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2025-05-12 00:54:34"

        },
    "061204":
        {
            "name": "Tanisha",
            "major": "Designer",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2025-05-12 00:54:34"

        }
}

for key,value in data.items():
    ref.child(key).set(value)
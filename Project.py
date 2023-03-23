import mysql.connector
import os

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="soal"
)

pilihan_user = int(input("Pilih menu : "))
if (pilihan_user == 1):
    # menu_profile()
    print(".")
elif (pilihan_user == 2):
    # menu_soal()
    print(".")
elif (pilihan_user == 3):
    # menu_rangking()
    print(".")
else:
    print("Terima Kasih :)")
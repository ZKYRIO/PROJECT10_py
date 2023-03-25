import mysql.connector
import os

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="soal"
)

def menu_utama():
    os.system('cls')
    print("""
        1. Profile
        2. Soal
        3. Rangking
        4. Keluar
    """)
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
    elif (pilihan_user == 4):
        print("Terima Kasih :)")
    else:
        print("Input anda salah")
        menu_utama()
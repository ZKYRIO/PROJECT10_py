import mysql.connector
import os

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kids_math"
) 
cursor = database.cursor()

def menu_soal():

    def soal_penjumlahan():
        d_soal = []  # untuk menyimpan sementara soal dari bank soal database
        d_No = []  # untuk menyimpan no soal
        d_jawabUser = []  # untuk menyimpan sementara jawaban user untuk di koreksi
        d_benar = []  # untuk menyimpan banyaknya soal yang benar
        d_salah = []  # untuk menyimpan banyaknya soal yang salah

        def update_score():
            score = len(d_benar)*10

            # menampilkan data id_user dan username
            sql_show = 'SELECT id_user,username,nama FROM data'
            cursor.execute(sql_show)
            data = cursor.fetchall()
            print("id | username | nama")
            for datas in data:
                print(datas)

            id_user = int(input("Masukkan ID User Anda : "))
            # kolom nilai (n_...) disesuaikan dengan bab nya
            sql_update = 'UPDATE data SET nilai_pertambahan=%s WHERE id_user =%s '
            val_update = (score, id_user)
            cursor.execute(sql_update, val_update)
            database.commit()
            print("Nilai berhasil tersimpan ✅")
            os.system('cls')

        def koreksi_soal():
            y = 0
            while y < 10:  # ganti sesuai jumlah soal
                sql_koreksi = 'SELECT * FROM soal_tambah WHERE no =%s AND jawab =%s'
                values_koreksi = (d_No[y], d_jawabUser[y])
                cursor.execute(sql_koreksi, values_koreksi)
                cek = cursor.fetchone()
                if (cek != None):
                    benar = 0
                    benar += 1
                    d_benar.append(benar)
                else:
                    salah = 0
                    salah += 1
                    d_salah.append(salah)
                y += 1
            update_score()

        def tampil_score():
            score = len(d_benar)*10
            benar = len(d_benar)
            salah = len(d_salah)
            print("="*40)
            print("Soal Terjawab benar = {}".format(benar))
            print("Soal Terjawab salah = {}".format(salah))
            print("="*40)
            print("Score akhir yang kamu peroleh".center(10))
            print('{}'.format(score).center(40))

        def jawab_soal(x, y):
            os.system('cls')
            pilihan_user = int(input("{}) {} ".format(x, y)))
            d_jawabUser.append(pilihan_user)
            os.system('cls')

        def tampil_soal():

            # perintah sql untuk menampillkan soal dari database
            sql = 'SELECT soal FROM soal_tambah'
            cursor.execute(sql)

            # menampilkan soal dari database
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                hasil = cursor.fetchone()
                d_soal.append(hasil)
                # print(d_soal)
                x += 1

            # menampilkan No soal
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                no_soal = x+1
                d_No.append(str(no_soal))
                x += 1

            # menampilkan soal untuk user
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                for no, data in zip(d_No[x], d_soal[x]):
                    jawab_soal(no, data)
                x += 1

        tampil_soal()
        koreksi_soal()
        tampil_score()

    def soal_pengurangan():
        d_soal = []  # untuk menyimpan sementara soal dari bank soal database
        d_No = []  # untuk menyimpan no soal
        d_jawabUser = []  # untuk menyimpan sementara jawaban user untuk di koreksi
        d_benar = []  # untuk menyimpan banyaknya soal yang benar
        d_salah = []  # untuk menyimpan banyaknya soal yang salah

        def update_score():
            score = len(d_benar)*10

            # menampilkan data id_user dan username
            sql_show = 'SELECT id_user,username,nama FROM data'
            cursor.execute(sql_show)
            data = cursor.fetchall()
            print("id | username | nama")
            for datas in data:
                print(datas)

            id_user = int(input("Masukkan ID User Anda : "))
            # kolom nilai (n_...) disesuaikan dengan bab nya
            sql_update = 'UPDATE data SET nilai_pengurangan=%s WHERE id_user =%s '
            val_update = (score, id_user)
            cursor.execute(sql_update, val_update)
            database.commit()
            print("Nilai berhasil tersimpan ✅")
            os.system('cls')

        def koreksi_soal():
            y = 0
            while y < 10:  # ganti sesuai jumlah soal
                sql_koreksi = 'SELECT * FROM soal_kurang WHERE no =%s AND jawab =%s'
                values_koreksi = (d_No[y], d_jawabUser[y])
                cursor.execute(sql_koreksi, values_koreksi)
                cek = cursor.fetchone()
                if (cek != None):
                    benar = 0
                    benar += 1
                    d_benar.append(benar)
                else:
                    salah = 0
                    salah += 1
                    d_salah.append(salah)
                y += 1
            update_score()

        def tampil_score():
            score = len(d_benar)*10
            benar = len(d_benar)
            salah = len(d_salah)
            print("="*40)
            print("Soal Terjawab benar = {}".format(benar))
            print("Soal Terjawab salah = {}".format(salah))
            print("="*40)
            print("Score akhir yang kamu peroleh".center(10))
            print('{}'.format(score).center(40))

        def jawab_soal(x, y):
            os.system('cls')
            pilihan_user = int(input("{}) {} ".format(x, y)))
            d_jawabUser.append(pilihan_user)
            os.system('cls')

        def tampil_soal():

            # perintah sql untuk menampillkan soal dari database
            sql = 'SELECT soal FROM soal_kurang'
            cursor.execute(sql)

            # menampilkan soal dari database
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                hasil = cursor.fetchone()
                d_soal.append(hasil)
                # print(d_soal)
                x += 1

            # menampilkan No soal
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                no_soal = x+1
                d_No.append(str(no_soal))
                x += 1

            # menampilkan soal untuk user
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                for no, data in zip(d_No[x], d_soal[x]):
                    jawab_soal(no, data)
                x += 1

        tampil_soal()
        koreksi_soal()
        tampil_score()

    def soal_perkalian():
        d_soal = []  # untuk menyimpan sementara soal dari bank soal database
        d_No = []  # untuk menyimpan no soal
        d_jawabUser = []  # untuk menyimpan sementara jawaban user untuk di koreksi
        d_benar = []  # untuk menyimpan banyaknya soal yang benar
        d_salah = []  # untuk menyimpan banyaknya soal yang salah

        def update_score():
            score = len(d_benar)*10

            # menampilkan data id_user dan username
            sql_show = 'SELECT id_user,username,nama FROM data'
            cursor.execute(sql_show)
            data = cursor.fetchall()
            print("id | username | nama")
            for datas in data:
                print(datas)

            id_user = int(input("Masukkan ID User Anda : "))
            # kolom nilai (n_...) disesuaikan dengan bab nya
            sql_update = 'UPDATE data SET nilai_perkalian=%s WHERE id_user =%s '
            val_update = (score, id_user)
            cursor.execute(sql_update, val_update)
            database.commit()
            print("Nilai berhasil tersimpan ✅")
            os.system('cls')

        def koreksi_soal():
            y = 0
            while y < 10:  # ganti sesuai jumlah soal
                sql_koreksi = 'SELECT * FROM soal_kali WHERE no =%s AND jawab =%s'
                values_koreksi = (d_No[y], d_jawabUser[y])
                cursor.execute(sql_koreksi, values_koreksi)
                cek = cursor.fetchone()
                if (cek != None):
                    benar = 0
                    benar += 1
                    d_benar.append(benar)
                else:
                    salah = 0
                    salah += 1
                    d_salah.append(salah)
                y += 1
            update_score()

        def tampil_score():
            score = len(d_benar)*10
            benar = len(d_benar)
            salah = len(d_salah)
            print("="*40)
            print("Soal Terjawab benar = {}".format(benar))
            print("Soal Terjawab salah = {}".format(salah))
            print("="*40)
            print("Score akhir yang kamu peroleh".center(10))
            print('{}'.format(score).center(40))

        def jawab_soal(x, y):
            os.system('cls')
            pilihan_user = int(input("{}) {} ".format(x, y)))
            d_jawabUser.append(pilihan_user)
            os.system('cls')

        def tampil_soal():

            # perintah sql untuk menampillkan soal dari database
            sql = 'SELECT soal FROM soal_kali'
            cursor.execute(sql)

            # menampilkan soal dari database
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                hasil = cursor.fetchone()
                d_soal.append(hasil)
                # print(d_soal)
                x += 1

            # menampilkan No soal
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                no_soal = x+1
                d_No.append(str(no_soal))
                x += 1

            # menampilkan soal untuk user
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                for no, data in zip(d_No[x], d_soal[x]):
                    jawab_soal(no, data)
                x += 1

        tampil_soal()
        koreksi_soal()
        tampil_score()

    def soal_pembagian():
        d_soal = []  # untuk menyimpan sementara soal dari bank soal database
        d_No = []  # untuk menyimpan no soal
        d_jawabUser = []  # untuk menyimpan sementara jawaban user untuk di koreksi
        d_benar = []  # untuk menyimpan banyaknya soal yang benar
        d_salah = []  # untuk menyimpan banyaknya soal yang salah

        def update_score():
            score = len(d_benar)*10

            # menampilkan data id_user dan username
            sql_show = 'SELECT id_user,username,nama FROM data'
            cursor.execute(sql_show)
            data = cursor.fetchall()
            print("id | username | nama")
            for datas in data:
                print(datas)

            id_user = int(input("Masukkan ID User Anda : "))
            # kolom nilai (n_...) disesuaikan dengan bab nya
            sql_update = 'UPDATE data SET nilai_pembagian=%s WHERE id_user =%s '
            val_update = (score, id_user)
            cursor.execute(sql_update, val_update)
            database.commit()
            print("Nilai berhasil tersimpan ✅")
            os.system('cls')

        def koreksi_soal():
            y = 0
            while y < 10:  # ganti sesuai jumlah soal
                sql_koreksi = 'SELECT * FROM soal_bagi WHERE no =%s AND jawab =%s'
                values_koreksi = (d_No[y], d_jawabUser[y])
                cursor.execute(sql_koreksi, values_koreksi)
                cek = cursor.fetchone()
                if (cek != None):
                    benar = 0
                    benar += 1
                    d_benar.append(benar)
                else:
                    salah = 0
                    salah += 1
                    d_salah.append(salah)
                y += 1
            update_score()

        def tampil_score():
            score = len(d_benar)*10
            benar = len(d_benar)
            salah = len(d_salah)
            print("="*40)
            print("Soal Terjawab benar = {}".format(benar))
            print("Soal Terjawab salah = {}".format(salah))
            print("="*40)
            print("Score akhir yang kamu peroleh".center(10))
            print('{}'.format(score).center(40))

        def jawab_soal(x, y):
            os.system('cls')
            pilihan_user = int(input("{}) {} ".format(x, y)))
            d_jawabUser.append(pilihan_user)
            os.system('cls')

        def tampil_soal():

            # perintah sql untuk menampillkan soal dari database
            sql = 'SELECT soal FROM soal_bagi'
            cursor.execute(sql)

            # menampilkan soal dari database
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                hasil = cursor.fetchone()
                d_soal.append(hasil)
                # print(d_soal)
                x += 1

            # menampilkan No soal
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                no_soal = x+1
                d_No.append(str(no_soal))
                x += 1

            # menampilkan soal untuk user
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                for no, data in zip(d_No[x], d_soal[x]):
                    jawab_soal(no, data)
                x += 1

        tampil_soal()
        koreksi_soal()
        tampil_score()

    print("""
        1. Penjumlahan  (+)
        2. Pengurangan  (-)
        3. Perkalian    (×)
        4. Pembagian    (÷)
        5. Kembali
    """)
    pilihan_user = int(input("Pilih Menu : "))
    if (pilihan_user == 1 ):
        soal_penjumlahan()
    elif (pilihan_user == 2 ):
        soal_pengurangan()
    elif (pilihan_user == 3 ):
        soal_perkalian()
    elif (pilihan_user == 4 ):
        soal_pembagian()
    elif (pilihan_user == 5 ):
        menu_utama()
    else:
        print("Inputan anda salah")
        menu_soal()

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
        menu_soal()
    elif (pilihan_user == 3):
        # menu_rangking()
        print(".")
    elif (pilihan_user == 4):
        print("Terima Kasih :)")
    else:
        print("Input anda salah")
        menu_utama()

menu_utama()
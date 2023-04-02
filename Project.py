import mysql.connector
import os

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kids_math"
) 
cursor = database.cursor()

def menu_profile():
    os.system('cls')
    def search_data():
        os.system('cls')
        print("="*40)
        print("=", "CARI DATA".center(36), "=")
        print("="*40)
        print(" ")
        key = input("Kata kunci nama depan anda : ")
        sql_search = "SELECT id_user,username,nama,gender,jenjang FROM data WHERE nama LIKE %s"
        val_search = ("{}%".format(key), )
        cursor.execute(sql_search, val_search)
        show_data = cursor.fetchall()

        print(" "*20)
        if cursor.rowcount < 0:
            print("Data tidak ditemukan")
        else:
            for data in show_data:
                print(data)
        print(" "*20)

        confirm = input("Tekan[enter] untuk kembali ")
        os.system('cls')
        menu()

    def update_data():
        # header
        os.system('cls')
        print("="*40)
        print("=", "UPDATE DATA".center(36), "=")
        print("="*40)
        print(" ")

        # perintah sql untuk menampilkan id_user, username, nama, gender, jenjang
        sql_show = 'SELECT id_user,username, nama, gender, jenjang FROM data'
        cursor.execute(sql_show)
        show_data = cursor.fetchall()
        for data in show_data:
            id_     = data[0]
            usn     = data[1]
            name    = data[2]
            sex     = data[3]
            sch     = data[4]
            print(" ")
            print("[    Id_User     |    Username    |    Name    |    Gender   |    Jenjang   |]")
            print("|      {}                {}            {}           {}            {}         |")
            print(" ")

        # inputan user untuk data update
        id_user = int(input("Masukkan id_user anda : "))
        usn = input("Masukkan username baru anda : ")
        nama = input("Masukkan nama baru anda : ")
        gender = input("Masukkan jenis kelamin anda (L / P) : ")
        school = input("Masukkan jenjang sekolah anda (TK / SD) : ")

        # perintah sql untuk mengupdate data
        sql_update = 'UPDATE data SET username=%s , nama=%s, gender=%s, jenjang=%s WHERE id_user=%s'
        val_update = (usn, nama, gender, school, id_user)
        cursor.execute(sql_update, val_update)
        database.commit()
        os.system('cls')
        print("="*40)
        print("=", "Data berhasil di update ✅".center(35), "=")
        print("="*40)
        print(" ")
        confirm = input("Tekan[enter] untuk kembali")
        os.system('cls')
        menu()

    def delete_data():

        # perintah sql untuk menampilkan id_user, username, nama, gender, jenjang
        sql_show = 'SELECT id_user,username, nama, gender, jenjang FROM data'
        cursor.execute(sql_show)
        show_data = cursor.fetchall()
        for data in show_data:
            id_     = data[0]
            usn     = data[1]
            name    = data[2]
            sex     = data[3]
            sch     = data[4]
            print(" ")
            print("[    Id_User     |    Username    |    Name    |    Gender   |    Jenjang   |]")
            print("|      {}                {}            {}           {}            {}         |")
            print(" ")

        # perintah sql untuk menghapus data
        id_user = int(input("Masukkan id user anda : "))
        sql_del = 'DELETE FROM data WHERE id_user=%s'
        val_del = (id_user, )
        cursor.execute(sql_del,val_del)
        
        # perintah sql untuk mengurutkan id_user secara otomatis
        sql_urut = 'ALTER TABLE data DROP id_user'
        cursor.execute(sql_urut)
        sql_urut2 = 'ALTER TABLE data ADD id_user INT(11) PRIMARY KEY AUTO_INCREMENT FIRST, ADD KEY(id_user)'
        cursor.execute(sql_urut2)
        database.commit()

        os.system('cls')
        print("="*40)
        print("=", "Data berhasil di hapus ✅".center(35), "=")
        print("="*40)
        print(" ")
        confirm = input("Tekan[enter] untuk kembali")
        os.system('cls')
        menu()

    def Daftar():
        # header
        os.system('cls')
        print("="*40)
        print("=", "Daftar / Login".center(36), "=")
        print("="*40)
        print(" ")

        username = str.capitalize(input("Masukkan Username Anda : "))
        nama = str.capitalize(input("Masukkan Nama Anda : "))
        sex = str.capitalize(input("(Laki - laki) / (Perempuan) : "))
        school = str.capitalize(input("Jenjang Sekolah (TK / SD) : "))
        
        # menyimpan sign up user ke database
        def confirm():
            confirm = input("Apakah anda yakin (iya / tidak) : ")
            if (confirm == "tidak" or confirm == "TIDAK" or confirm == "Tidak"):
                Daftar()
            elif (confirm == "iya" or confirm == "IYA" or confirm == "Iya"):
                # perintah sql untuk menambahkan data user ke dalam database
                sql_insert = 'INSERT INTO data (username,nama,gender,jenjang) VALUES(%s,%s,%s,%s)'
                val_insert = (username, nama, sex, school)
                cursor.execute(sql_insert, val_insert)
                database.commit()
            else :
                print("Inputan anda salah, silahkan input kembali")
                confirm()

            os.system('cls')
            print("="*40)
            print("=", "Data berhasil tersimpan ✅".center(35), "=")
            print("="*40)
            print(" ")
            confirm = input("Tekan[enter] untuk kembali")
            os.system('cls')
            menu()
        confirm()

    def Data_diri():
        # header
        os.system('cls')
        print("="*40)
        print("=", "Profile".center(36), "=")
        print("="*40)
        print("""
        1. Search
        2. Update
        3. Delete
        4. Kembali
        """)
        pilihan_user = int(input("Pilih : "))
        if (pilihan_user == 1):
            search_data()
        elif (pilihan_user == 2):
            update_data()
        elif (pilihan_user == 3):
            delete_data()
        elif (pilihan_user == 4):
            menu()
        else:
            print("Inputan anda salah")
            Data_diri()

    def menu():
        os.system('cls')
        # header
        print("="*40)
        print("=", "Menu Profile".center(36), "=")
        print("="*40)
        print("""
        1. Daftar
        2. Data diri
        3. Kembali
        """)
        pilihan_user = int(input("Pilih menu : "))
        if (pilihan_user == 1):
            # menu_daftar()
            Daftar()
        elif (pilihan_user == 2):
            Data_diri()
        elif (pilihan_user == 3):
            # menu utama
            menu_utama()
        else:
            print("Inputan anda salah")
            menu()
    menu()

def menu_rangking():
    os.system('cls')
    def show_data_tambah():
        # perintah sql untuk menampilkan data id_user,username,dan nilai
        # kolom database harus bernama sesuai bab
        sql = 'SELECT id_user,username,nama,nilai_pertambahan FROM data'
        cursor.execute(sql)
        score = cursor.fetchall()

        # untuk mengcek apakah ada data atau tidak
        if cursor.rowcount < 0:
            print("Data Tidak Ada")
        else:
            for nilai in score:
                id_user = nilai[0]
                usn     = nilai[1]
                nama    = nilai[2]
                nil     = nilai[3]
                print(" ")
                print("[  Id User  |    Username    |   Nama   |    Nilai Penjumlahan   ]")
                print("|    {}          {}              {}                  {}          |")
                print(" ")


        confirm = input("Press [enter] untuk kembali ")
        os.system('cls')
        menu()

    def show_data_kurang():
        # perintah sql untuk menampilkan data id_user,username,dan nilai
        # kolom database harus bernama sesuai bab
        sql = 'SELECT id_user,username,nama,nilai_pengurangan FROM data'
        cursor.execute(sql)
        score = cursor.fetchall()

        # untuk mengcek apakah ada data atau tidak
        if cursor.rowcount < 0:
            print("Data Tidak Ada")
        else:
            for nilai in score:
                id_user = nilai[0]
                usn = nilai[1]
                nama = nilai[2]
                nil = nilai[3]
                print(" ")
                print(
                    "[  Id User  |    Username    |   Nama   |    Nilai Pengurangan   ]")
                print(
                    "|    {}          {}              {}                  {}          |")
                print(" ")

        confirm = input("Press [enter] untuk kembali ")
        os.system('cls')
        menu()

    def show_data_kali():
        # perintah sql untuk menampilkan data id_user,username,dan nilai
        # kolom database harus bernama sesuai bab
        sql = 'SELECT id_user,username,nama,nilai_perkalian FROM data'
        cursor.execute(sql)
        score = cursor.fetchall()

        # untuk mengcek apakah ada data atau tidak
        if cursor.rowcount < 0:
            print("Data Tidak Ada")
        else:
            for nilai in score:
                id_user = nilai[0]
                usn = nilai[1]
                nama = nilai[2]
                nil = nilai[3]
                print(" ")
                print(
                    "[  Id User  |    Username    |   Nama   |    Nilai Penjumlahan   ]")
                print(
                    "|    {}          {}              {}                  {}          |")
                print(" ")

        confirm = input("Press [enter] untuk kembali ")
        os.system('cls')
        menu()

    def show_data_bagi():
        # perintah sql untuk menampilkan data id_user,username,dan nilai
        # kolom database harus bernama sesuai bab
        sql = 'SELECT id_user,username,nama,nilai_pembagian FROM data'
        cursor.execute(sql)
        score = cursor.fetchall()

        # untuk mengcek apakah ada data atau tidak
        if cursor.rowcount < 0:
            print("Data Tidak Ada")
        else:
            for nilai in score:
                id_user = nilai[0]
                usn = nilai[1]
                nama = nilai[2]
                nil = nilai[3]
                print(" ")
                print(
                    "[  Id User  |    Username    |   Nama   |    Nilai Penjumlahan   ]")
                print(
                    "|    {}          {}              {}                  {}          |")
                print(" ")

        confirm = input("Press [enter] untuk kembali ")
        os.system('cls')
        menu()

    def menu():
        os.system('cls')
        print("""
            1.Pertambahan
            2.Pengurangan
            3.Perkalian
            4.Pembagian
            5.Kembali
        """)
        pilihan_user = int(input("Pilih Menu : "))
        if (pilihan_user == 1):
            show_data_tambah()
        elif (pilihan_user == 2):
            show_data_kurang()
        elif (pilihan_user == 3):
            show_data_kali()
        elif (pilihan_user == 4):
            show_data_bagi()
        elif (pilihan_user == 5):
            menu_utama()
        else:
            print("Inputan anda salah")
            confirm = input("Tekan [enter] untuk melanjutkan ")
            os.system('cls')
            rangking()
    menu()

def menu_soal():
    os.system('cls')
    def soal_penjumlahan():
        d_soal = []  # untuk menyimpan sementara soal dari bank soal di database
        d_No = []  # untuk menyimpan no soal
        d_jawabUser = []  # untuk menyimpan sementara jawaban user dan untuk di koreksi
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
        menu_profile()
    elif (pilihan_user == 2):
        menu_soal()
    elif (pilihan_user == 3):
        menu_rangking()
    elif (pilihan_user == 4):
        os.system('cls')
        print("Terima Kasih :)")
    else:
        print("Input anda salah")
        menu_utama()

menu_utama()
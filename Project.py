import mysql.connector
import os

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kids_math"
)
cursor = database.cursor()

def alert():
    os.system('cls')
    print("—"*45)
    print("|               !! ALERT !!                 |")
    print("|            Input anda salah               |")
    print("—"*45)
    confirm = input("| Tekan [enter] untuk kembali ")

def menu_profile():
    os.system('cls')
    def Daftar():
        # header
        os.system('cls')
        print("—"*45)
        print("╎              DAFTAR / LOGIN               ╎")
        print("—"*45)
        username = input("| Input Username Anda : ")
        nama = str.capitalize(input("| Input Nama Anda : "))
        sex = str.capitalize(input("| Input Gender Anda (Pria / Wanita) : "))
        school = str.upper(input("| Input Jenjang Sekolah ('SD + KELAS' --> SD 5) : "))
        print("—"*45)

        # menyimpan sign up user ke database
        def confirm():
            confirm = input("| Apakah anda yakin (iya / tidak) : ")
            if (confirm == "tidak" or confirm == "TIDAK" or confirm == "Tidak"):
                Daftar()
            elif (confirm == "iya" or confirm == "IYA" or confirm == "Iya"):
                # perintah sql untuk menambahkan data user ke dalam database
                sql_insert = 'INSERT INTO data (username,nama,gender,jenjang) VALUES(%s,%s,%s,%s)'
                val_insert = (username, nama, sex, school)
                cursor.execute(sql_insert, val_insert)
                database.commit()
            else:
                print("| Inputan anda salah, silahkan input kembali |")
                confirm()

            os.system('cls')
            print("="*45)
            print("|        Data berhasil tersimpan ✅         |")
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            os.system('cls')
            menu()
        confirm()

    def Data_diri():
        def search_data():
            os.system('cls')
            print("—"*45)
            print("╎               SEARCH DATA                 ╎")
            print("—"*45)
            key = input("| Kata kunci nama depan anda : ")
            sql_search = "SELECT id_user,username,nama,gender,jenjang FROM data WHERE nama LIKE %s"
            val_search = ("{}%".format(key), )
            cursor.execute(sql_search, val_search)
            show_data = cursor.fetchall()

            if (show_data == []) :
                os.system('cls')
                print("—"*45)
                print("|                                           |")
                print("|            Data tidak ditemukan           |")
                print("|                                           |")
                print("—"*45)
                confirm = input("| Tekan[enter] untuk kembali ")
                Data_diri()
            else:
                print("—"*45)
                for data in show_data:
                    id_ = data[0]
                    usn = data[1]
                    name = data[2]
                    sex = data[3]
                    sch = data[4]
                    print(" ")
                    print("| Id User    = {}".format(id_))
                    print("| Username   = {}".format(usn))
                    print("| Nama       = {}".format(name))
                    print("| Gender     = {}".format(sex))
                    print("| Jenjang    = {}".format(sch))
                    print(" ")
            print("—"*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            os.system('cls')
            Data_diri()

        def edit_data():
            # header
            os.system('cls')
            print("—"*45)
            print("╎                EDIT DATA                  ╎")
            print("—"*45)

            # perintah sql untuk menampilkan id_user, username, nama, gender, jenjang
            sql_show = 'SELECT id_user,username, nama, gender, jenjang FROM data'
            cursor.execute(sql_show)
            show_data = cursor.fetchall()

            if (show_data == []):
                print("|                                           |")
                print("|              Tidak Ada Data               |")
                print("|                                           |")
                print("—"*45)
                confirm = input("| Tekan [enter] untuk kembali ")
                os.system('cls')
                Data_diri()
            else :
                for data in show_data:
                    id_ = data[0]
                    usn = data[1]
                    name = data[2]
                    sex = data[3]
                    sch = data[4]
                    sch = data[4]
                    print(" ")
                    print("| Id User    = {}".format(id_))
                    print("| Username   = {}".format(usn))
                    print("| Nama       = {}".format(name))
                    print("| Gender     = {}".format(sex))
                    print("| Jenjang    = {}".format(sch))
                    print(" ")

                # inputan user untuk data update
                print("—"*45)
                id_user = int(input("| Masukkan id_user anda : "))
                usn = input("| Masukkan username baru anda : ")
                nama = input("| Masukkan nama baru anda : ")
                gender = input("| Masukkan jenis kelamin anda (Pria / Wanita) : ")
                school = input("| Masukkan jenjang sekolah anda (TK / SD) : ")

                if (usn == "" or nama == "" or gender == ""):
                    os.system('cls')
                    print("—"*45)
                    print("|               !! ALERT !!                 |")
                    print("|           Data Tidak Lengkap              |")
                    print("—"*45)
                    confirm = input("| Kembali mengedit (y / n) : ")
                    if (confirm == "y" or confirm == "Y"):
                        edit_data()
                    else:
                        Data_diri()

                else:
                    # perintah sql untuk mengupdate data
                    sql_update = 'UPDATE data SET username=%s , nama=%s, gender=%s, jenjang=%s WHERE id_user=%s'
                    val_update = (usn, nama, gender, school, id_user)
                    cursor.execute(sql_update, val_update)
                    database.commit()
                    os.system('cls')
                    print("="*45)
                    print("|         Data berhasil diupdate ✅         |")
                    print("="*45)
                    confirm = input("| Tekan[enter] untuk kembali ")
                    os.system('cls')
                    menu()

        def delete_data():
            os.system('cls')
            print("—"*45)
            print("╎               DELETE DATA                 ╎")
            print("—"*45)
            # perintah sql untuk menampilkan id_user, username, nama, gender, jenjang
            sql_show = 'SELECT id_user,username, nama, gender, jenjang FROM data'
            cursor.execute(sql_show)
            show_data = cursor.fetchall()

            if (show_data == []):
                print("|                                           |")
                print("|              Tidak Ada Data               |")
                print("|                                           |")
                print("—"*45)
                confirm = input("| Tekan [enter] untuk kembali ")
                os.system('cls')
                Data_diri()
            
            else :

                for data in show_data:
                    id_ = data[0]
                    usn = data[1]
                    name = data[2]
                    sex = data[3]
                    sch = data[4]
                    print(" ")
                    print("| Id User    = {}".format(id_))
                    print("| Username   = {}".format(usn))
                    print("| Nama       = {}".format(name))
                    print("| Gender     = {}".format(sex))
                    print("| Jenjang    = {}".format(sch))
                    print(" ")

                print("—"*45)
                id_user = int(input("| Masukkan id user anda : "))
                sql_del = 'DELETE FROM data WHERE id_user=%s'
                val_del = (id_user, )
                cursor.execute(sql_del, val_del)

                # perintah sql untuk mengurutkan id_user secara otomatis
                sql_urut = 'ALTER TABLE data DROP id_user'
                cursor.execute(sql_urut)
                sql_urut2 = 'ALTER TABLE data ADD id_user INT(11) PRIMARY KEY AUTO_INCREMENT FIRST, ADD KEY(id_user)'
                cursor.execute(sql_urut2)
                database.commit()

                os.system('cls')
                print("="*45)
                print("|        Data berhasil dihapus ✅           |")
                print("="*45)
                confirm = input("| Tekan[enter] untuk kembali ")
                os.system('cls')
                menu()

        # header
        os.system('cls')
        print("—"*50)
        print("╎                   DATA DIRI                    ╎")
        print("—"*50)
        print("|                                                |")
        print("|    1.Search | 2.Edit | 3.Delete | 4.Kembali    |")
        print("|                                                |")
        print("—"*50)
        pilihan_user = int(input("| Pilih ( 1 / 2 / 3 / 4 ) : "))
        if (pilihan_user == 1):
            search_data()
        elif (pilihan_user == 2):
            edit_data()
        elif (pilihan_user == 3):
            delete_data()
        elif (pilihan_user == 4):
            menu()
        else:
            os.system('cls')
            alert()
            Data_diri()

    def menu():
        os.system('cls')
        # header
        print("—"*45)
        print("╎               MENU PROFILE                ╎")
        print("—"*45)
        print("|                                           |")
        print("|    1. Daftar | 2.Data Diri | 3.Kembali    |")
        print("|                                           |")
        print("—"*45)
        pilihan_user = int(input("| Pilih menu ( 1 / 2 / 3 ) : "))
        if (pilihan_user == 1):
            # menu_daftar()
            Daftar()
        elif (pilihan_user == 2):
            Data_diri()
        elif (pilihan_user == 3):
            # menu utama
            menu_utama()
        else:
            os.system('cls')
            alert()
            menu()
    menu()

def menu_rangking():
    os.system('cls')

    def show_data_tambah():
        os.system('cls')
        print("—"*45)
        print("╎           RANGKING PENJUMLAHAN            ╎")
        print("—"*45)
        # perintah sql untuk menampilkan data id_user,username,dan nilai
        # kolom database harus bernama sesuai bab
        sql = 'SELECT id_user,username,nama,nilai_pertambahan FROM data ORDER BY nilai_pertambahan DESC'
        cursor.execute(sql)
        show_data = cursor.fetchall()

        # untuk mengcek apakah ada data atau tidak
        if (show_data == []):
            print("|                                           |")
            print("|              Tidak Ada Data               |")
            print("|                                           |")
        else:
            for data in show_data:
                id_ = data[0]
                usn = data[1]
                name = data[2]
                nilai = data[3]
                print(" ")
                print("| Id User    = {}".format(id_))
                print("| Username   = {}".format(usn))
                print("| Nama       = {}".format(name))
                print("| Nilai (+)  = {}".format(nilai))
                print(" ")

        print("—"*45)
        confirm = input("| Tekan [enter] untuk kembali ")
        os.system('cls')
        menu()

    def show_data_kurang():
        os.system('cls')
        print("—"*45)
        print("╎           RANGKING PENGURANGAN            ╎")
        print("—"*45)
        # perintah sql untuk menampilkan data id_user,username,dan nilai
        # kolom database harus bernama sesuai bab
        sql = 'SELECT id_user,username,nama,nilai_pengurangan FROM data ORDER BY nilai_pengurangan DESC'
        cursor.execute(sql)
        show_data = cursor.fetchall()

        # untuk mengcek apakah ada data atau tidak
        if (show_data == []):
            print("|                                           |")
            print("|              Tidak Ada Data               |")
            print("|                                           |")
        else:
            for data in show_data:
                id_ = data[0]
                usn = data[1]
                name = data[2]
                nilai = data[3]
                print(" ")
                print("| Id User    = {}".format(id_))
                print("| Username   = {}".format(usn))
                print("| Nama       = {}".format(name))
                print("| Nilai (-)  = {}".format(nilai))
                print(" ")

        print("—"*45)
        confirm = input("| Tekan [enter] untuk kembali ")
        os.system('cls')
        menu()

    def show_data_kali():
        os.system('cls')
        print("—"*45)
        print("╎            RANGKING PERKALIAN             ╎")
        print("—"*45)
        # perintah sql untuk menampilkan data id_user,username,dan nilai
        # kolom database harus bernama sesuai bab
        sql = 'SELECT id_user,username,nama,nilai_perkalian FROM data ORDER BY nilai_perkalian DESC'
        cursor.execute(sql)
        show_data = cursor.fetchall()

        # untuk mengcek apakah ada data atau tidak
        if (show_data == []):
            print("|                                           |")
            print("|              Tidak Ada Data               |")
            print("|                                           |")
        else:
            for data in show_data:
                id_ = data[0]
                usn = data[1]
                name = data[2]
                nilai = data[3]
                print(" ")
                print("| Id User    = {}".format(id_))
                print("| Username   = {}".format(usn))
                print("| Nama       = {}".format(name))
                print("| Nilai (×)  = {}".format(nilai))
                print(" ")

        print("—"*45)
        confirm = input("| Tekan [enter] untuk kembali ")
        os.system('cls')
        menu()

    def show_data_bagi():
        os.system('cls')
        print("—"*45)
        print("╎            RANGKING PEMBAGIAN             ╎")
        print("—"*45)
        # perintah sql untuk menampilkan data id_user,username,dan nilai
        # kolom database harus bernama sesuai bab
        sql = 'SELECT id_user,username,nama,nilai_pembagian FROM data ORDER BY nilai_pembagian DESC'
        cursor.execute(sql)
        show_data = cursor.fetchall()

        # untuk mengcek apakah ada data atau tidak
        if (show_data == []):
            print("|                                           |")
            print("|              Tidak Ada Data               |")
            print("|                                           |")
        else:
            for data in show_data:
                id_ = data[0]
                usn = data[1]
                name = data[2]
                nilai = data[3]
                print(" ")
                print("| Id User    = {}".format(id_))
                print("| Username   = {}".format(usn))
                print("| Nama       = {}".format(name))
                print("| Nilai (÷)  = {}".format(nilai))
                print(" ")

        print("—"*45)
        confirm = input("| Tekan [enter] untuk kembali ")
        os.system('cls')
        menu()

    def menu():
        os.system('cls')
        print("—"*45)
        print("╎               MENU RANGKING               ╎")
        print("—"*45)
        print("|                                           |")
        print("|             1.Penjumlahan  (+)            |")
        print("|             2.Pengurangan  (-)            |")
        print("|             3.Perkalian    (×)            |")
        print("|             4.Pembagian    (÷)            |")
        print("|             5.Kembali                     |")
        print("|                                           |")
        print("—"*45)
        pilihan_user = int(input("| Pilih Menu ( 1 / 2 / 3 / 4 / 5 ) : "))
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
            os.system('cls')
            alert()
            menu()
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
            show_data = cursor.fetchall()
            print("—"*45)
            print("╎                  CONFIRM                  ╎")
            print("—"*45)
            for data in show_data:
                id_ = data[0]
                usn = data[1]
                name = data[2]
                print(" ")
                print("| Id User    = {}".format(id_))
                print("| Username   = {}".format(usn))
                print("| Nama       = {}".format(name))
                print(" ")

            print("—"*45)
            id_user = int(input("| Masukkan ID User Anda : "))
            # kolom nilai (n_...) disesuaikan dengan bab nya
            sql_update = 'UPDATE data SET nilai_pertambahan=%s WHERE id_user =%s '
            val_update = (score, id_user)
            cursor.execute(sql_update, val_update)
            database.commit()
            print("="*45)
            print("|                                            |")
            print("|        Nilai berhasil tersimpan ✅         |")
            print("|                                            |")
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            tampil_score()
            
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
            os.system('cls')
            print("="*45)
            print("|       Score akhir yang kamu peroleh       |")
            print('|                    {}                     |'.format(score))
            print("="*45)
            print("| Soal Terjawab benar = {}                   |".format(benar))
            print("| Soal Terjawab salah = {}                   |".format(salah))
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            menu()

        def jawab_soal(x, y):
            os.system('cls')
            print("—"*45)
            print("╎                PENJUMLAHAN                ╎")
            print("—"*45)
            pilihan_user = int(input("| {}) {} ".format(x, y)))
            d_jawabUser.append(pilihan_user)
            os.system('cls')

        def tampil_soal():

            # perintah sql untuk menampillkan soal dari database
            sql = 'SELECT soal FROM soal_tambah'
            cursor.execute(sql)

            # menampilkan soal dari database
            x = 0
            while x < 10:
                hasil = cursor.fetchone()
                d_soal.append(hasil)
                # print(d_soal)
                x += 1

            # menampilkan No soal
            x = 0
            while x < 10 :  # ganti sesuai jumlah soal
                no_soal = x+1
                d_No.append(str(no_soal))
                x += 1

            # menampilkan soal untuk user
            x = 0
            while x < 10:  # ganti sesuai jumlah soal
                for no, data in zip(d_No[x], d_soal[x]):
                    jawab_soal(no, data)
                x += 1
            koreksi_soal()

        tampil_soal()

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
            show_data = cursor.fetchall()
            print("—"*45)
            print("╎                  CONFIRM                  ╎")
            print("—"*45)
            for data in show_data:
                id_ = data[0]
                usn = data[1]
                name = data[2]
                print(" ")
                print("| Id User    = {}".format(id_))
                print("| Username   = {}".format(usn))
                print("| Nama       = {}".format(name))
                print(" ")

            print("—"*45)
            id_user = int(input("| Masukkan ID User Anda : "))
            # kolom nilai (n_...) disesuaikan dengan bab nya
            sql_update = 'UPDATE data SET nilai_pengurangan=%s WHERE id_user =%s '
            val_update = (score, id_user)
            cursor.execute(sql_update, val_update)
            database.commit()
            print("="*45)
            print("|                                            |")
            print("|        Nilai berhasil tersimpan ✅         |")
            print("|                                            |")
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            tampil_score()

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
            os.system('cls')
            print("="*45)
            print("|       Score akhir yang kamu peroleh        |")
            print('|                    {}                      |'.format(score))
            print("="*45)
            print("| Soal Terjawab benar = {}                   |".format(benar))
            print("| Soal Terjawab salah = {}                   |".format(salah))
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            menu()

        def jawab_soal(x, y):
            os.system('cls')
            print("—"*45)
            print("╎                PENGURANGAN                ╎")
            print("—"*45)
            pilihan_user = int(input("| {}) {} ".format(x, y)))
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
            koreksi_soal()

        tampil_soal()

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
            show_data = cursor.fetchall()
            print("—"*45)
            print("╎                  CONFIRM                  ╎")
            print("—"*45)
            for data in show_data:
                id_ = data[0]
                usn = data[1]
                name = data[2]
                print(" ")
                print("| Id User    = {}".format(id_))
                print("| Username   = {}".format(usn))
                print("| Nama       = {}".format(name))
                print(" ")

            print("—"*45)
            id_user = int(input("| Masukkan ID User Anda : "))
            # kolom nilai (n_...) disesuaikan dengan bab nya
            sql_update = 'UPDATE data SET nilai_perkalian=%s WHERE id_user =%s '
            val_update = (score, id_user)
            cursor.execute(sql_update, val_update)
            database.commit()
            print("="*45)
            print("|                                            |")
            print("|        Nilai berhasil tersimpan ✅         |")
            print("|                                            |")
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            tampil_score()

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
            os.system('cls')
            print("="*45)
            print("|       Score akhir yang kamu peroleh       |")
            print('|                    {}                     |'.format(score))
            print("="*45)
            print("| Soal Terjawab benar = {}                   |".format(benar))
            print("| Soal Terjawab salah = {}                   |".format(salah))
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            menu()

        def jawab_soal(x, y):
            os.system('cls')
            print("—"*45)
            print("╎                 PERKALIAN                 ╎")
            print("—"*45)
            pilihan_user = int(input("| {}) {} ".format(x, y)))
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
            koreksi_soal()

        tampil_soal()

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
            show_data = cursor.fetchall()
            print("—"*45)
            print("╎                  CONFIRM                  ╎")
            print("—"*45)
            for data in show_data:
                id_ = data[0]
                usn = data[1]
                name = data[2]
                print(" ")
                print("| Id User    = {}".format(id_))
                print("| Username   = {}".format(usn))
                print("| Nama       = {}".format(name))
                print(" ")

            print("—"*45)
            id_user = int(input("| Masukkan ID User Anda : "))
            # kolom nilai (n_...) disesuaikan dengan bab nya
            sql_update = 'UPDATE data SET nilai_pembagian=%s WHERE id_user =%s '
            val_update = (score, id_user)
            cursor.execute(sql_update, val_update)
            database.commit()
            print("="*45)
            print("|                                            |")
            print("|        Nilai berhasil tersimpan ✅         |")
            print("|                                            |")
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            tampil_score()

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
            os.system('cls')
            print("="*45)
            print("|       Score akhir yang kamu peroleh       |")
            print('|                    {}                    |'.format(score))
            print("="*45)
            print("| Soal Terjawab benar = {}                   |".format(benar))
            print("| Soal Terjawab salah = {}                   |".format(salah))
            print("="*45)
            confirm = input("| Tekan[enter] untuk kembali ")
            menu()

        def jawab_soal(x, y):
            os.system('cls')
            print("—"*45)
            print("╎                 PEMBAGIAN                 ╎")
            print("—"*45)
            pilihan_user = int(input("| {}) {} ".format(x, y)))
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
            koreksi_soal()

        tampil_soal()

    def menu():
        os.system('cls')
        print("—"*45)
        print("╎                 MENU SOAL                 ╎")
        print("—"*45)
        print("|                                           |")
        print("|             1.Penjumlahan  (+)            |")
        print("|             2.Pengurangan  (-)            |")
        print("|             3.Perkalian    (×)            |")
        print("|             4.Pembagian    (÷)            |")
        print("|             5.Kembali                     |")
        print("|                                           |")
        print("—"*45)
        pilihan_user = int(input("| Pilih Bab ( 1 / 2 / 3 / 4 / 5 ) : "))
        if (pilihan_user == 1):
            soal_penjumlahan()
        elif (pilihan_user == 2):
            soal_pengurangan()
        elif (pilihan_user == 3):
            soal_perkalian()
        elif (pilihan_user == 4):
            soal_pembagian()
        elif (pilihan_user == 5):
            menu_utama()
        else:
            os.system('cls')
            print("—"*45)
            print("|               !! ALERT !!                 |")
            print("|            Input anda salah               |")
            print("—"*45)
            confirm = input("| Tekan [enter] untuk kembali ")
            menu_soal()
    menu()
    
def menu_utama():
    os.system('cls')
    print("—"*45)
    print("╎                 KIDS MATH                 ╎")
    print("╎        PROGRAM BELAJAR MATEMATIKA         ╎")
    print("—"*45)
    print("|                                           |")
    print("|   1. Profile | 2.Soal | 3.Rank | 4.Exit   |")
    print("|                                           |")
    print("—"*45)
    pilihan_user = int(input("| Pilih menu ( 1 / 2 / 3 / 4 ) : "))
    if (pilihan_user == 1):
        menu_profile()
    elif (pilihan_user == 2):
        menu_soal()
    elif (pilihan_user == 3):
        menu_rangking()
    elif (pilihan_user == 4):
        os.system('cls')
        print("—"*45)
        print("╎                 KIDS MATH                 ╎")
        print("╎        PROGRAM BELAJAR MATEMATIKA         ╎")
        print("—"*45)
        print("|                                           |")
        print("|              Terima Kasih :)              |")
        print("|                                           |")
        print("—"*45)
        confirm = input("| See You Again..... ")
        os.system('cls')
    else:
        os.system('cls')
        alert()
        menu_utama()

menu_utama()
# pendeklarasian array
buku = []


# fungsi showdata
def show_data():
    if len(buku) <= 0:
        print('belum ada data')
    else:
        for index in range(len(buku)):
            print("[%d]%s"%(index,buku[index]))
show_data()


# fungsi insert data
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)
insert_data()


# fungsi edit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if (indeks > len(buku)):
        print("ID Salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru
edit_data()


# fungsi delete data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks > len(buku)):
        print("ID salah")
    else:
        buku.remove(buku[indeks])
delete_data()

# fungsi show menu
def show_menu():
    print("\n")
    print("======Menu=====")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    menu = int(input("Pilih Menu : "))
    print("\n")
    if menu == 1 :
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Input yang Anda masukan salah")
    if __name__ == "__main__":
        while(True):
            show_menu()
show_menu()
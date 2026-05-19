# ===================================
# [Rental Mobil]
# ===================================
# Developed by. Athiyyah Nisrina Husna
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
car_data = [
    {"id": 1, "merk": "Toyota", "model": "Avanza", "license_plate": "B 1234 EFT ", " daily_rate ": 500_000, 
"availability": True},
    {"id": 2, "merk": "Honda", "model": "Brio", "license_plate": "B 5155 ENT ", " daily_rate ": 300_000, 
"availability": True},
    {"id": 3, "merk": "Mitsubishi", "model": "Xpander", "license_plate": "B 8105 EAS ", " daily_rate ": 700_000, 
"availability": True}
]



# /===== Feature Program =====/
# Create your feature program here
# def read():
#     """Function for read the data
#     """
#     return

# def create():
#     """Function for create the data
#     """
#     return

# def update():
#     """Function for update the data
#     """
#     return

# def delete():
#     """Function for delete the data
#     """
#     return

# # /===== Main Program =====/
# # Create your main program here
# def main():
#     """Function for main program
#     """

#     input_user = input("Insert your option: ")
#     if input_user == "1":
#         read()
#     elif input_user == "2":
#         create()
#     elif input_user == "3":
#         update()
#     elif input_user == "4":
#         delete()
#     else:
#         print("Input is not valid !")

def main_menu():
    print("\n=== SELAMAT DATANG DI APLIKASI RENTAL MOBIL ===")
    print("Silahkan pilih menu: ")
    print("1. Menampilkan daftar mobil")
    print("2. Menambahkan data mobil baru")
    print("3. Menghapus data mobil")
    print("4. Mengupdate data mobil")
    print("5. Exit aplikasi")
    choice = input("Masukkan angka menu yang ingin dijalankan: ")
    return choice

def sub_menu1():
    print("\nPilih Menu: ")
    print("1. Tampilkan daftar semua mobil")
    print("2. Cari mobil berdasarkan nama")
    print("3. Kembali ke menu utama")
    submenu = input("Masukkan angka menu yang ingin dijalankan: ")
    return submenu

def sub_menu2():
    print("\nPilih Menu: ")
    print("1. Tambahkan data mobil")
    print("2. Kembali ke menu utama")
    submenu = input("Masukkan angka menu yang ingin dijalankan: ")
    return submenu

def sub_menu3():
    print("\nPilih Menu: ")
    print("1. Hapus data mobil")
    print("2. Kembali ke menu utama")
    submenu = input("Masukkan angka menu yang ingin dijalankan: ")
    return submenu

def sub_menu4():
    print("\nPilih Menu: ")
    print("1. Update data mobil")
    print("2. Kembali ke menu utama")
    submenu = input("Masukkan angka menu yang ingin dijalankan: ")
    return submenu
    
def view_all():
    print("a")
def search_car(): 
    print("b")
def add_car():
    print("c")
def delete_car():
    print("d")
def update_car():
    print("e")    
running = True
while running:
    choice = main_menu()

    if choice == "1":  # READ
        while running:
            submenu = sub_menu1()
            if submenu == "1":
                view_all()
            elif submenu == "2":
                search_car()
            elif submenu == "3":
                break  # kembali ke menu utama
            else:
                print("\nPilihan tidak ada di dalam menu\n")

    elif choice == "2":  # CREATE
        while running:
            submenu = sub_menu2()
            if submenu == "1":
                add_car()
            elif submenu == "2":
                break  
            else:
                print("\nPilihan tidak ada di dalam menu\n")

    elif choice == "3":  # DELETE
        while running:
            submenu = sub_menu3()
            if submenu == "1":
                delete_car()
            elif submenu == "2":
                break  
            else:
                print("\nPilihan tidak ada di dalam menu\n")

    elif choice == "4":  # UPDATE
        while running:
            submenu = sub_menu4()
            if submenu == "1":
                update_car()
            elif submenu == "2":
                break  
            else:
                print("\nPilihan tidak ada di dalam menu\n")

    elif choice == "5":
        running = False

    else:
        print("\nPilihan tidak ada di dalam menu\n")
        
            
        
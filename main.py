# ===================================
# [Rental Mobil]
# ===================================
# Developed by. Athiyyah Nisrina Husna
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
car_data = [
    {"id": 1, "merk": "Toyota", "model": "Avanza", "license_plate": "B 1234 EFT ", "daily_rate": 500_000, 
"availability": True},
    {"id": 2, "merk": "Honda", "model": "Brio", "license_plate": "B 5155 ENT ", "daily_rate": 300_000, 
"availability": True},
    {"id": 3, "merk": "Mitsubishi", "model": "Xpander", "license_plate": "B 8105 EAS ", "daily_rate": 700_000, 
"availability": True},
    {"id": 4, "merk": "Daihatsu", "model": "Sigra", "license_plate": "B 7865 UAI ", "daily_rate": 550_000, 
"availability": False}
    ]


# FUNCTIN TAMBAHAN
import re

def format_rupiah(amount):#Format angka ke rupiah    
    return f"Rp {amount:,.0f}".replace(",", ".")
 
 
def print_header(title): #Cetak header dengan garis pembatas
    line = "=" * 60
    print(f"\n{line}")
    print(f"  {title}")
    print(line)
 
 
def print_car_table(cars: list):
    
    if not cars:
        print("  (Tidak ada data mobil yang ditampilkan)")
        return
 
    # Lebar tiap kolom
    c1, c2, c3, c4, c5, c6 = 4, 12, 10, 14, 12, 12
 
    border = f"+{'-'*(c1+2)}+{'-'*(c2+2)}+{'-'*(c3+2)}+{'-'*(c4+2)}+{'-'*(c5+2)}+{'-'*(c6+2)}+"
    header = f"| {'No':<{c1}} | {'Merk':<{c2}} | {'Model':<{c3}} | {'Plat Nomor':<{c4}} | {'Tarif/Hari':<{c5}} | {'Status':<{c6}} |"
 
    print(f"\n{border}")
    print(header)
    print(border)
 
    for idx, car in enumerate(cars, start=1):
        status = "Tersedia" if car["availability"] else "Disewa"
        print(
            f"| {idx:<{c1}} "
            f"| {car['merk']:<{c2}} "
            f"| {car['model']:<{c3}} "
            f"| {car['license_plate']:<{c4}} "
            f"| {format_rupiah(car['daily_rate']):<{c5}} "
            f"| {status:<{c6}} |"
        )
 
    print(border)
    print(f"  Total: {len(cars)} mobil\n")



# MENU FUNCTION
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
    
# MAIN FUNCTION
    
def view_all():
    print_header("DAFTAR SEMUA MOBIL")
 
    # Tampilkan semua mobil
    print_car_table(car_data)
 
    print("Filter tampilan:")
    print("1. Hanya mobil tersedia")
    print("2. Hanya mobil sedang disewa")
    choose = input("Pilih filter [1/2] atau Enter untuk skip: ").strip()
 
    if choose == "1":
        hasil = [c for c in car_data if c["availability"]]
        print_header("MOBIL TERSEDIA")
        print_car_table(hasil)
    elif choose == "2":
        hasil = [c for c in car_data if not c["availability"]]
        print_header("MOBIL SEDANG DISEWA")
        print_car_table(hasil)
    elif choose == "":
        pass
    else:
        print("\n  Pilihan tidak valid.")


def search_car(): 
    print_header("CARI MOBIL")
 
    keyword = input("Masukkan nama merk mobil yang dicari: ").strip().lower()
 
    if not keyword:
        print("\n  Keyword tidak boleh kosong.")
        return
 
    result = [
        c for c in car_data
        if keyword in c["merk"].lower() or keyword in c["model"].lower()
    ]
    
    #hasil
    print_header(f"HASIL PENCARIAN: {len(result)} mobil ditemukan")
    if result:
        print_car_table(result)
    else:
        print("Tidak ada mobil yang sesuai dengan pencarian Anda.\n")

def add_car():
    print_header("TAMBAH DATA MOBIL")

    while True:
        merk = input("Masukkan merk mobil: ").strip()
        if merk:
            break
        else:
            print("Merk tidak boleh kosong!")

    while True:
        model = input("Masukkan model mobil: ").strip()
        if model:
            break
        else:
            print("Model tidak boleh kosong!")
            
    # validasi license plate
    while True:
        license_plate = input("Masukkan plat nomor (contoh: B 1234 ABC): ").strip().upper()
        if not re.fullmatch(r"[A-Z]{1,2} \d{1,4} [A-Z]{1,3}", license_plate):
            print("  Format plat tidak valid! Contoh yang benar: B 1234 ABC")
        else:
            duplicate = False
            for c in car_data:
                if c["license_plate"].strip() == license_plate:
                    duplicate = True
                    break
            if duplicate:
                print("  Plat nomor sudah terdaftar! Masukkan plat nomor lain.")
            else:
                break
    
    # Validasi input harga
    while True:
        daily_rate_input = input("Masukkan tarif harian (Rp): ").strip()
        if daily_rate_input.isdigit():
            daily_rate = int(daily_rate_input)
            break
        else:
            print("Tarif harus berupa angka!")
            
    # availability       
    while True:
        print("Status ketersediaan mobil:")
        print("1. Tersedia")
        print("2. Sedang Disewa")
        avail_input = input("Pilih status (1/2): ").strip()
        if avail_input == "1":
            availability = True
            break
        elif avail_input == "2":
            availability = False
            break
        else:
            print("Pilihan tidak valid, masukkan 1 atau 2!")
    
    car = {
        "id"            : len(car_data) + 1,
        "merk"          : merk,
        "model"         : model,
        "license_plate" : license_plate,
        "daily_rate"    : daily_rate,
        "availability"  : availability
    }
    print(car)
    confirm = input("yakin untuk menambah produk (y/n)?")
    if confirm.lower() == "y":
        car_data.append(car)
        print("Mobil berhasil ditambahkan!")
        print_car_table(car_data)
    else:
        print("Mobil batal ditambahkan")
       
def delete_car():
    print_car_table(car_data)
    while True:
        index_input = input("Masukkan index mobil yang ingin dihapus: ").strip()
        if index_input.isdigit():
            index_delete = int(index_input)
            break
        else:
            print("Index harus berupa angka!")
            
    if 1 <= index_delete <= len(car_data):
        deleted = car_data[index_delete - 1]
        print(f"\nMobil yang akan dihapus:")
        print_car_table([deleted])
        confirm = input("Yakin ingin menghapus mobil ini? (y/n): ").strip().lower()
        if confirm == "y":
            car_data.pop(index_delete - 1)
            print(f"'{deleted['merk']} {deleted['model']}' berhasil dihapus!")
            print_car_table(car_data)
        else:
            print("Penghapusan dibatalkan.")
    else: 
        print("index tidak valid!")      
    
def update_car():
    print_car_table(car_data)
    
    while True: # pilih cara pencarian
        print("Cari mobil berdasarkan:")
        print("1. Merk")
        print("2. Model")
        print("3. Plat Nomor")
        search_choice = input("Pilih metode pencarian (1-3): ").strip()
        
        found = None
        if search_choice == "1":
            keyword = input("Masukkan merk mobil: ").strip().lower()
            hasil = [c for c in car_data if c["merk"].lower() == keyword]

        elif search_choice == "2":
            keyword = input("Masukkan model mobil: ").strip().lower()
            hasil = [c for c in car_data if c["model"].lower() == keyword]

        elif search_choice == "3":
            keyword = input("Masukkan plat nomor: ").strip().upper()
            hasil = [c for c in car_data if c["license_plate"].strip() == keyword]
        
        else:
            print("Pilihan tidak valid, masukkan 1-3!")
            continue

        if not hasil:
            print("Mobil tidak ditemukan! Coba lagi.")
            continue

        # jika hasil lebih dari 1, tampilkan dan minta user pilih
        if len(hasil) == 1:
            found = hasil[0]
            break
        else:
            print("\nDitemukan lebih dari 1 mobil:")
            print_car_table(hasil)
            while True:
                pilih_input = input(f"Pilih nomor mobil (1-{len(hasil)}): ").strip()
                if pilih_input.isdigit() and 1 <= int(pilih_input) <= len(hasil):
                    found = hasil[int(pilih_input) - 1]
                    break
                else:
                    print(f"Pilihan tidak valid! Masukkan 1-{len(hasil)}.")
            break
   
    # data lama disimpan
    data_lama = found.copy()
    
    # pilih bagian yang ingin diupdate
    while True:
        print("Pilih bagian yang ingin diupdate:")
        print("1. Merk")
        print("2. Model")
        print("3. Plat Nomor")
        print("4. Tarif Harian")
        print("5. Status Ketersediaan")
        pilihan = input("Pilih (1-5): ").strip()
        
        if pilihan == "1":
            while True:
                merk_baru = input("Masukkan merk baru: ").strip()
                if merk_baru:
                    found["merk"] = merk_baru
                    break
                else:
                    print("  Merk tidak boleh kosong!")
                    break
    
        elif pilihan == "2":
            while True:
                model_baru = input("Masukkan model baru: ").strip()
                if model_baru:
                    found["model"] = model_baru
                    break
                else:
                    print("  Model tidak boleh kosong!")
            break
        
        elif pilihan == "3":
            while True:
                plat_baru = input("Masukkan plat nomor baru (contoh: B 1234 ABC): ").strip().upper()
                if not re.fullmatch(r"[A-Z]{1,2} \d{1,4} [A-Z]{1,3}", plat_baru):
                    print("Format plat tidak valid!")
                else:
                    duplicate = False
                    for c in car_data:
                        if c["license_plate"] == plat_baru:
                            duplicate = True
                            break
                    if duplicate:
                        print("Plat nomor sudah terdaftar!")
                    else:
                        found["license_plate"] = plat_baru
                        break
            break
        
        elif pilihan == "4":
            while True:
                tarif_baru = input("Masukkan tarif harian baru (Rp): ").strip()
                if tarif_baru.isdigit():
                    found["daily_rate"] = int(tarif_baru)
                    break
                else:
                    print("  Tarif harus berupa angka!")
            break
        
        elif pilihan == "5":
            while True:
                print("Status ketersediaan:")
                print("1. Tersedia")
                print("2. Sedang Disewa")
                status_baru = input("Pilih status (1/2): ").strip()
                if status_baru == "1":
                    found["availability"] = True
                    break
                elif status_baru == "2":
                    found["availability"] = False
                    break
                else:
                    print("Pilihan tidak valid!")
            break
        
        else:
            print("Pilihan tidak valid, masukkan 1-5!")
    
    # konfirmasi
    print("\nData setelah diupdate:")
    print_car_table([found])
    confirm = input("Yakin ingin menyimpan perubahan? (y/n): ").strip().lower()
    if confirm == "y":
        print(f"  '{found['merk']} {found['model']}' berhasil diupdate!")
        print_car_table(car_data)
    else:
        found.update(data_lama)
        print("Update dibatalkan.")
           
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
        
            
        
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Fungsi untuk menampilkan banner
def display_banner():
    banner_text1 = """
██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗     ███████╗███████╗ ██████╗
██║ ██╔╝██╔═══██╗██║ ██╔╝██╔═══██╗██║ ██╔╝     ██╔════╝██╔════╝██╔════╝
█████╔╝ ██║   ██║█████╔╝ ██║   ██║█████╔╝█████╗███████╗█████╗  ██║     
██╔═██╗ ██║   ██║██╔═██╗ ██║   ██║██╔═██╗╚════╝╚════██║██╔══╝  ██║     
██║  ██╗╚██████╔╝██║  ██╗╚██████╔╝██║  ██╗     ███████║███████╗╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     
                Kalkulator - Powered by kikikokok
    """
    banner_text2 = """
     ====================================================================
     **                  Instagram : @risky.manuel                     **
     **                  Telegram  : @kikikokok9                       **
     **                  Email     : riskymanuel08@proton.me           **
     ====================================================================
    """
    print(banner_text1)
    print(banner_text2)

# Fungsi-fungsi operasi matematika
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return "Tidak dapat membagi dengan nol!" if b == 0 else a / b

# Fungsi untuk menampilkan menu
def show_menu():
    print("\nMenu Perhitungan:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Tampilkan Riwayat")
    print("6. Keluar")

# Fungsi utama
def main():
    display_banner()
    history = []  # Menyimpan riwayat perhitungan

    operations = {
        '1': tambah,
        '2': kurang,
        '3': kali,
        '4': bagi
    }

    while True:
        show_menu()
        choice = input("Pilih operasi (1/2/3/4/5/6): ")

        if choice in operations.keys():
            try:
                num1 = float(input("Masukkan angka pertama: "))
                num2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
                continue

            # Lakukan operasi yang dipilih
            operation = operations[choice]
            result = operation(num1, num2)
            print(f"Hasil: {result}")

            # Simpan ke riwayat
            history.append(f"{num1} {operation.__name__} {num2} = {result}")

        elif choice == '5':
            print("\n=== Riwayat Perhitungan ===")
            if history:
                for entry in history:
                    print(entry)
            else:
                print("Belum ada riwayat.")
        elif choice == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

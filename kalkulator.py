import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Define colors
NORMAL = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"
LGREEN = "\033[92m"
DGRAY = "\033[90m"
RED = "\033[91m"
LBLUE = "\033[1;34m"
RESET = "\033[0m"  # Tambahkan ini untuk menghindari NameError

# Fungsi untuk menampilkan banner
def display_banner():
    banner_text1 = f"""{BOLD}{LGREEN}
██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗     ███████╗███████╗ ██████╗
██║ ██╔╝██╔═══██╗██║ ██╔╝██╔═══██╗██║ ██╔╝     ██╔════╝██╔════╝██╔════╝
█████╔╝ ██║   ██║█████╔╝ ██║   ██║█████╔╝█████╗███████╗█████╗  ██║     
██╔═██╗ ██║   ██║██╔═██╗ ██║   ██║██╔═██╗╚════╝╚════██║██╔══╝  ██║     
██║  ██╗╚██████╔╝██║  ██╗╚██████╔╝██║  ██╗     ███████║███████╗╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝ ╚═════╝
                                    {RESET}
                {BOLD}Kalkulator - Powered by kikikokok{RESET}
    """
    banner_text2 = f"""
     {BOLD}{RED}====================================================================
     **                  Instagram : @risky.manuel                     **
     **                  Telegram  : @kikikokok9                       **
     **                  Email     : riskymanuel08@proton.me           **
     ===================================================================={RESET}
    """
    extra_text = f"""
{BOLD}{RED}V 1.0 ~ Happy Hunting - Mr.Kiy 
 ̿̿ ̿̿ ̿̿ ̿'̿'\\̵͇̿̿\\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿{RESET}

{BLINK}{LBLUE}🕱 @risky.manuel {DGRAY} | {RED}kikikokok-sec {NORMAL}
"""
    
    # Print the combined banner
    print(banner_text1)
    print(banner_text2)
    print(extra_text)

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

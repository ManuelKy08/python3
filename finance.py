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
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝ ╚═════╝ 
       Aplikasi Manajemen Keuangan Sederhana - Powered by kikikokok
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

class FinanceManager:
    def __init__(self):
        self.income = 0
        self.expenses = 0

    def add_income(self, amount):
        self.income += amount
        logging.info(f"Pemasukan ditambahkan: {amount}")

    def add_expense(self, amount):
        self.expenses += amount
        logging.info(f"Pengeluaran ditambahkan: {amount}")

    def get_balance(self):
        return self.income - self.expenses

    def get_report(self):
        return {
            'Pemasukan': self.income,
            'Pengeluaran': self.expenses,
            'Saldo': self.get_balance()
        }

def show_menu():
    print("\nMenu Manajemen Keuangan:")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Tampilkan Laporan Keuangan")
    print("4. Keluar")

def main():
    display_banner()
    manager = FinanceManager()

    while True:
        show_menu()
        choice = input("Pilih tindakan (1/2/3/4): ")

        if choice == '1':
            try:
                amount = float(input("Masukkan jumlah pemasukan: "))
                manager.add_income(amount)
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        elif choice == '2':
            try:
                amount = float(input("Masukkan jumlah pengeluaran: "))
                manager.add_expense(amount)
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        elif choice == '3':
            report = manager.get_report()
            print("\nLaporan Keuangan:")
            for key, value in report.items():
                print(f"{key}: {value}")
        elif choice == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

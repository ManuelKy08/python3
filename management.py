import logging
import json

logging.basicConfig(level=logging.INFO)

def display_banner():
    banner_text1 = """
██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗     ███████╗███████╗ ██████╗
██║ ██╔╝██╔═══██╗██║ ██╔╝██╔═══██╗██║ ██╔╝     ██╔════╝██╔════╝██╔════╝
█████╔╝ ██║   ██║█████╔╝ ██║   ██║█████╔╝█████╗███████╗█████╗  ██║     
██╔═██╗ ██║   ██║██╔═██╗ ██║   ██║██╔═██╗╚════╝╚════██║██╔══╝  ██║     
██║  ██╗╚██████╔╝██║  ██╗╚██████╔╝██║  ██╗     ███████║███████╗╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝ ╚═════╝ 
          Sistem Manajemen Inventaris - Powered by kikikokok
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

# Kelas untuk barang di inventaris
class Item:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def __str__(self):
        return f"{self.name}: {self.stock} item(s)"

# Fungsi untuk menambahkan barang
def add_item(inventory, name, quantity):
    if name in inventory:
        inventory[name].stock += quantity
    else:
        inventory[name] = Item(name, quantity)
    logging.info(f"Menambahkan {quantity} item(s) ke {name}.")

# Fungsi untuk mengurangi barang
def remove_item(inventory, name, quantity):
    if name in inventory and inventory[name].stock >= quantity:
        inventory[name].stock -= quantity
        logging.info(f"Mengurangi {quantity} item(s) dari {name}.")
        if inventory[name].stock == 0:
            del inventory[name]  # Hapus item jika stoknya habis
    else:
        logging.warning(f"Tidak cukup stok untuk {name} atau item tidak ditemukan.")

# Fungsi untuk menampilkan seluruh inventaris
def display_inventory(inventory):
    print("\nStok Inventaris:")
    for item in inventory.values():
        print(item)

# Fungsi untuk menyimpan riwayat perubahan stok
def save_stock_history(history, filename='stock_history.json'):
    with open(filename, 'w') as file:
        json.dump(history, file, indent=4)
    logging.info(f"Riwayat perubahan stok disimpan ke {filename}.")

def main():
    display_banner()

    inventory = {}
    stock_history = []

    while True:
        print("\nMenu:")
        print("1. Tambah Stok")
        print("2. Kurangi Stok")
        print("3. Tampilkan Stok")
        print("4. Keluar")

        choice = input("Pilih tindakan (1/2/3/4): ")

        if choice == '1':
            item_name = input("Masukkan nama barang: ")
            quantity = int(input("Masukkan jumlah yang ingin ditambahkan: "))
            add_item(inventory, item_name, quantity)
            stock_history.append(f"Tambah: {item_name} sebanyak {quantity}")
        elif choice == '2':
            item_name = input("Masukkan nama barang: ")
            quantity = int(input("Masukkan jumlah yang ingin dikurangi: "))
            remove_item(inventory, item_name, quantity)
            stock_history.append(f"Kurangi: {item_name} sebanyak {quantity}")
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            save_stock_history(stock_history)
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

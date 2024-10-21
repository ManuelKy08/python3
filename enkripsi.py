import string
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
               Alat Enkripsi Pesan - Powered by kikikokok
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

# Caesar Cipher Encryption/Decryption
def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(table)

# Vigenère Cipher Encryption/Decryption
def vigenere_cipher(text, key, decrypt=False):
    alphabet = string.ascii_lowercase
    key = key.lower()
    key_indices = [alphabet.index(k) for k in key]

    result = []
    key_index = 0
    for char in text:
        if char.lower() in alphabet:
            shift = key_indices[key_index % len(key)]
            if decrypt:
                shift = -shift
            new_char = caesar_cipher(char, shift)
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)  # Keep punctuation and spaces

    return ''.join(result)

def show_menu():
    print("\nMenu Enkripsi Pesan:")
    print("1. Enkripsi dengan Caesar Cipher")
    print("2. Dekripsi dengan Caesar Cipher")
    print("3. Enkripsi dengan Vigenère Cipher")
    print("4. Dekripsi dengan Vigenère Cipher")
    print("5. Keluar")

def main():
    display_banner()

    while True:
        show_menu()
        choice = input("Pilih tindakan (1/2/3/4/5): ")

        if choice in ['1', '2']:
            text = input("Masukkan pesan: ")
            shift = int(input("Masukkan kunci (shift): "))
            if choice == '1':
                encrypted_text = caesar_cipher(text, shift)
                print(f"Hasil enkripsi: {encrypted_text}")
            else:
                decrypted_text = caesar_cipher(text, shift, decrypt=True)
                print(f"Hasil dekripsi: {decrypted_text}")

        elif choice in ['3', '4']:
            text = input("Masukkan pesan: ")
            key = input("Masukkan kunci (kata): ")
            if choice == '3':
                encrypted_text = vigenere_cipher(text, key)
                print(f"Hasil enkripsi: {encrypted_text}")
            else:
                decrypted_text = vigenere_cipher(text, key, decrypt=True)
                print(f"Hasil dekripsi: {decrypted_text}")

        elif choice == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

import logging

logging.basicConfig(level=logging.INFO)

def display_banner():
    banner_text1 = """
██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗     ███████╗███████╗ ██████╗
██║ ██╔╝██╔═══██╗██║ ██╔╝██╔═══██╗██║ ██╔╝     ██╔════╝██╔════╝██╔════╝
█████╔╝ ██║   ██║█████╔╝ ██║   ██║█████╔╝█████╗███████╗█████╗  ██║     
██╔═██╗ ██║   ██║██╔═██╗ ██║   ██║██╔═██╗╚════╝╚════██║██╔══╝  ██║     
██║  ██╗╚██████╔╝██║  ██╗╚██████╔╝██║  ██╗     ███████║███████╗╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝ ╚═════╝ 
          Penyaring Email - Powered by kikikokok
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

def filter_emails(emails, keywords):
    important_emails = []
    for email in emails:
        if any(keyword.lower() in email.lower() for keyword in keywords):
            important_emails.append(email)
    return important_emails

# Fungsi untuk menyimpan email penting ke file
def save_important_emails(important_emails, filename='cek_emails.txt'):
    with open(filename, 'w') as file:
        for email in important_emails:
            file.write(email + '\n')
    logging.info(f"{len(important_emails)} email penting telah disimpan ke {filename}.")

# Fungsi untuk menghitung frekuensi kata kunci
def analyze_keywords(emails, keywords):
    keyword_freq = {keyword: 0 for keyword in keywords}
    for email in emails:
        for keyword in keywords:
            if keyword.lower() in email.lower():
                keyword_freq[keyword] += 1
    return keyword_freq

def main():
    display_banner()

    # Daftar email contoh
    emails = [
        "Penting: Rapat besok jam 10 pagi.",
        "Promo: Diskon 50% untuk produk kami.",
        "Notifikasi: Pembayaran berhasil.",
        "Penting: Risky akan makan siang pukul 14.20 WIB.",
        "Newsletter: kokok suka sama inisial E tapi dia ga pernah pacaran dan malu mengungkapkannya.",
        "Tindakan Diperlukan: Tindak lanjuti laporan."
    ]

    keywords = input("Masukkan kata kunci (pisahkan dengan koma): ").split(',')

    keywords = [keyword.strip() for keyword in keywords]

    important_emails = filter_emails(emails, keywords)

    save_important_emails(important_emails)

    keyword_analysis = analyze_keywords(emails, keywords)
    print("\nAnalisis Frekuensi Kata Kunci:")
    for keyword, freq in keyword_analysis.items():
        print(f"{keyword}: {freq} kali ditemukan.")

if __name__ == "__main__":
    main()

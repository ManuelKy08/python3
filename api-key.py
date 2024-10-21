import requests
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
                 API Client - Powered by kikikokok
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

# Fungsi untuk mendapatkan cuaca dari OpenWeather API
def get_weather(city_name, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except requests.exceptions.HTTPError as errh:
        logging.error(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        logging.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        logging.error(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        logging.error(f"Something went wrong: {err}")
    return None

def show_menu():
    print("\nMenu:")
    print("1. Cari cuaca berdasarkan kota")
    print("2. Keluar")

def main():
  
    display_banner()
    api_key = "MASUKKAN_API_KEY_ANDA_DI_SINI"  # Ganti dengan API key dari OpenWeatherMap atau dari mana aja yah!

    while True:
        show_menu()
        choice = input("Pilih tindakan (1/2): ")

        if choice == '1':
            city_name = input("Masukkan nama kota: ")
            weather = get_weather(city_name, api_key)
            if weather:
                print(f"\nCuaca di {weather['city']}, {weather['country']}:")
                print(f"Suhu: {weather['temperature']}°C")
                print(f"Kondisi: {weather['description']}\n")
            else:
                print("Gagal mendapatkan data cuaca. Coba lagi.")
        elif choice == '2':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

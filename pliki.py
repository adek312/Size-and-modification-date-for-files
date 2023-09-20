import os
import datetime
import pathlib

def main():
    
    while True:
        try:
            print("Podaj ścieżkę do folderu zgodnie ze wzorem: X:\\folder\\folder\\plik")
            type_path = input()
            if os.path.exists(type_path):
                break
        except FileNotFoundError:
            print("Zły format")
    
    # Przechowanie listy wszystkich plikow ze sciezki
    file_list = os.listdir(type_path)
    while True:
        try:
            print("Co chcesz sprawdzić:")
            print("1- wielkość plików")
            print("2- datę modyfikacji")
            choice = int(input())
            break
        except ValueError:
            print("Niepoprawny wybór")    
    if choice == 1: list_size(file_list, type_path)
    elif choice == 2: list_modification(file_list, type_path)
    else: print("Niepoprawny wybór choice = {}".format(choice))
        
            


def list_size(file_list, type_path):
    for plik in file_list:
            full_path = os.path.join(type_path, plik)
            size = os.path.getsize(full_path)
            megaOrGiga = megabytes_or_gigabytes(size)
            print('Plik {} waży: {}'.format(plik, megaOrGiga))

def list_modification(file_list, type_path):
    for plik in file_list:
            full_path = os.path.join(type_path, plik)
            mod_time = os.path.getmtime(full_path)
            mod_time_str = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d o godzinie: %H:%M:%S')
            print('Plik {} użyty był: {}'.format(plik, mod_time_str))

# Sprawdzenie czy plik jest w GB czy MB
def megabytes_or_gigabytes(bytes):
    if bytes >= 1024 ** 3: 
        Gbytes = bytes / (1024 ** 3)
        return f"{Gbytes:.2f} GB"
    else: 
        Mbytes = bytes / (1024 ** 2)
        return f"{Mbytes:.2f} MB"
    
# Wywolanie glownej funkcji przy starcie skryptu
if __name__ == "__main__":
    main()
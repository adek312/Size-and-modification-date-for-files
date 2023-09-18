import os
import datetime
import pathlib

def main():
    # Uzyskanie sciezki od uzytkownika
    print("Podaj ścieżkę do folderu zgodnie ze wzorem: X:\\folder\\folder\\plik")
    type_path = input()
    
    # Wybor co uzytkownik chce sprawdzic
    print("Co chcesz sprawdzić:")
    print("1- wielkość plików")
    print("2- datę modyfikacji")
    choice = input()

    # Przechowanie listy wszystkich plikow ze sciezki
    file_list = os.listdir(type_path)
    
        # Wylistowanie wszystkich plikow i ich wielkosci
    if (choice == '1'):
        for plik in file_list:
            full_path = os.path.join(type_path, plik)
            size = os.path.getsize(full_path)
            megaOrGiga = megabytes_or_gigabytes(size)
            print('Plik {} waży: {}'.format(plik, megaOrGiga))
               
        # Wylistowanie wszystkich plikow i ich daty modyfikacji 
    elif (choice == '2'):
        for plik in file_list:
            full_path = os.path.join(type_path, plik)
            mod_time = os.path.getmtime(full_path)
            mod_time_str = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d o godzinie: %H:%M:%S')
            print('Plik {} użyty był: {}'.format(plik, mod_time_str))    
            
    else:
        print("niepoprawny wybór")

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
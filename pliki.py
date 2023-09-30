import os
import datetime

def main():
    
    #* Zczytanie sciezki
    while True:
        try:
            print("Podaj ścieżkę do folderu zgodnie ze wzorem: X:\\folder\\folder\\plik")
            type_path = input()
            if os.path.exists(type_path):
                break
        except FileNotFoundError:
            print("Zły format")
    
    #* Przechowanie listy wszystkich plikow ze sciezki
    file_list = os.listdir(type_path)
    
    #* Wybor do wylistowania
    while True:
        try:
            print("Co chcesz sprawdzić:")
            print("1- wielkość plików")
            print("2- datę modyfikacji")
            choice = int(input())
            break
        except ValueError:
            print("Niepoprawny wybór")    
    if choice == 1: file_size(file_list, type_path)
    elif choice == 2: list_modification(file_list, type_path)



#* Wylistowanie wielkosci        
def file_size(file_list, type_path):
    for plik in file_list:
        full_path = os.path.join(type_path, plik)
        # Folder
        if  os.path.isdir(full_path): 
            #? Funkcja directory_size sprawdza wielkość folderu w bajtach, która potem
            #? Jest przesyłana do funkcji m_o_g, która sprawdza czy wielkość ma być
            #? Podana w GB lub MB
            megaOrGiga = megabytes_or_gigabytes(directory_size(full_path))
            lista = {}
            lista[plik] = megaOrGiga
            for nazwa, rozmiar in lista.items():
                sorting(nazwa, rozmiar)
        # Plik
        else:
            size = os.path.getsize(full_path)
            megaOrGiga = megabytes_or_gigabytes(size)
            lista = {}
            lista[plik] = megaOrGiga
            #for nazwa, rozmiar in lista.items():
                #print('{}, {}'.format(nazwa, rozmiar))

#TODO zrobić sortowanie najpierw po GB, potem po MB i połączyć GB z MB    
def sorting(nazwa, rozmiar):
    pass
    
#* Obliczanie wielkości folderu
def directory_size(file_list):
    bytes = 0
    for main_path, katalogi, files in os.walk(file_list):
        for plik in files:
            plik_sciezka = os.path.join(main_path, plik)
            bytes += os.path.getsize(plik_sciezka)
    return bytes

#* Wylistowanie czasu modyfikacji
def list_modification(file_list, type_path):
    for plik in file_list:
            full_path = os.path.join(type_path, plik)
            mod_time = os.path.getmtime(full_path)
            mod_time_str = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d o godzinie: %H:%M:%S')
            print('Plik {} użyty był: {}'.format(plik, mod_time_str))

    
#* Sprawdzenie czy plik jest w GB czy MB
def megabytes_or_gigabytes(bytes):
    if bytes >= 1024 ** 3: 
        Gbytes = bytes / (1024 ** 3)
        return f"{Gbytes:.2f} GB"
    else: 
        Mbytes = bytes / (1024 ** 2)
        return f"{Mbytes:.2f} MB"
    
    





#* Wywolanie glownej funkcji przy starcie skryptu
if __name__ == "__main__":
    main()
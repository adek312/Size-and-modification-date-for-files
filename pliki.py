import os
import datetime


def main():
    print("Podaj ścieżkę do folderu zgodnie ze wzorem: X:\\folder\\folder\\plik")
    type_path = input()

    print("Co chcesz sprawdzić:")
    print("1- wielkość plików")
    print("2- datę modyfikacji")
    choice = input()

    file_list = os.listdir(type_path)
    if (os.path.isdir(type_path)):
        if (choice == '1'):
            for plik in file_list:
                full_path = os.path.join(type_path, plik)
                size = os.path.getsize(full_path)
                megabyte_size = bytes_to_megabytes(size)
                print('Plik {} waży: {}MB'.format(plik, megabyte_size))
                
        elif (choice == '2'):
            for plik in file_list:
                full_path = os.path.join(type_path, plik)
                mod_time = os.path.getmtime(full_path)
                mod_time_str = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d o godzinie: %H:%M:%S')
                print('Plik {} użyty był: {}'.format(plik, mod_time_str))    
                
        else:
            print("niepoprawny wybór")
    elif os.path.isdir(type_path)== False:
        print("niepoprawna ścieżka do folderu")


def bytes_to_megabytes(bytes):
    megabytes = bytes / (1024*1024)
    formatted_megabytes = "{:.2f}".format(megabytes)
    return formatted_megabytes
        

if __name__ == "__main__":
    main()
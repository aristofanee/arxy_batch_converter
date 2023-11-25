import zipfile
from pandas import DataFrame
from os import walk
from os import mkdir
from tkinter.filedialog import askdirectory
import struct

folder_from = askdirectory()
folder_to = askdirectory()


dir_tree = walk(folder_from)

for element in dir_tree:
    new_folder = folder_to + "/export_csv/" + element[0].replace(folder_from,'').replace('\\','') + '/' 
    mkdir(new_folder)

    for file_in_dir in element[2]:
        if file_in_dir.endswith(".aryx"):

            old_folder = element[0].replace('\\','/') + '/'

            with zipfile.ZipFile(old_folder + file_in_dir,'r') as aryx_file:
                for file in aryx_file.namelist():
                    if file.endswith(".~tmp"):
                        with aryx_file.open(file) as file_bin:
                            file_bin = file_bin.read()

                            num_doubles = len(file_bin) // struct.calcsize('d')
                            data = struct.unpack('<' + 'd' * num_doubles, file_bin)

                            intens = data[::2]
                            wl = data[1::2]

                        nome_csv = file_in_dir.replace('.aryx','.csv')
                        with open(new_folder + nome_csv,'w', newline = '') as file_csv:
                            df = DataFrame({'wl':wl,'int':intens})
                            DataFrame.to_csv(df,file_csv,header=True,index=False,mode='w')
                       
                        







                        



                    

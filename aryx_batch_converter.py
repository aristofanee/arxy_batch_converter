import zipfile
from pandas import DataFrame
from os import walk, mkdir, path
from tkinter.filedialog import askdirectory
from tkinter import Tk
import struct
from alive_progress import alive_bar




print("""\nAn .aryx to .csv spectra batch converter!\n 
First select the folder that you \033[32mwant to convert\033[39m, then the \033[32mdestination directory\033[39m.
The folder structure will be cloned in the new directory.
All the aryx files in the folders and subfolders will be converted into csv.""")

print("\nThe original files will \033[31mNOT\033[39m be affected.\n")


x = Tk()
x.withdraw()
x.after(2000)


folder_from = askdirectory(title = "Select the directory that you want to convert:")
folder_to = askdirectory(title = "Select were you want to save the converted folder:")

folder_from_name = path.basename(folder_from)


number_of_aryx = 0
for element in walk(folder_from):
    for file_in_dir in element[2]:
        if file_in_dir.endswith(".aryx"):
            number_of_aryx += 1


dir_tree = walk(folder_from)

print("\033[34m")

with alive_bar(number_of_aryx) as bar:

    for element in dir_tree:

        
        new_folder = folder_to + "/" + folder_from_name + "_csv" + element[0].replace('\\','/').replace(folder_from,'') + '/'
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

                            
                            bar()
                            

print("\033[39m")
                            
print("\033[32m\nConversion completed!\033[39m\n")

x.after(2000)  
x.destroy()







                        



                    

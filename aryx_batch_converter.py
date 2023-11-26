import zipfile
from pandas import DataFrame
<<<<<<< HEAD
from os import walk, makedirs, path
=======
from os import walk, mkdir, path
>>>>>>> 7881a2eb4401dd02b86a8f57572e9b6ec7aff54d
from tkinter.filedialog import askdirectory
from tkinter import Tk
import struct
from alive_progress import alive_bar


#description of the program

<<<<<<< HEAD
print("""\nAn .aryx to .csv spectra batch converter!\n 
First select the folder that you \033[32mwant to convert\033[39m, then the \033[32mdestination directory\033[39m.
The folder structure will be cloned in the new directory.
All the .aryx files in the folders and subfolders will be converted into .csv.""")

print("\nThe original files or folders will \033[31mNOT\033[39m be affected.\n")


#opening and hiding the tk root window
root = Tk()
root.withdraw()


#inserting the source and destination directory with error handling if window is closed
folder_from = askdirectory(title = "Select the directory that you want to convert")

if folder_from == '':
    print("You need a valid directory, please restart the program.")
    root.after(2000) 
    quit()


folder_to = askdirectory(title = "Select were you want to save the converted folder")

if folder_to == '':
    print("You need a valid directory, please restart the program.")
    root.after(2000)  
    quit()


#scraping the name of the folder to create the version with "_csv" at the end
folder_from_name = path.basename(folder_from)


#this loop is needed for both counting the number of files (for the progress bar)
#and for checking if the destination folder is inside the source one
number_of_aryx = 0
for element in walk(folder_from):
    if element[0].replace('\\','/') == folder_to: #
        print("The destination folder can't be inside the source one.")
        root.after(2000)  
        quit()
=======

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
>>>>>>> 7881a2eb4401dd02b86a8f57572e9b6ec7aff54d
    for file_in_dir in element[2]:
        if file_in_dir.endswith(".aryx"):
            number_of_aryx += 1

<<<<<<< HEAD
#function needed to "scan" the directory and subdirectories 
dir_tree = walk(folder_from)

print("\033[34m")

#the whole conversion is inside a "with" for the progress bar
with alive_bar(number_of_aryx) as bar:

    for element in dir_tree:

        #creates the path of the new folder each iteratiomn it takes the first part form the destination folder
        #and the second part form the source one
        new_folder = folder_to + "/" + folder_from_name + "_csv" + element[0].replace('\\','/').replace(folder_from,'') + '/'

        #creating the new directory, ignoring the overwriting 
        makedirs(new_folder, exist_ok=True)

        #iteration for every file in every directory of the tree, checking for the .aryx one
=======

dir_tree = walk(folder_from)

print("\033[34m")

with alive_bar(number_of_aryx) as bar:

    for element in dir_tree:

        
        new_folder = folder_to + "/" + folder_from_name + "_csv" + element[0].replace('\\','/').replace(folder_from,'') + '/'
        mkdir(new_folder)

>>>>>>> 7881a2eb4401dd02b86a8f57572e9b6ec7aff54d
        for file_in_dir in element[2]:
            if file_in_dir.endswith(".aryx"):

                old_folder = element[0].replace('\\','/') + '/'

<<<<<<< HEAD
                #"extracting" the .aryx
                with zipfile.ZipFile(old_folder + file_in_dir,'r') as aryx_file:
                    for file in aryx_file.namelist():
                        #scraping the binary file with the .~tmp and opening it as a zipfile file object
                        if file.endswith(".~tmp"):
                            with aryx_file.open(file) as file_bin:
                                #actually accessing the bytes of the binary
                                file_bin = file_bin.read()

                                #unpacking the bytes into a tuple
                                num_doubles = len(file_bin) // struct.calcsize('d')
                                data = struct.unpack('<' + 'd' * num_doubles, file_bin)

                                #creating the array for the intensity and wavelengths 
                                intens = data[::2]
                                wl = data[1::2]

                            #creating and writing the csv
=======
                with zipfile.ZipFile(old_folder + file_in_dir,'r') as aryx_file:
                    for file in aryx_file.namelist():
                        if file.endswith(".~tmp"):
                            with aryx_file.open(file) as file_bin:
                                file_bin = file_bin.read()

                                num_doubles = len(file_bin) // struct.calcsize('d')
                                data = struct.unpack('<' + 'd' * num_doubles, file_bin)

                                intens = data[::2]
                                wl = data[1::2]

>>>>>>> 7881a2eb4401dd02b86a8f57572e9b6ec7aff54d
                            nome_csv = file_in_dir.replace('.aryx','.csv')
                            with open(new_folder + nome_csv,'w', newline = '') as file_csv:
                                df = DataFrame({'wl':wl,'int':intens})
                                DataFrame.to_csv(df,file_csv,header=True,index=False,mode='w')
<<<<<<< HEAD
                            
                            #updating the progress bar
=======

                            
>>>>>>> 7881a2eb4401dd02b86a8f57572e9b6ec7aff54d
                            bar()
                            

print("\033[39m")
                            
print("\033[32m\nConversion completed!\033[39m\n")
<<<<<<< HEAD
root.after(2000)  

#closing the tkinter window
root.destroy()
=======

x.after(2000)  
x.destroy()
>>>>>>> 7881a2eb4401dd02b86a8f57572e9b6ec7aff54d







                        



                    

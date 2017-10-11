import os
def remane_files():
   # (1) obtener nombres de archivos desde folder
   file_list = os.listdir("/Users/LaDulce/Desktop/dev")
   print file_list
   saved_path = os.getcwd()
   print ("Current Working Directory is: "+ saved_path)
   os.chdir("/Users/LaDulce/Desktop/dev")
   # (2) para cada archivo, cambiar el nombre
   for file_name in file_list:
       os.rename(file_name, file_name.translate(None, "0123456789"))
   os.chdir(saved_path)

remane_files()
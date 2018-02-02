import os

photos_dir = r"/Users/brunonovo/Projects/python/Udemy/Programming-Foundations-with-Python/prank"

def rename_files():
    # (1) Get Files From a Folder
    file_list = os.listdir(photos_dir)
    #print(file_list)

    # Saving The Current Directory
    saved_path = os.getcwd()
    print("Current Working Directory is : {}".format(saved_path))

    # Changing To The Right Folder
    os.chdir(photos_dir)
    print("Now, The Current Working Directory is: {}".format(os.getcwd()))

    # For Each File, Rename Filename
    for file_name in file_list:
        print("Old Name: {}".format(file_name))
        print("New Name: {}".format(file_name.translate(None,"0123456789")))
                # Old Name     # New Name, Without the Numbers
        os.rename(file_name, file_name.translate(None,"0123456789"))
    
    print("Going Back To The Previous Directory...")
    os.chdir(saved_path)

rename_files()
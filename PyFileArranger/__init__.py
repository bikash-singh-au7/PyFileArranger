import os, time
import shutil

class Arrange:
    def arrange(self):
        print("Welcome to Py File Arranger")
        print("[1] Extenssion")
        print("[2] File Modify Date")
        print("[3] File Size")
        print("[4] File Creation Date")
        choice = int(input("Enter Your Choice: "))
        # For Extension
        if choice == 1:
            path = input("Enter Directory: ")
            if(os.path.exists(path)):
                self.arrange_file_with_ext(path)
            else:
                print("Directory Not Exists")
        
        # For Modify Date
        elif choice == 2:
            path = input("Enter Directory: ")
            if(os.path.exists(path)):
                self.arrange_file_with_modification_date(path)
            else:
                print("Directory Not Exists")
        
        # For File Size
        elif choice == 3:
            path = input("Enter Directory: ")
            if(os.path.exists(path)):
                self.arrange_file_with_size(path)
            else:
                print("Directory Not Exists")
        elif choice == 4:
            pass
        else:
            print("Wrong Input !!")

    def make_base_directory(self, path):
        if os.path.exists(path+"/arranged"):
            pass
        else:
            os.mkdir(path+"/arranged")

    def remove_directory(self, path):
        all_dir = os.listdir(path)
        for dir in all_dir:
            rm_dir = path+"/"+dir
            if dir == "arranged":
                pass
            else:
                try:
                    shutil.rmtree(rm_dir)
                except NotADirectoryError:
                    os.unlink(rm_dir)
    

    def move_file(self, src, dest):
        try:
            return shutil.move(src, dest)
        except shutil.Error:
            print("Not Moved !!")

    #=================Arrange According to Modification Date======
    def arrange_file_with_modification_date(self, path):
        self.make_base_directory(path)
        all_files = os.walk(path)
        for dir, fileName, files in all_files:
            for f in files:
                directory = dir+'/'+f
                # print(f, time.ctime(os.path.getmtime(directory)))
                print(f, time.localtime(os.path.getmtime(directory)))
        # Remove all directory except arranged directory
        # self.remove_directory(path)
        # print("Arranged Successfully")

    # ================Arrange According To Size===================
    def arrange_file_with_size(self, path):
        self.make_base_directory(path)
        file_list = []
        all_files = os.walk(path)
        for dir, fileName, files in all_files:
            for f in files:
                directory = dir+'/'+f
                file_list.append(directory)   
        else:
            for file in file_list:
                if os.stat(file).st_size >= 0 and os.stat(file).st_size <= (500*1024):
                    move_dir = path+"/arranged/0kb-500kb"
                    if(os.path.exists(move_dir)):
                        self.move_file(file, move_dir)
                    else:
                        os.mkdir(move_dir)
                        self.move_file(file, move_dir)
                elif os.stat(file).st_size >= (500*1024) and os.stat(file).st_size <= (1024*1024):
                    move_dir = path+"/arranged/500kb-1mb"
                    if(os.path.exists(move_dir)):
                        self.move_file(file, move_dir)
                    else:
                        os.mkdir(move_dir)
                        self.move_file(file, move_dir)
                else:
                    move_dir = path+"/arranged/1mb-larger"
                    if(os.path.exists(move_dir)):
                        self.move_file(file, move_dir)
                    else:
                        os.mkdir(move_dir)
                        self.move_file(file, move_dir)

        # Remove all directory except arranged directory
        self.remove_directory(path)
        print("Arranged Successfully")
    # ================End Section=================================
    
    # ================Arrange According To Extenssion=============
    def make_ext_dir(self, path):
        all_files = os.walk(path)
        for dir, fName, files in all_files:
            for file in files:
                ext = file.split(sep=".")
                directory = path+"/arranged/"+ext[-1]+"_files"
                if os.path.exists(directory):
                    pass
                else:
                    os.mkdir(directory)

    def arrange_file_with_ext(self, path):
        # Create base directory
        self.make_base_directory(path)
        self.make_ext_dir(path)

        all_files = os.walk(path)
        for dir, file_name, files in all_files:
            for f in files:
                directory = dir+'/'+f
                ext = f.split(sep=".")
                try:
                    moving_dir = path+"/arranged/"+ext[-1]+"_files"
                    shutil.move(directory, moving_dir)
                except shutil.Error:
                    print("Not Moved !!")
                    continue
        print("Arranged All Files")

        # Remove empty folders
        self.remove_directory(path)
    # ================End Section=================================
    
a = Arrange()
a.arrange()

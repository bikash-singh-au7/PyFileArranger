import os
import shutil

class Arrange:
    def arrange(self):
        print("Welcome to Py File Arranger")
        print("According To Extenssion [1]")
        print("According To Modify [2]")
        print("According To Size [3]")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            path = input("Enter Directory: ")
            if(os.path.exists(path)):
                self.arrange_file_with_ext(path)
            else:
                print("Directory Not Exists")
        elif choice == 2:
            print("Comming Soon")
        else:
            print("Comming Soon")

    def make_base_directory(self, path):
        if os.path.exists(path+"/arranged"):
            pass
        else:
            os.mkdir(path+"/arranged")

    def make_ext_dir(self, path):
        all_files = os.walk(path)
        for dir, fName, files in all_files:
            for file in files:
                ext = file.split(sep=".")
                directory = path+"/arranged/"+ext[1]+"_files"
                if os.path.exists(directory):
                    pass
                else:
                    os.mkdir(directory)

    def remove_directory(self, path):
        all_dir = os.listdir(path)
        for dir in all_dir:
            rm_dir = path+"/"+dir
            if dir == "arranged":
                pass
            else:
                shutil.rmtree(rm_dir)

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
                    moving_dir = path+"/arranged/"+ext[1]+"_files"
                    shutil.move(directory, moving_dir)
                except shutil.Error:
                    continue
        print("arranged Alll Files")

        # Remove empty folders
        self.remove_directory(path)
        
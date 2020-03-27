# AttainU Project
```
Project Name: Junk File Organizer
Auther: Bikash Kumar Singh
Author Email: bikashsinghak47@gmail.com
```

# PyFileArranger Module
The `PyFileArranger` is a Python Module. This module is helpful for arranging the file within the directory. 
Using this module you can arrange or sort the file in different aspects. You can sort file according to following:

* According to Extenssion
* According to File Modification Date
* According to File Creation date
* And also According to File Size

## How To Install PyFileArranger
You can easily `install` this module using `pip` command

```download
pip install PyFileArranger
```

## How To Use PyFileArranger
You can easily use `PyFileArranger` module to arrange you file. First you need to install this module. After installation follow these steps: 
```
Step-1: Creating a object
a = PyFileArranger.Arrange()

Step-2: Call arrange() method using created object
a.arrange()

Step-3: After that you would see
Welcome To PyFileArranger
[1] Extenssion
[2] File Modify Date
[3] File Size
[4] File Creation Date
Enter Your Choice: 

Step-4: Enter anyone given option number and hit enter key, After that it ask you to about the directory which you want to sort
Enter Directory:

Step-5: After enter the directory again hit enter key and your all file would arranged
```
## Sort Discription About Making PyFileArranger Module
In creating this module I used some predefined python module and lots of methods. All methods are written by me.

### Name of Modules and uses
```
1. os module
2. time module
3. shutil module
```
#### 1. os module:
This module used to read files within the folder, The os module also helpfull to read the file size. Below the list of methods are used to making `PyFileArranger` module
```
i. os.listdir():- To find all the directory name between given directory.
ii. os.walk():- To find all sub directory, filename, and files in given directory
iii. os.path.exists():- To check given directory is exist or not
iv. os.mkdir():- To make the new directory
v. os.stat(file).st_size:- To get file size
vi. os.path.getctime():- To get file creation time
vii. os.path.getmtime():- To get file modification time
```

#### 2. time module:
Using this module I found the time and convert the time into localtime. Below the list of methods of time module that used to making `PyFileArranger` module
```
i. time.localtime():- To convert the time in localtime
```

### Name of Classes and uses
```
1. Arrange
```
#### 1. Arrange Class:
This `Arrange` is used to wrap all the methods and improve the security level 

### Name of Methods and uses
```
1. arrange()
2. make_base_directory(path)
3. make_day_directory(path)
4. remove_directory(path)
5. move_file(src, dest)

6. arrange_file_with_modification_date(path)
7. arrange_file_with_creation_date(path)
8. arrange_file_with_size(path)

9. make_ext_dir(path)
10. arrange_file_with_ext(path):

```

#### 1. arrange():
The `arrange()` method is base method of this module because it works as a navigator. In this method i wrote the user input for both directory any user choise for how to arrange theirs file.

#### 2. make_base_directory(path):
The `make_base_directory(path)` methods is used to create the base directory (arranged). All the sorted or arranged files are stored in this directory.

#### 3. make_day_directory(path):
The `make_day_directory(path)` method is useful when user want to arranged his file according to file creation date or modification date. This method create some directory that is `today` `yesterday` `earlier`

#### 4. remove_directory(path):
This one of the useful method of this module. It helpful to delete the empty directory after moving the files to arranged directory

#### 5. move_file(src, dest):
This method takes two arguments one source and another destination. And it moves the files from soucre to destination directory

#### 6. arrange_file_with_modification_date(path):
It helps to arranged the file according to file modification date. It takes only one argument as a directory path

#### 7. arrange_file_with_creation_date(path):
It helps to arranged the file according to file creation date. It takes only one argument as a directory path

#### 8. arrange_file_with_size(path):
It helps to arranged the file according to file size. It takes only one argument as a directory path

#### 9. make_ext_dir(path):
The `make_ext_dir(path)` method is useful when user want to arranged his file according to file extenssion. This method create some directory in following formate
Format: extenssion_files
Example: txt_files (for .txt extension)
         pdf_files (for .pdf extension)
         
#### 10. arrange_file_with_ext(path):
It helps to arranged the file according to file extenssion. It takes only one argument as a directory path


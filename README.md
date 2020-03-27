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


# Custom-Find-Utility
A simple Linux find utility implemented in python

With no options specified, csfind.pylists the regular files in the specified directory (it skips directories and other non-regular files when present). Note that the full pathnames are shown
```python
raine@pequod:~/Custom-Find-Utility$ ./custom_find.py ./Sample_1
./Sample_1/file2  1  :  file2
./Sample_1/file1  1  :  file1
./Sample_1/output.txt  1  :  output.txt
```
The -nameoption matches file names in the directory against the specified regex pattern and shows the full pathnamesof the matching files found:

raine@pequod:~/Custom-Find-Utility$ ./custom_find.py ./Sample_1/ -name 'file[12]'
./Sample_1/file2  1  :  file2
./Sample_1/file1  1  :  file1

The -grep option matches file contents against the specified pattern and only lists the files with the contents shown for each line the matches:


raine@pequod:~/Custom-Find-Utility$ ./custom_find.py ./Sample_1 -grep '[0-9]+'
./Sample_1/file2  1  :  This is line one of file1
./Sample_1/file2  2  :  welcome to cop4342
./Sample_1/file2  8  :  This is line one of file1
./Sample_1/file2  9  :  welcome to cop4342
./Sample_1/file2  15  :  This is line one of file1
./Sample_1/file2  16  :  welcome to cop4342
./Sample_1/file1  22  :  This is line 22 of this test file, expect 50 lines atmost in any test file for this project
./Sample_1/output.txt  1  :  1,22c1,22
./Sample_1/output.txt  23  :  < This is line 22 of this test file, expect 50 lines atmost in any test file for this project
./Sample_1/output.txt  25  :  > This is line one of file1
./Sample_1/output.txt  26  :  > welcome to cop4342
./Sample_1/output.txt  32  :  > This is line one of file1
./Sample_1/output.txt  33  :  > welcome to cop4342
./Sample_1/output.txt  39  :  > This is line one of file1
./Sample_1/output.txt  40  :  > welcome to cop4342


With both -name and -grep options specified,the matching files and file contents are listed:


raine@pequod:~/Custom-Find-Utility$ ./custom_find.py ./Sample_1 -name 'file[12]' -grep '[0-9]+'
./Sample_1/file2  1  :  This is line one of file1
./Sample_1/file2  2  :  welcome to cop4342
./Sample_1/file2  8  :  This is line one of file1
./Sample_1/file2  9  :  welcome to cop4342
./Sample_1/file2  15  :  This is line one of file1
./Sample_1/file2  16  :  welcome to cop4342
./Sample_1/file1  22  :  This is line 22 of this test file, expect 50 lines atmost in any test file for this project

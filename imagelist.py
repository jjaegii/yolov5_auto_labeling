# python3 imagelist.py 이미지폴더경로

import sys
import glob

if len(sys.argv) != 2:
    print("잘못된 인자")
    sys.exit()

directory_path = sys.argv[1] + "/*"
file_list = glob.glob(directory_path)
print(file_list)
f = open("imagelist.txt", "w")
for i in file_list:
    f.write(i + "\n")
f.close()
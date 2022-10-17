import os
os.chdir('f:\\LocalRepository\\PythonExercises\\split_test\\')

with open('file_for_test.txt') as file_object:
   lines = file_object.readline()

list_accounts = ''
if int(lines)//3 == 0:
   for line in lines:
      list_accounts += line


print(f'{list_accounts}')
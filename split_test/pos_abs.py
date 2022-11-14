import os
os.chdir('f:\\LocalRepository\\PythonExercises\\split_test\\')

with open('file_for_test.txt') as file_object:
   lines = file_object.readline()

for line in lines:
   if line.strip("\n") != "nickname_to_delete":
      f.write(line)


print(f'{list_accounts}')
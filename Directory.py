from pathlib import Path as pt
path = pt("e_commerce")
print(path.exists())
path1 = pt("NewDirectory")
path1.mkdir()  # Creates a new directory
print(path1.exists())
# path1.rmdir()  # Removes directory

path2 = pt()  # Refers to current dir
for file in path2.glob('*.py'):
    print(file)

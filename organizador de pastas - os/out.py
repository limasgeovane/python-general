import os

cwd = os.getcwd()

folder_lists = [i for i in os.listdir(cwd) if os.path.isdir(i)]

for folder in folder_lists:
    path = os.path.join(cwd, folder)

    files = os.listdir(path)
    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(cwd, file)
        os.replace(from_path, to_path)
    os.rmdir(path)
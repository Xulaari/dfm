import os, shutil

print("making backup folder.")

try:
    username = os.getlogin()
except OSError:
    username = os.getenv("USER")

if os.path.exists(f"/home/{username}/dmbackup"):
    shutil.rmtree(f"/home/{username}/dmbackup")

os.mkdir(f"/home/{username}/dmbackup")

print("cloning dot files.")

for file in os.listdir(f"/home/{username}"):
    try:
        if file.startswith(".") and os.path.isdir(f"/home/{username}/{file}"):
            print(f"{file} as a folder")
            shutil.copytree(f"/home/{username}/{file}", f"/home/{username}/dmbackup/{file}")
        elif file.startswith(".") and os.path.isfile(f"/home/{username}/{file}"):
            print(f"{file} as a file")
            shutil.copy(f"/home/{username}/{file}", f"/home/{username}/dmbackup/{file}")
    except shutil.Error as e:
        print(f"an error occured => {e}. continuing")
        pass
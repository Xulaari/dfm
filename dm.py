import sys, os, shutil

if sys.argv[1] == "project":
    status_code = os.system(f"git clone {sys.argv[2]} >/dev/null 2>&1")

    if status_code == 0:
        print(f"Successfully projected {sys.argv[2]}.")
    elif status_code == 32768:
        print(f"{sys.argv[2]} is already projected in your folder.")
elif sys.argv[1] == "backup":
    print("making backup folder.")

    try:
        username = os.getlogin()
    except OSError:
        username = os.getenv("USER")

    if os.path.exists(f"/home/{username}/dmbackup"):
        shutil.rmtree(f"/home/{username}/dmbackup")

    os.mkdir(f"/home/{username}/dmbackup")

    quest = input("do you want to clone just themes or themes and cfgs? (1/2): ")

    print("cloning dot files.")

    try:
        if quest.startswith("1"):
            related_files = [".themes", ".icons"]
            for file in os.listdir(f"/home/{username}"):
                    if file.startswith(".") and os.path.isdir(f"/home/{username}/{file}") and file in related_files:
                        print(f"{file} as a folder")
                        shutil.copytree(f"/home/{username}/{file}", f"/home/{username}/dmbackup/{file}")
                    elif file.startswith(".") and os.path.isfile(f"/home/{username}/{file}") and file in related_files:
                        print(f"{file} as a file")
                        shutil.copy(f"/home/{username}/{file}", f"/home/{username}/dmbackup/{file}")
    
        elif quest.startswith("2"):
            excluded = [".local", ".var"]
            for file in os.listdir(f"/home/{username}"):
                    if file.startswith(".") and os.path.isdir(f"/home/{username}/{file}") and file not in excluded:
                        print(f"{file} as a folder")
                        shutil.copytree(f"/home/{username}/{file}", f"/home/{username}/dmbackup/{file}")
                    elif file.startswith(".") and os.path.isfile(f"/home/{username}/{file}") and file not in excluded:
                        print(f"{file} as a file")
                        shutil.copy(f"/home/{username}/{file}", f"/home/{username}/dmbackup/{file}")
        else:
            exit()
    
    except shutil.Error as e:
        pass

    excluded = [".local", ".var"]
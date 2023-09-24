import sys, os

if sys.argv[1] == "project":
    status_code = os.system(f"git clone {sys.argv[2]} >/dev/null 2>&1")

    if status_code == 0:
        print(f"Successfully projected {sys.argv[2]}.")
    elif status_code == 32768:
        print(f"{sys.argv[2]} is already projected in your folder.")
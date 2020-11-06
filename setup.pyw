import os
import sys
import subprocess


def install_modules():
    try:
        os.system("pip install -r requirements.txt")

    except Exception as e:
        print(e)


def run_tasks():
    try:
        os.system("python tasks.py")

    except Exception as e:
        print(e)


def main():
    install_modules()
    run_tasks()

if __name__ == "__main__":
    main()

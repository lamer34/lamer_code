import os
import sys
import subprocess
import tasks


module_names = tasks.moduls


def import_modules(module_name):

    globals()[module_name] = __import__(module_name)
    print(f"{module_name} imported succesfully!")


def install_modules(module_name):
    try:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', module_name])
        print(f"{module_name} installed succesfully!")

    except Exception as e:
        print(e)


def ready():
    for module_name in module_names:
        try:
            import_modules(module_name)

        except ImportError:
            install_modules(module_name)
            import_modules(module_name)

        except Exception as e:
            print(e)


def main():
    ready()
    tasks.main()


if __name__ == "__main__":
    main()

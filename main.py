import argparse
from pathlib import PosixPath
import subprocess
from typing import Iterator

BASE_PATH = PosixPath("~/.git-switch").expanduser()
GIT_PATH = PosixPath("~/.git-credentials").expanduser()


def get_credentials(name: str) -> str | None:
    try:
        with open(BASE_PATH, "r") as file:
            data = file.read().split()
            for i in data:
                key, value = i.split("=")
                if key == name:
                    return value
    except Exception as ex:
        print(ex)
        return None


def set_credentials_to_git(name: str, token: str) -> None:
    string = f"https://{name}:{token}@github.com"
    with open(GIT_PATH, "w") as file:
        file.write(string)


def get_git_config() -> Iterator:
    r = str(subprocess.check_output(["git", "config", "--list"]))
    for i in r.split("\\n"):
        try:
            key, value = i.split("=")
            yield key, value
        except ValueError:
            continue


def set_account_data():
    current_name, current_email = "name not found", "mail not found"

    for key, value in get_git_config():
        match key, value:
            case "user.name", value:
                current_name = value
            case "user.email", value:
                current_email = value
            case _:
                pass

    print(f"In current repo your credentials: {current_name} <{current_email}>")

    password = get_credentials(current_name) 
    if password:
        try:
            set_credentials_to_git(current_name, password)
        except:
            print("Cannot write credentials in ~/.git-credentials")
        else:
            print(f"New password for {current_name} successfully activated!")
    else:
        print("Password was not found in ~/.git-switch")


if __name__ == "__main__":
   parser = argparse.ArgumentParser("git-switch") 
   args = parser.parse_args()
   
   set_account_data()

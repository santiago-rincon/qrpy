from colorama import Fore
import inquirer
import os
import qrcode
import qrcode.image.svg as svg
import sys
import utils.file_system as fs


def make_qr(text, output, ext):
    fs.output_file_exist(output)
    if ext == '.svg':
        factory = svg.SvgPathImage
        img = qrcode.make(text, image_factory=factory)
    else:
        img = qrcode.make(text)
    img.save(output)
    print(f'\n{Fore.GREEN}QR code saved in: {output}\n')
    sys.exit(0)


def make_qr_interactive():
    print(f'{Fore.BLUE} NOTE: Press Ctrl + C to cancel program execution.')
    questions = [
        [inquirer.Text('text', message='Enter the text to be encoded to QR'),],
        [inquirer.Text(
            'output', message='Enter the folder file path (optional)'),],
        [inquirer.Text(
            'file', message='Enter the name of the output file (optional)'),],
        [inquirer.List(
            'format', message='Select the format (press space key to select)', choices=['.png', '.svg'])]

    ]
    while True:
        temp_answer = inquirer.prompt(questions[0])
        if temp_answer['text'] == '':
            print(f'{Fore.RED}[-] The text cannot be empty')
        else:
            answers = {'text': temp_answer['text']}
            break
    while True:
        temp_answer = inquirer.prompt(questions[1])
        isValid = fs.verify_output_interactive(temp_answer['output'])
        if len(isValid) > 0:
            answers['output'] = isValid
            break
    while True:
        temp_answer = inquirer.prompt(questions[2])
        isValid = fs.verify_file_name(temp_answer['file'])
        if len(isValid) > 0:
            answers['file'] = isValid
            break
    temp_answer = inquirer.prompt(questions[3])
    answers['format'] = temp_answer['format']
    text = answers['text']
    output = os.path.join(
        answers['output'], answers['file'] + answers['format'])
    make_qr(text, output, answers['format'])

from colorama import Fore
from utils.make_qr import make_qr
from utils.make_qr import make_qr_interactive
import click
import sys
import utils.file_system as fs


@click.group()
def cli():
    """
    QRpy is a command line interface (CLI) that uses Python's qrcore library to generate QR codes in png or svg formats.\n
    All available documentation is: https://github.com/santiago-rincon/qrpy\n
    Tool made by: Cristian Santiago Rincón (https://github.com/santiago-rincon)
    """
    pass


@cli.command()
@click.argument('text', type=str)
@click.option('--output', '-o', type=str, default='qr.png', help='Output file path. By default, the file will be saved in the current working directory with the name "qr.png". If the output path contains folders that do not exist, they will be created.  Also, if the output path does not contain the image extension, the file will also be saved as "qr.png".')
def generate(text, output):
    """
    Generate a QR code from a text string.\n
    Examples:\n
    [*] qrpy generate "Hello World" -o qr.png\n
    [*] qrpy generate "Hello World" -o qr.svg\n
    NOTE: the file path can be specified either absolutely or relatively. In addition, the CLI will ignore all paths that do not contain the "png " or "svg " extension. If the output path contains folders that do not exist on the computer, the CLI will create them, and if the output file name is not specified (i.e. the path does not end in ".png" or ".svg" extension) it will be saved as "qr.png".\n
    All available documentation is: https://github.com/santiago-rincon/qrpy\n
    Tool made by: Cristian Santiago Rincón (https://github.com/santiago-rincon)
    """
    qr, ext = fs.build_output_path(output)
    try:
        make_qr(text, qr, ext)
    except Exception as e:
        print(f'{Fore.RED}[-] Failed to generate the QR code\n:{e}')
        sys.exit(1)


@cli.command()
def interactive():
    """
    Generate a QR code interactively.\n
    """
    try:
        make_qr_interactive()
    except Exception as e:
        print(f'{Fore.RED}[-] Failed to generate the QR code\n:{e}')
        sys.exit(1)


if __name__ == '__main__':
    # Running the program
    cli()

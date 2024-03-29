# QRPY

QRPY is a python command line interface (CLI) tool that uses the [qrcode](https://github.com/lincolnloop/python-qrcode) library to to generate QR codes in png or svg formats.

## Installation

To install the CLI you must:

1. Clone the repository

   ```bash
   git clone https://github.com/santiago-rincon/qrpy.git
   cd qrpy
   ```

2. Install the required dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Create QR with parameters

You can generate QR codes with the command `generate` and the text you want to encode as QR. In addition, with the `-o` or `--output` parameter you can specify the path (relative or absolute) where the QR will be saved.

You have the following options when entering the path:

- Do not set the parameter: it will save the file in the current working directory with the name `qr.png`.

  #### Example

  This example generates a QR with the text "Some text" and saves it in the current working directory with the name "qr.png".

  ```shell
  python qrpy.py generate 'Some text'
  ```

- Set the path with the file name: you must specify the path where you want to save the file ending with the name and extension, only `.png` and `.svg` extensions are supported in case of placing another one, it will be replaced with `.png`.

  #### Examples

  - This example generates a QR with the text "Some text" and saves it in the path `/any/folder/` with the name `my_qr.png`.

    ```shell
    python qrpy.py generate 'Some text' -o /any/folder/my_qr.png
    ```

  - This example generates a QR with the text "Some text" and saves it in the path `/any/folder/not/created/` with the name `vect_qr.svg`.

    > Folders that do not exist will be created

    ```shell
    python qrpy.py generate 'Some text' --output /any/folder/not/created/vect_qr.svg
    ```

  - This example generates a QR with the text "Some text" and saves it in the path `/any/folder/` with the name `my_qr.png`.

    > Extension will be changed

    ```shell
    python qrpy.py generate 'Some text' -o /any/folder/my_qr.jpg
    ```

- Set the path with only folders: in case the specified path does not contain a file name with extension, the folders specified in the path will be created (if they do not exist) and the QR will be saved with the name qr.png.
  #### Example
  - This example generates a QR with the text "Some text" and saves it in the path `/only/folders/` with the name `qr.png`.
    > Folders that do not exist will be created
    ```shell
    python qrpy.py generate 'Some text' -o /only/folders
    ```

### Create QR interactively

You can generate QR codes with the command `interactive`. The CLI will ask for the text you want to encode in QR, the folder where you want to save the file, the name you want to give to the file and the extension you want to generate it with.

#### Parameters to be taken into account for each question

- _Enter the text to be encoded to QR_: the text you place cannot be an empty string.
- _Enter the folder file path (optional)_: In this question you have two options, leave it blank (it will save the image in the current working folder) or specify the path, either relative or absolute. **You must only specify the folders**, **NOT** the file name. Remember that the folders you specify that do not exist on your computer were created.
- _Enter the name of the output file (optional)_: In this question you must specify **only the file name**, WITHOUT EXTENSION or SPECIAL CHARACTERS, if you leave it empty it will be saved as qr.
- _Select the format (press space key to select)_: In this question you must choose a file extension.
  > If any question contains an error, the question will be repeated. If you want to cancel the QR generation process press `ctrl + c`

#### Example

```shell
python qrpy.py interactive
```

## Note for Windows

If you want to add the script to the PATH in windows you must add the text string ".py" to the `PATHEXT` environment variable.

With powershell:

```powershell
$env:PATHEXT += ";.py"
```

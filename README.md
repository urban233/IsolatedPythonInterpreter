# IsolatedPythonInterpreter
This project allows you to bundle a Python script into a single binary executable 
using [PyInstaller](https://www.pyinstaller.org/). 
It enables the execution of Python scripts in a self-contained, 
portable environment, with a focus on Windows platforms. 
This makes it easy to distribute Python applications without requiring users to 
install Python or dependencies separately.

## Features
- **Single Binary Output:** Bundle Python scripts into a single executable binary file.
- **Portable:** The resulting binary can be run on machines without needing Python installed.
- **Custom Libraries:** Include additional libraries by adding them to the virtual environment used during the build process.
- **Windows Focused:** Designed primarily for Windows users, but can be adapted for other platforms with appropriate configuration.

## Prerequisites
Before you begin, ensure you have the following installed:

- Python (version > 3.11 recommended)

## Installation
1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/urban233/IsolatedPythonInterpreter.git
   cd IsolatedPythonInterpreter
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv && .\.venv\Scripts\activate && pip install -r requirements.txt
   ```

3. Install PyInstaller with:

   ```bash
   pip install pyinstaller
   ```

## Usage
### Building the Single Binary

1. Ensure you have the required libraries installed in your virtual environment. You can install any necessary libraries using `pip`:

   ```bash
   pip install <library-name>
   ```

2. Use PyInstaller to bundle your Python script into a single executable binary. For example:

   ```bash
   .\scripts\bat\script2exe.bat
   ```

   This will create a `dist/` directory containing the single binary file for your script.

3. The resulting executable can be found in the `dist/` folder. You can now distribute this executable without needing Python installed on the target machine.

### Additional Options

- **Adding External Libraries:** If your Python script requires additional libraries, simply install them in your virtual environment before running the `pyinstaller` command. These libraries will be bundled into the final executable.

- **Customizing the Build:** You can customize the build process using PyInstaller options. For a list of available options, refer to the [PyInstaller Documentation](https://pyinstaller.readthedocs.io/en/stable/).

## Test
To check if the binary is working you can use the `test_launch.bat` in the `scripts` folder.

## Troubleshooting

- **Missing Libraries:** If certain libraries are not included in the final binary, ensure they are installed in the virtual environment before running `pyinstaller`. You can also check PyInstaller's logs for missing dependencies.

- **Antivirus Issues:** Some antivirus software may flag PyInstaller binaries as potential threats due to the way they are packed. This is typically a false positive, but you should test your binary in a controlled environment before distributing it.

## License
This project is licensed under the GNU GPL v3 License – see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [PyInstaller](https://www.pyinstaller.org/) for creating the tool that makes this project possible.
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) for managing isolated environments.

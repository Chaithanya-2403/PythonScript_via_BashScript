import subprocess
import sys

def call_dotnet(args):
    # The path to the .NET 6 app DLL or executable
    dotnet_app_path = '/home/chaithanya/Documents/Python_via_Bash/linux-x64/BashPythonScript.dll'

    # Call the .NET app with arguments
    command = ['dotnet', dotnet_app_path] + args

    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

if __name__ == '__main__':
    # Get arguments passed to the Python script (excluding script name)
    python_args = sys.argv[1:]
    call_dotnet(python_args)

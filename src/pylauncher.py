import os
import argparse


def execute_script(script_path, script_args):
  """Executes the given Python script with arguments."""
  if not os.path.exists(script_path):
    print(f"Error: Script '{script_path}' not found.")
    return

  # Create a global environment for the script
  script_globals = {
    "__name__": "__main__",
    "__file__": script_path,
    "__args__": script_args,
  }

  # Open and execute the script
  with open(script_path, "r") as script_file:
    exec(script_file.read(), script_globals)


def main():
  """Main function to handle CLI input."""
  # Initialize the argument parser
  parser = argparse.ArgumentParser(
    description="pylauncher - A simple script launcher for Python scripts."
  )
  # Define the arguments
  parser.add_argument("script", help="The Python script to run.")
  parser.add_argument(
    "args", nargs=argparse.REMAINDER, help="Arguments to pass to the script."
  )
  # Parse the arguments
  args = parser.parse_args()
  # Call function to execute the script with provided arguments
  execute_script(args.script, args.args)


if __name__ == "__main__":
  main()

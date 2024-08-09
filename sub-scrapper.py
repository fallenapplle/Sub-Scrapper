import argparse
import subprocess
import sys 
import os


RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
CYAN = "\033[0;36m"
END = '\033[0m'
BOLD = "\033[1m"

# Checking the file to read 


# function for file existance....... 
def file_exists_check(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError: 
        print("-----------------------------------------------------")
        print(f"{RED}File name: {BOLD}{filename}{END} {RED}is not readable or does not exist{END}")
        print("-----------------------------------------------------")
        sys.exit(1)


def report_folder_check(folder):
    while os.path.exists(folder):
        print(f"{RED}Folder name {folder} already exists.{END}")
        folder = input(f"{BOLD}Please enter a new folder name:  {END}")
    os.makedirs(folder)
    return folder



def subFinder(filename, folder, verbose=False):


# call this function to check file existance 
    lines = file_exists_check(filename)

   

    
    output_file_path = os.path.join(folder, "subfinder_out.txt")

    
    with open(output_file_path, 'w') as subfinder_output:
        for line in lines:
            domain = line.strip()
            try:
                command = subprocess.run(["subfinder", "-d", domain],  capture_output=True , text=True, check=True)
                subfinder_output.write(command.stdout)
                if verbose:
                    print(f"{GREEN} Subfinder command is success for {YELLOW}{domain}{END}")

            except subprocess.CalledProcessError as e:
                print(f" {RED} subfinder command failed  for {YELLOW}{domain}{END}")
                subfinder_output.write(f"{RED}subfinder command failed on {YELLOW}{domain}{END}")




def amass(filename, folder, verbose=False):




    lines = file_exists_check(filename)

    
    output_file_check = os.path.join(folder, 'amass_output.txt')
    with open(output_file_check, 'w') as amass_output:
        for line in lines:
            domain = line.strip()
            try:
                command = subprocess.run(["amass", "enum","-d",domain], capture_output=True, text=True, check=True)
                amass_output.write(command.stdout)
                if verbose:
                    print(f"{GREEN} Amass command is success for {YELLOW}{domain}{END}")

            except subprocess.CalledProcessError as e:
                print(f" {RED} Amass command failed  for {YELLOW}{domain}{END}")
                amass_output.write(f"{RED}Amass command failed on {YELLOW}{domain}{END}")


            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Specify the file name." )
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    parser.add_argument("-t", "--tool", choices=["subfinder", "amass"], help="Choices of your tools")
    parser.add_argument("-r", "--report-folder", default="Report", help="Specify the report folder name (optional)")
    args = parser.parse_args()
    
    # Use default report folder if not specified
    report_folder = report_folder_check(args.report_folder)


   

    if args.tool:
        if args.tool == "subfinder":
            subFinder(args.filename, report_folder, args.verbose)
        elif args.tool == "amass":
            amass(args.filename, report_folder, args.verbose)
    else:
        subFinder(args.filename, report_folder, args.verbose)
        amass(args.filename, report_folder, args.verbose)

if __name__ == "__main__":
    
    main()


    


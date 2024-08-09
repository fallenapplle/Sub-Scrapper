# Subdomain Enumeration Script

This script is designed to perform subdomain enumeration using the `subfinder` and `amass` tools. It reads a list of domains from a file, runs the selected tool(s) on each domain, and saves the output to a specified report folder.

## Features

- **File Existence Check**: Ensures that the input file exists and is readable before processing.
- **Customizable Report Folder**: Allows specifying a custom report folder. If the folder already exists, the script prompts the user to provide a new name.
- **Tool Selection**: Users can choose between `subfinder` and `amass` tools for subdomain enumeration.


## Prerequisites

- Python 3.+
- `subfinder` and `amass` tools must be installed on your system and accessible via the command line.
- `go language` for installing subfinder `sudo apt install golang`
- `subfinder` 1st tool used for subdomain enumration.
- `amass` 2nd tool used for subdomain enumration.
  

## Installation

1. Download  and setup amass:
   ```
   go install -v github.com/owasp-amass/amass/v4/...@master
   sudo cp ~/go/bin/amass /usr/local/bin
   ```
2. Download and setup subfinder
   ```
   go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
   sudo cp  ~/go/bin  /usr/local/bin
   ```

3. Clone this repository:
   ```bash
   git clone https://github.com/fallenapplle/Sub-Scrapper.git
   cd Sub-Scrapper
   python3 sub-scrapper.py <filename> [-t <tool>] [-r <report-folder>] [-v]
   ```



   
   

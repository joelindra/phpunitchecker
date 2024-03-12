# PHPUnit Checker

**Description:**

PHPUnit Checker is a tool designed to identify instances of PHPUnit on web servers. PHPUnit is a popular testing framework for PHP, but if left accessible on a production server, it can pose a security risk. This tool scans a list of websites to check if the PHPUnit testing framework is exposed at various common paths.

**Features:**
- Multi-threaded scanning for efficient and fast checking.
- Checks for PHPUnit at various common paths used by different web frameworks.
- Generates a results file (`phpunit.txt`) containing URLs where PHPUnit is found.

## Usage

1. Provide a list of websites in a text file.
2. The tool will scan each website for the presence of PHPUnit at predefined paths.
3. Results are displayed in the console and saved to a `phpunit.txt` file in the "results" folder.

```bash
python3 main.py
```

## Requirements
1. Python 3.x
2. Requests library (pip install requests)
3. Colorama library (pip install colorama)

# Simpler Real Estate Workflow

Automatic program designed to help you create leads from phila.gov with initial address.

Program created in Python 3.6

## Features

1. Extract balance due from given address

2. Extract sale date from given address

3. Extract sale price from given address

4. Extract owner from given address

## Requirements

**Software**

**Python >= 3.6**

[Chromedriver](https://chromedriver.chromium.org/)

[Selenium](https://pypi.org/project/selenium/) >= 3.141.0

[pyperclip](https://pypi.org/project/pyperclip/) >= 1.7.0

## Future Updates

Choose real estate website
Choose file format/output

## Setup

Have redata.csv file in the same folder as script/program, the second column in redata.csv must be address you want leads from. Edit '/usr/lib/chromium-browser/chromedriver' to chrome driver location.

Currently saves output info in separate text files because of pyperclip testing.

The program will run until there are no more addresses.


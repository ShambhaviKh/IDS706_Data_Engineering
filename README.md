# IDS706_Data_Engineering
[![Python Template for IDS706](https://github.com/ShambhaviKh/IDS706_Data_Engineering/actions/workflows/main.yml/badge.svg)](https://github.com/ShambhaviKh/IDS706_Data_Engineering/actions/workflows/main.yml)

Data Engineering (Fall'25)

- The project requires a basic understanding of how to create github repository, connect it with VScode, create various files and run it correctly.

  This project includes- 
- A simple Python script hello.py with three functions:
  - say_hello(name) – returns a personalized greeting.
  - add(a, b) – returns the sum of two numbers.
  - sub(a, b) – returns the subtraction of two numbers.
- Unit tests/ edge cases for all functions.
- Makefile for automation.
- requirements.txt for dependency management.
- GitHub Actions workflow for linting and testing.


Note- The hello.py, test_hello.py and requirements file should always be there in your repository. 

There are a couple of steps to be followed, first being the creation of a github account. 

## Create a new Github Repository 

Go to [GitHub](https://github.com) and create a new repository. 
   - Make sure to select "Public" or "Private" based on your preference.
   - Optionally, add a description.  
2. enable the "Add a README file" option.
3. Click on "Create repository".


## Create new files in the repository (using the terminal or manually)
bash
touch Makefile
touch hello.py
touch test_hello.py
touch requirements.txt

## Install Docker for using devcontainer and then setup the environment (install dependencies)

## Create a Makefile
makefile
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	flake8 hello.py

test:
	python -m pytest -vv --cov=hello test_hello.py

clean:
    rm -rf __pycache__ .pytest_cache .coverage

all: install format lint test


## Create a requirements.txt file
text
pylint
flake8
pytest
click
black
pytest-cov

(Once the environment is steady, write your code to your working file- hello.py, add test cases in the test_hello.py)

## Write code

It is simple Python project that demonstrates basic functions such as greeting, addition, and subtraction.

say_hello(name: str) -> str  
  Returns a greeting message for the given name.
sub(a: int, b: int) -> int  
Returns the result of subtracting b from a.
add(a: int, b: int) -> int  
  Returns the sum of two numbers.

## Run Makefile commands as needed: 

make install, make test, make format, make lint, make clean.
- Commit and push your changes to GitHub.
- Enable GitHub Actions for automation/Continuous Integration.


## Create a test file

Add some test cases in it, some edge cases as well.

for eg-
test_hello.py
from hello import say_hello, add, sub

def test_say_hello():
    assert say_hello("Shambhavi") == "Hello, Shambhavi, welcome to Data Engineering Systems (IDS 706)!"

def test_add():
    assert add(5, 5) == 10

def test_sub():
    assert sub(10, 8) == 2

## Run commands locally

1. Run the tests and correct the code if any error faced. 

2. Format the code
bash 
make format

3. Lint the code
bash
make lint

4. Clean up the environment
bash
make clean

## Push your changes via commands! 

## View your repository 

## Enable GitHub Actions

1. Go to your repository on GitHub.
2. Click on the "Actions" tab.
3. Click on "New workflow".
4. Select "Set up a workflow yourself".
5. Create a main.yml
6. Commit and push this file to your repository.
7. GitHub Actions will run automatically on every push or pull request

View the Actions tab 

1. Go to the "Actions" tab in your repository.
2. You should see the workflow running.
3. Click on the latest workflow run to see the details.

##Congratulations!!
You now have a working Python template for Data Engineering Systems with:
-Automated testing
-Linting and formatting
-Continuous Integration via GitHub Actions


##Additional Resources 

- [GitHub Documentation](https://docs.github.com/en)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Installing Python and conda](https://www.practicaldatascience.org/notebooks/PDS_not_yet_in_coursera/00_setup_env/setup_python.html)
- [Setting Up Visual Studio Code](https://www.practicaldatascience.org/notebooks/PDS_not_yet_in_coursera/00_setup_env/setup_vscode.html)
- [GitHub Dev-Container Documentation](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces)
- [Makefile Documentation](https://www.gnu.org/software/make/manual/make.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

##This template provides a structured way to set up a Python project with essential tools for development, testing, and continuous integration. It includes:
- A Makefile for easy command execution.
- A virtual environment setup for dependency management.
- A devcontainer configuration for GitHub Codespaces
- A simple Python script with functions.
- Unit tests to ensure code correctness.
- GitHub Actions for continuous integration to automate linting and testing.
- Github Copilot for AI-assisted coding.

## Acknowledgments
This template was created as part of the Data Engineering Systems (IDS 706) course to help students set up their projects efficiently using modern development practices.   






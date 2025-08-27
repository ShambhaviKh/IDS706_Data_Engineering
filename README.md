# IDS706_Data_Engineering
[![Python Template for IDS706](https://github.com/ShambhaviKh/IDS706_Data_Engineering/actions/workflows/main.yml/badge.svg)](https://github.com/ShambhaviKh/IDS706_Data_Engineering/actions/workflows/main.yml)

Data Engineering (Fall'25)

The project requires a basic understanding of how to create github repository, connect it with VScode, create various files and run it correctly. 

This template provides a structured way to set up a Python project with essential tools for development, testing, and continuous integration. It includes:
- A `Makefile` for easy command execution.
- A virtual environment setup for dependency management.
- A devcontainer configuration for GitHub Codespaces
- A simple Python script with functions.
- Unit tests to ensure code correctness.
- GitHub Actions for continuous integration to automate linting and testing.
- Github Copilot for AI-assisted coding.

note- The hello.py, test_hello.py and requirements file should always be there in your repository. 

There are a couple of steps to be followed, first being the creation of a github account. 
You create a new repository, keep readme file and gitignore and then export it to your local VScode by linking your account and install all dependencies and devcontainer. Once the environment is steady, create the files in your repository, add your code to yor working file- hello.py, add test cases in the test_hello.py and also write what requirements are needed in the requiremnets file. 

It is simple Python project that demonstrates basic functions such as greeting, addition, and subtraction.

Write code

say_hello(name: str) -> str  
  Returns a greeting message for the given name.
sub(a: int, b: int) -> int  
Returns the result of subtracting b from a.
add(a: int, b: int) -> int  
  Returns the sum of two numbers.

Run Makefile commands as needed: 

make install, make test, make format, make lint, make clean.
- Commit and push your changes to GitHub.
- Enable GitHub Actions for automation/Continuous Integration.

Create a test file

Add some test cases in it, some edge cases as well.

Enable GitHub Actions

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

Additional Resources 

- [GitHub Documentation](https://docs.github.com/en)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Installing Python and conda](https://www.practicaldatascience.org/notebooks/PDS_not_yet_in_coursera/00_setup_env/setup_python.html)
- [Setting Up Visual Studio Code](https://www.practicaldatascience.org/notebooks/PDS_not_yet_in_coursera/00_setup_env/setup_vscode.html)
- [GitHub Dev-Container Documentation](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces)
- [Makefile Documentation](https://www.gnu.org/software/make/manual/make.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

You have successfully created a Python template project for Data Engineering Systems (IDS 706) using GitHub and GitHub Actions.





# Python Template for Project
[![Python 3.12](https://img.shields.io/badge/Python-3.12-green.svg)](https://www.python.org/downloads/release/python-390/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

This repository is a my python template to help you get started quickly on a new project.

## How to Use This Template for a New Project

Follow these steps to start a new project based on this template:

1. **Create a New Repository**: First, create a new repository on GitHub. This will be the repository for your new project.

2. **Clone the template to a New Directory**: On your local machine, clone this template repository into a new directory that will become your new project. Then remove the `.git` directory to completely decouple it from the template. Use these commands:

    ```bash
    git clone https://github.com/kaki005/PythonTemplate.git <new-project>
    cd <new-project>
    rm -rf .git
    ```

3. **Setting Up The Local Development Environment**: Install the required python version, set the local python version, create and use a new poetry environment, and install the project dependencies. You can do this with the provided `Makefile` using the following command:

    ```bash
    make install
    ```

4. **Initialize a New Repository**: Then, initialize a new repository in the new directory:

    ```bash
    git init
    ```

5. **Set the Remote of the New Repository**: Set your new GitHub repository as the remote for your new project:

    ```bash
    git remote add origin <url-of-your-new-repository>
    ```

6. **Push to the New Repository**: Stage all files, commit them, and push them to your new repository:

    ```bash
    git add .
    git commit -m ":tada: initial commit"
    git push -u origin main
    ```

By following these steps, you can start a new project based on this starter set.

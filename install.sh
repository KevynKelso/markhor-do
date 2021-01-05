#!/bin/bash

UNAME=$(uname)
HOMEBREW_PATH=$(which brew)
PYTHON_PATH=$(which python3)

function installHomebrew() {
    if [ $HOMEBREW_PATH == "" ]; then
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi

    echo "Homebrew setup complete."
}

function installPython() {
    if [ $PYTHON_PATH == "" ]; then
        if [ $UNAME == "Darwin" ]; then
            installHomebrew
            brew install python
        fi

        if [$UNAME == "Linux" ]; then
            apt-get install python3 pip
        fi
    fi

    echo "Python setup complete."
}

function setUp() {
    installPython

    pipenv --three
    pipenv run pipenv install
    pipenv run pre-commit install

    echo "Environment setup complete."
    echo "Run 'pipenv shell' to enter environment."
}

setUp
exit 0

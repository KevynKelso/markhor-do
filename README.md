# markhor

## Description
Flask server to handle Snipcart webhook requests.

## Install
1. `git clone https://github.com/bscs-science-learning/markhor.git`
2. `cd markhor`
3. `chmod u+x install.sh`
4. `./install.sh`

## Contributing
1. Contact an admin to be added as a contributer.
2. All commit messages should be in the imperative tense (Ex. "Edit files" instead of "Edited files").
3. Checkout a new branch from the master branch.
4. Once you've made changes, push your branch to GitHub: `git push -u origin <branch-name>`
5. In GitHub, open a new pull request from your new branch.
6. Once your pull request is merged by an admin, your branch will be deleted from GitHub.

## Usage
To run in development without Docker:
1. `cd app`
2. `python3 ./non_docker_server.py`

To run in development with Docker:
1. `docker-compose -f .docker/dev/dev.docker-compose.yml down`
2. `docker-compose -f .docker/dev/dev.docker-compose.yml build`
3. `docker-compose -f .docker/dev/dev.docker-compose.yml up`

To run in production with Docker:
1. `ssh-python`
2. `cd /home/bscs/markhor`
3. `git pull`
4. Make sure `.env` is copied into the server at `/home/bscs/markhor/.env`
5. `dcall`

# markhor-do

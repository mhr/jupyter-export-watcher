# Jupyter Export Watcher

## What does it do?
TL;DR: Importing Jupyter notebooks as modules.

This command watches the filesystem (recursively) for changes to *.ipynb files, and when a change occurs, it exports those files to *.py and removes whitespace from the exported versions so they can be imported in Python as modules.

## Is it any good?
Yes.

## Installing Dependencies
- [Node.js](https://nodejs.org/en/)

- [Python](https://www.python.org/)

- [Nodemon](https://github.com/remy/nodemon)

## Running
`$ nodemon ./jupyter_export_watcher/jupyter_export_watcher.js`
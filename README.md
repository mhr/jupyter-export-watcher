# Jupyter Export Watcher

## What does it do?
This command watches the filesystem (recursively) for changes to *.ipynb files, and when a change occurs, it exports those files to *.py and removes whitespace from the exported versions so they can be imported in Python.

## Is it any good?
Yes.

## Installing Dependencies
- Node

https://nodejs.org/en/

- Nodemon

`$ npm install -g nodemon`

## Running
`$ nodemon ./jupyter_export_watcher/jupyter_export_watcher.js`
const { exec } = require("child_process");
const command = `python ./jupyter-export-watcher/jupyter-export-watcher.py`;
const child = exec(command, (error, stdout, stderr) => {
    if (error) {
        console.log(error.message);
    }
    if (stderr) {
        console.log(stderr);
    }
    console.log(stdout);
});

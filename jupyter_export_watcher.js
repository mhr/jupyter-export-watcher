const { exec } = require("child_process");
const command = "python ./jupyter_export_watcher/jupyter_export_watcher.py";
const child = exec(command, (error, stdout, stderr) => {
    if (error) {
        console.log(error.message);
    }
    if (stderr) {
        console.log(stderr);
    }
    console.log(stdout);
});
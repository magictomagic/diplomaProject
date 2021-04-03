const child_process = require('child_process')
const path = require('path')
pythonFile = path.join(__dirname, "first.py")
const pythonProcess = child_process.spawnSync('python', [pythonFile, "data send to python as a param"])

console.log(pythonProcess.stdout.toString())
console.log("Wait until previous process finished")
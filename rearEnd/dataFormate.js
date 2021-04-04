const child_process = require('child_process')
// const {data_test} = require('./data_test')
const path = require('path')

const project_dir = path.dirname(__dirname)
const py_project = 'algorithm'
const py_script = 'filter_middle.py'

const py_scipt_path = path.join(project_dir, py_project, py_script)
// console.log(py_scipt_path)

const judge = (data_test) => {
    to_python = JSON.stringify(data_test)
    const pythonProcess = child_process.spawnSync('python', [py_scipt_path, to_python])
    const raw_receive = pythonProcess.stdout.toString()
    const raw_json = JSON.parse(raw_receive)
    let strategy = {}
    let delete_set = new Set()
    Object.entries(raw_json).forEach(item => {
        let key = item[0]
        const value = item[1]
        key = key.split('|')[0]
        if(value > 4){
            delete_set.add(key)
        }
        strategy[key] = value
    })
    console.log(strategy)
    console.log(delete_set)
    return delete_set
}

module.exports = {judge}
// export {judge}


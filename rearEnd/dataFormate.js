// get raw data from app.js
// package it into formate
// send it to python file
const child_process = require('child_process')
const {data_test} = require('./data_test')
const path = require('path')

const project_dir = path.dirname(__dirname)
const py_project = 'algorithm'
const py_script = 'filter_middle.py'

const py_scipt_path = path.join(project_dir, py_project, py_script)

console.log(py_scipt_path)
// const {json} = require('json')
// give data to python to handle
to_python = JSON.stringify(data_test)
// console.log(to_python)

const pythonProcess = child_process.spawnSync('python', [py_scipt_path, to_python])

console.log(pythonProcess.stdout.toString())


// console.log(to_python)

// user_id = "3456"
// url_id = "3456"
// comment_emoji = "3"
// nickname = "3"
// like_count = "3"
// reply_count = "3"
// be_co_retweet = "3"
// be_co_comments = "3"
// be_co_like = "3"
// author = "3"
// be_contents = "3"
// be_emoji = "3"

// raw_data = Object.entries(data_test)
// raw_data.forEach(item => {
//     f_key = '|'.join([item[0], user_id, url_id])
//     f_value = ''
//     console.log(item)
// })
// console.log(raw_data)

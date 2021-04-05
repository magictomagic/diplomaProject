const child_process = require('child_process')
const redis = require("redis");
const {client, hgetSync, hsetSync, aa} = require("./sync_redis")
// const {data_test} = require('./data_test')
const path = require('path')

const project_dir = path.dirname(__dirname)
const py_project = 'algorithm'
const py_script = 'filter_middle.py'

const py_scipt_path = path.join(project_dir, py_project, py_script)
db_name = 'if_del';
const split_data = async (data_test) => {
    let fish_dragon = Object.keys(data_test)
    let delete_set = new Set()
    let del_store = {}
    for(let i of fish_dragon){
        let jv = await hgetSync(db_name, i)
        if(jv){
            delete_set.add(i)
        }else{
            del_store[i] = data_test[i]
            // console.log(data_test[i])
            // console.log(i)
        }
    }
    console.log(del_store)
    return {
        delete_set,
        del_store
    }
}



const judge1 = async (delete_set, del_store) => { // data_test
    // let fish_dragon = Object.keys(data_test)
    // let delete_set = new Set()
    // let del_store = {}
    // fish_dragon.forEach((item) => {
    //     client.hget(db_name, 'test1', (err, res) => {
    //         if (res) {
    //             delete_set.add(item)
    //         }else{
    //             del_store[item] = data_test[item]
    //         }
    //     });
    // })
    // console.log(fish_dragon)
    // for(let i in fish_dragon){
    //     let jv = 1 // await hgetSync(db_name, i)
    //     if(jv){
    //         delete_set.add(i)
    //     }else{
    //         del_store[i] = data_test[i]
    //     }
    // }


    // fish_dragon.forEach(async (item) => {
    //     let jv = await hgetSync(db_name, item)
    //     // console.log(jv)
    //     if(jv){
    //         delete_set.add(item)
    //     }else{
    //         del_store[item] = data_test[item]
    //         console.log(data_test[item])
    //     }
    // })
    console.log(del_store)
    console.log(delete_set)

    // to_python = JSON.stringify(data_test)
    // const pythonProcess = child_process.spawnSync('python', [py_scipt_path, to_python])
    // const raw_receive = pythonProcess.stdout.toString()
    // const raw_json = JSON.parse(raw_receive)
    // let strategy = {}
    
    // Object.entries(raw_json).forEach(item => {
    //     let key = item[0]
    //     const value = item[1]
    //     key = key.split('|')[0]
    //     if(value > 4){
    //         delete_set.add(key)
    //     }
    //     strategy[key] = value
    // })
    // console.log(strategy)
    // console.log(delete_set)
    // return delete_set
}
// judge(data_test)
const judge = async (data_test) => { // data_test
    let fish_dragon = Object.keys(data_test)
    let delete_set = new Set()
    let del_store = {}
    for(let i of fish_dragon){
        let jv = await hgetSync(db_name, i)
        if(jv && jv > 4){
            delete_set.add(i)
        }else if (!jv){
            del_store[i] = data_test[i]
            // console.log(data_test[i])
            // console.log(i)
        }
    }
    console.log(delete_set.size)
    console.log(delete_set)
    console.log(Object.keys(del_store).length)
    console.log(del_store)
    // return
    if(Object.keys(del_store).length < 3) { // if to change 3 smaller, python threshold should shrink
        // client.quit()
        return delete_set
    }
    console.log('start detecting...')
    to_python = JSON.stringify(del_store)
    const pythonProcess = child_process.spawnSync('python', [py_scipt_path, to_python])
    const raw_receive = pythonProcess.stdout.toString()
    // console.log(raw_receive)
    const raw_json = JSON.parse(raw_receive)
    let strategy = {}
    
    Object.entries(raw_json).forEach(item => {
        let key = item[0]
        const value = item[1]
        key = key.split('|')[0]
        if(value > 4){
            delete_set.add(key)
        }
        strategy[key] = value
        // console.log(key + ' : ' + value)
        client.hset(db_name, key, value)
    })
    console.log('data stored')
    // add to redis
    // client.quit()
    return delete_set
    // console.log(strategy)
    // console.log(delete_set)
    // return delete_set
}
// console.log(judge(data_test));
// let { delete_set, del_store} = split_data(data_test).then(v=>console.log(v))
// split_data(data_test)
// judge(delete_set, del_store)
// console.log(del_store)
// judge(data_test)
module.exports = {judge}
// export {judge}

// client.quit()
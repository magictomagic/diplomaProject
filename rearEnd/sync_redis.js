const redis = require("redis");
const client = redis.createClient();

client.on("error", function(error) {
  console.error(error);
});
// db_name = 'if_del';
// let delete_set = new Set()
// let ss = {}

const hgetSync = (db_name, key) =>{
    return new Promise((resolve, reject)=>{
        client.hget(db_name, key, (err,  res) =>  {
            if(err){
                reject(err)
            }else{
                resolve(res)
            }
        });
    })
}

const hsetSync = (db_name, key, value) => {
    return new Promise((resolve, reject)=>{
        client.hset(db_name, key, value, (err,  res) =>  {
            if(err){
                reject(err)
            }else{
                resolve(res)
            }
        });
    })
}

const aa = () => {
    console.log('aaa')
}

module.exports = {client, hgetSync, hsetSync, aa}

// client.hgetSync('if_del', 'test1')

// async function run(){
//     // let aa = await b(db_name, 'test1')
//     let aa = await hsetSync(db_name, 'test3', '9')
//     console.log(aa)
// }

// run()


// client.quit()



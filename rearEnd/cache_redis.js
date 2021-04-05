const redis = require("redis");
const {client, hgetSync, hsetSync, aa} = require("./sync_redis")

db_name = 'if_del';

let fish_dragon = ['234343324', '32434324543']

async function aaa ()  {
    let delete_set = new Set()
    let ss = {}
    
    fish_dragon.forEach(async (item) => {
        const aa = await hgetSync(db_name, 'test1')
        console.log(aa)
    // client.hget(db_name, item, (err,  res) =>  {
    //     // let aa = await res
    //     if (res) {
    //         delete_set.add(item)
    //     }else{
    //         // del_store[item] = data_test[item]
    //         ss[item] = 'd'
    //         console.log(ss)
    //     }
        
    // });
    // // ss[item] = 'd'
    // // return await 
})
return ss;
}

aaa()
// console.log(ss)
client.quit()





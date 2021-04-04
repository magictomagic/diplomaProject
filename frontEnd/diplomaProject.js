const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}


(async() => {
    'use strict';
    await sleep(6000); // 之后迭代忙等监控网页是否加载出来
    // const jq = document.createElement('script');
    // jq.src = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js";

    // $("div").ready(() => {
        // 监听个屁，setInterval 不断监听
    // })

    let data = Array.from(document.querySelectorAll("[node-type='root_comment']")).map(ele => {
        let commentId = ele.getAttribute("comment_id"),
            text = ele.textContent.trim().substring(0, 127).trim().split('：')[1];
        if(!text && ele.querySelector('div.WB_media_wrap')){
            text = "img";
        }else if(!text){
            text = "";
        }
        return [commentId, text];
    })

    // convert array to Json
    var obj = {};
    data.forEach(ele => obj[ele[0].toString()] = ele[1]);

    let strdata = JSON.stringify(obj);
    console.log(strdata);

    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let rest = xhr.responseText
            console.log(rest)
            console.log(typeof rest)
            const obj_r = JSON.parse(rest)
            // let to_del = rest['td']
            // console.log(typeof to_del)
            // console.log(to_del)
            console.log(obj_r['td'])
        }
    };
    xhr.open('POST', 'http://127.0.0.1:3000/simple-cors')
    xhr.setRequestHeader("Content-type", "application/json")
    xhr.send(strdata)


})()



/**
 * document.querySelectorAll("[node-type='root_comment']")[0].getElementsByClassName("WB_text")[0].lastChild
 * 
 * 
 * document.querySelectorAll("[node-type='root_comment']")[0].getAttribute("comment_id")
 * 
 * 
 * document.querySelectorAll("[node-type='root_comment']")[0]
 * 
 * 
 */
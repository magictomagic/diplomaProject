const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}
//  var script = document.createElement("script");
//     script.src = "https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js";
//     document.getElementsByTagName('head')[0].appendChild(script);

(async() => {
    'use strict';
    let total_len = 0;
    while(true){
        // Do not trigger comment filter while comment number less than 5
        while(document.querySelectorAll("[node-type='root_comment']").length < 5){
            await sleep(500)
        }

        // alert("adasd");
        console.log("start loop");

        total_len = document.querySelectorAll("[node-type='root_comment']").length;

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
        // console.log(strdata);

        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4 && xhr.status === 200) {
                console.log('Getting del data......')
                let rest = xhr.responseText
                // console.log(rest)
                // console.log(typeof rest)
                const obj_r = JSON.parse(rest)
                // console.log(to_del)
                let to_del = obj_r['td']
                // console.log(typeof to_del)
                let to_del_obj = JSON.parse(to_del)
                // console.log(typeof JSON.parse(to_del))
                console.log(to_del_obj)
                let del_list = Object.values(to_del_obj);
                Array.from(document.querySelectorAll("[node-type='root_comment']")).forEach(ele => {
                    let commentId = ele.getAttribute("comment_id");
                    if(del_list.includes(commentId)){
                            let text = ele.textContent.trim().substring(0, 127).trim().split('：')[1];
                            console.log(text)
                            ele.remove()
                        }
                })
                console.log('delete complete');

            }
        };
        xhr.open('POST', 'http://127.0.0.1:3000/simple-cors')
        xhr.setRequestHeader("Content-type", "application/json")
        xhr.send(strdata)
        
        while (document.querySelectorAll("[node-type='root_comment']").length <= total_len) {
            await sleep(500)
        }

        console.log("next loop");
    }
})()
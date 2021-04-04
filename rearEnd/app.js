const express = require('express')
const bodyParser = require('body-parser')
app = express()

port = 3000

const cors = require('cors')
var jsonParser = bodyParser.json()
app.use(bodyParser.urlencoded({ extended: false }))

var corsOptions = {
    origin: 'https://weibo.com',
    optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
}

app.listen(port, () => {
    console.log('port is listening')
})
app.options('*', cors())
    // app.get('/simple-cors', cors(corsOptions), (req, res, next) => { // cors() 允许跨域请求
    //     res.json({ msg: 'This is CORS-enabled for a Single Route' })
    // })

app.post('/simple-cors', jsonParser, cors(), (req, res) => { // cors() 可不加 ？
    res.header('Access-Control-Allow-Origin', req.headers.origin || "*");
    res.header('Access-Control-Allow-Methods', 'GET,POST,PUT,HEAD,DELETE,OPTIONS');
    res.header('Access-Control-Allow-Headers', 'content-Type,x-requested-with');
    console.info("POST /simple-cors");
    let comments = req.body;
    console.log(comments);
    console.log(typeof comments);
    console.log(Object.keys(comments).length);
    res.json({
        text: "Simple CORS requests are working. [POST]"
    })
})
const fs = require('fs')

const rs = fs.createReadStream('./观书有感.txt')

// 绑定data事件
rs.on('data', chunk => {

    console.log(chunk.length);
    console.log(chunk.toString());
})

rs.on('end', () => {
    console.log('文件读取完成');
})

rs.on('error', () => {
    console.log('文件读取失败');
})
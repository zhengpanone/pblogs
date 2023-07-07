const fs = require('fs')
const process = require('process')

// 同步读取写入文件
let data = fs.readFileSync('观书有感.txt')
fs.writeFileSync('./观书有感_copy.txt', data)
console.log(process.memoryUsage());

// 流式读取写入文件
const rs = fs.createReadStream('./观书有感.txt')
const ws = fs.createWriteStream('./观书有感_copy2.txt')
rs.on('data', chunk => {
    ws.write(chunk)
})

rs.on('end', () => {
    console.log('文件读取完成');
    console.log(process.memoryUsage());
})
ws.on('finish', () => {
    console.log('文件写入完成');
})

// 管道写入
rs.pipe(ws)
const fs = require('fs')

// 异步写入
fs.writeFile('./座右铭.txt', '温故而知新，可以为师矣！\n', { flag: 'a' }, err => {
    if (err) {
        console.log('写入失败')
        return
    }
    console.log('写入成功')
})

// 同步写入
fs.writeFileSync('./data.txt', 'text')
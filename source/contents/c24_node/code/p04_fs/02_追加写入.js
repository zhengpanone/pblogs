const fs = require('fs')

fs.appendFile('./座右铭.txt', '学而时习之，不亦说乎？\n有朋自远方来，不亦乐乎？\n人不知而不愠，不亦君子乎？\n', err => {
    if (err) {
        console.log('写入失败')
        return
    }
    console.log('追加写入')
})
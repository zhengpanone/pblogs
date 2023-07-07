const fs = require('fs')

// 文件重命名
fs.rename('./观书有感.txt', './rename_file.txt', err => {
    if (err) {
        console.log('文件重命名失败');
        return
    }
    console.log('文件重命名成功');
})

// 移动
fs.rename('./rename_file.txt', '../观书有感.txt', err => {
    if (err) {
        console.log('文件移动失败');
        return
    }
    console.log('文件移动成功');
})
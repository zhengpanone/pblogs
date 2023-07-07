const fs = require('fs')

// 创建文件夹
// fs.mkdir('./html', err => {
//     if (err) {
//         console.log('创建文件夹失败');
//         return
//     }
//     console.log('创建文件夹成功');
// })

// // 递归创建文件夹
// fs.mkdir('./a/b', { recursive: true }, err => {
//     if (err) {
//         console.log('创建文件夹失败');
//         return
//     }
//     console.log('创建文件夹成功');
// })

// 读取文件夹
fs.readdir('./html', (err, data) => {
    if (err) {
        console.log('读取文件夹失败' + err);
        return
    }
    console.log('读取文件夹成功' + data);
})

// 删除文件夹
fs.rmdir('./html', { recursive: true, force: true }, err => {
    if (err) {
        console.log('删除文件夹失败' + err);
        return
    }
    console.log('删除文件夹成功');
})

// 删除文件夹
fs.rmdir('./html', { recursive: true, force: true }, err => {
    if (err) {
        console.log('删除文件夹失败' + err);
        return
    }
    console.log('删除文件夹成功');
})
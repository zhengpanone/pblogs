const fs = require('fs')

// 文件删除 unlinkSync
fs.unlink('../观书有感.txt', err => {
    if (err) {
        console.log('文件删除失败');
        return
    }
    console.log('文件删除成功');
})
// rm 删除文件 rmSync
fs.rm('./观书有感.txt', err => {
    if (err) {
        console.log('文件删除失败');
        return
    }
    console.log('文件删除成功');
})
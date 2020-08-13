const fs = require("fs")
const _path = require("path")

function getFileByPath(fpath) {
    return new Promise(function (resolve, reject) {
        fs.readFile(fpath, 'utf-8', (err, dataStr) => {
            if (err) return reject(err)
            resolve(dataStr)
        })
    })
}
/***
 * 
 */
getFileByPath("./11.txt")
    .then(function (data) {
        console.log(data)
        return getFileByPath("./2.txt")
    })
    .then(function (data) {
        console.log(data)
        return getFileByPath("./1.txt")
    }).then(function (data) {
        console.log(data)
        //catch的作用，如果前面的任何promise执行失败，则立即终止所有promise的执行，
        //并马上进入catch处理Promise中抛出的异常
    }).catch(function (error) {
        console.log(error.message)
    })

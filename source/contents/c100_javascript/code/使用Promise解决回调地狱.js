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

/**
 * 在上一个.then中返回的新的promise实例，可以继续用下一个.then来处理
 * 如果前面的Promise执行失败，不想后续的Promise操作被终止，可以为每个promise指定失败的回调
 */
getFileByPath("./11.txt")
    .then(function (data) {
        console.log(data)
        return getFileByPath("./2.txt")
    }, function (err) {// 异常处理
        console.log("这个是失败的结果" + err.message)
        return getFileByPath("./1.txt")//重新实例化return一个新的promise
    })
    .then(function (data) {
        console.log(data)
        return getFileByPath("./1.txt")
    }).then(function (data) {
        console.log(data)
    })

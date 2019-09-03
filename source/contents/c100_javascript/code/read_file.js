const fs = require("fs")
const path = require("path")

/*每当new一个promise实例,就会立即执行这个异步操作中的代码
就是说，new的时候，除了能够得到一个promise实例之外，还会立即调用我们的promise构造函数
传递的那个function，执行这个function中的异步操作代码
*/

/* var promise = new Promise(function () {
    fs.readFile(path.join(__dirname, "./1.txt"), "utf-8", (err, dataStr) => {
        if (err) throw err
        console.log(dataStr)
    })
}) */

function getFileByPath(fpath) {
    return new Promise(function (resolve, reject) {
        fs.readFile(path.join(__dirname, fpath), "utf-8", (err, dataStr) => {
            if (err) return reject(err)
            resolve(dataStr)
        })
    })

}

getFileByPath("./1.txt").then(function (data) {
    console.log("success\t" + data)
}, function (err) {
    console.log("failed" + err.message)
})
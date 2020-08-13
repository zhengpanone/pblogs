var options = {
    classname: 'my-class',
    id: 'my-id',
    // 进度条要出现的位置
    target: document.getElementById('myDivId')

};
// 初始化进度条对象
var nanobar = new Nanobar(options);

nanobar.go(30);// 30% 进度条
nanobar.go(76);// 76% 进度条
// 100% 进度条，进度条结束
nanobar.go(100);


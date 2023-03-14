// buffer 与字符串的转换
let buf_1 = Buffer.from([105, 108, 111, 118, 101, 121, 111, 117])
console.log(buf_1.toString()) //iloveyou  默认以utf-8编码进行转换

// []
let buf_2 = Buffer.from('hello')
console.log(buf_2[0]) //104 十进制 
console.log(buf_2[0].toString(2)) //1101000  二进制
buf_2[0] = 95 // 更改buf
console.log(buf_2.toString()) // _ello

// 溢出
let buf_3 = Buffer.from('hello')
buf_3[0] = 361 // 舍弃高位数字 0001 0110 1001 => 0110 1001
console.log(buf_3); // <Buffer 69 65 6c 6c 6f>


// 中文
let buf_4 = Buffer.from('你好');
console.log(buf_4); //<Buffer e4 bd a0 e5 a5 bd>
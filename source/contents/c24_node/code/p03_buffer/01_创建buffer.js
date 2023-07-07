// 1.alloc 创建的内存空间会对内存数据会清空
let buf_1 = Buffer.alloc(10);
console.log(buf_1)

// 2. allocUnsafe 
// 创建的内存空间可能会包含旧的内存数据
// 创建的速度比alloc速度要快些，因为不用对内存数据进行清零操作
let buf_2 = Buffer.allocUnsafe(10);
console.log(buf_2)

// 3. from 
let buf_3 = Buffer.from('hello');
console.log(buf_3)
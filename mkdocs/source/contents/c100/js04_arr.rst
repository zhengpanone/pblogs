========================
100.3 JavaScript 对象
========================

1. 概述
--------------

数组是值的有序集合。每个值叫做元素，每个元素在数组中都有数字位置编号，也就是索引。JS中的数组是弱类型的，数组中可以含有不同类型的元素。数组元素甚至可以是对象或其它数组。

var arr = [1, true, null, undefined, {x : 1}, [1, 2, 3]];

创建数组-字面量
------------------

::

    var BAT = ['Alibaba', 'Tencent', 'Baidu'];
    var students = [{name : 'Bosn', age : 27}, {name : 'Nunnly', age : 3}];
    var arr = ['Nunnly', 'is', 'big', 'keng', 'B', 123, true, null];
    var arrInArr = [[1, 2], [3, 4, 5]];
    var commasArr1 = [1, , 2]; // 1, undefined, 2
    var commasArr2 = [,,]; // undefined * 2

size from 0 to 4,294,967,295(2^23  -1 ) 

new Array
-----------------
::

 var arr = new Array()
 var arrWithLength = new Array(100);    undefined*100
 var arrLikeLiteral = new Array(true,false,null,1,2,"hi");  
 //等价于 [true,false,null,1,2,"hi"];




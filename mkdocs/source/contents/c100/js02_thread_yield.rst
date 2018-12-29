========================
100.1 JavaScript 语句
========================

1. 语句
--------------

|image1|

block

|image2| |image3| |image4|

var 

::

 var a =1;
 var a = b = 1;
 var a =1,b = 1;
 function foo(){
    var a = b =1;
 }
 foo();
 console.log(typeof a); //undefined;
 console.log(typeof b); //number


try catch

::

 try{
    throw "test"
 }catch(ex){
    console.log(ex); //test
 }finally{
    console.log('finally');
 }

|image5|










.. |image1| image:: ./img/20181229102908.png
.. |image2| image:: ./img/20181229103055.png
.. |image3| image:: ./img/20181229103244.png
.. |image4| image:: ./img/20181229103345.png
.. |image5| image:: ./img/20181229104146.png
.. |image6| image:: ./img/
.. |image7| image:: ./img/
.. |image8| image:: ./img/
.. |image9| image:: ./img/
.. |image10| image:: ./img/
.. |image11| image:: ./img/
.. |image12| image:: ./img/

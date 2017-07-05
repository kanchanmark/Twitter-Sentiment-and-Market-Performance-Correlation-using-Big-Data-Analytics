$(document).ready(function(){
    var data=[];
    $('.table tr td:nth-child(5)').each(function(index){data[index]=$(this).text()});
    console.log(data)
});
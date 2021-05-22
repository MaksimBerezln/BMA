var obj = {
  className:'open menu'
}
function removeClass(obj,cls){
  var arr= obj.className.split('');
  for ( i=0; i<arr.length; i++){
    if(arr[i]=== cls){
      delete arr[i];
    }
  }
  return arr.join('');
}
alert(removeClass(obj,'menu'))

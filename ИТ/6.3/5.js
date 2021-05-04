let str = 'мой номер телефона 8-952-587-47-71'
function ucFirst(str) {
  if (!str) return str;

  return str[0].toUpperCase() + str.slice(1);
}

alert( ucFirst(str) );

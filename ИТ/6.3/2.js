let str = 'Выполнение лабораторной работы';

let regexp = /\W+/y;
regexp.lastIndex = 15;
alert( regexp.exec(str) );

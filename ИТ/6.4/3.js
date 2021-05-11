let login = prompt('Введите login','');
var message = (login == 'Вася')? "Привет":
(login == 'Директор')? "Здравствуйте":
(login == '')? "Нет логина": '';
alert(message)

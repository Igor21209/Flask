# Постановка задачи
В рамках лабораорной работы требуется написать программу со следующим функционалом:
1. При запуске программа должна вывести приветственную страницу с предложением увидеть список пользователей
2. Пользователи выводятся в формате "имя фамилия" и представляют собой ссылку на полную информацию о себе
3. При переходе по ссылке должна выводится полная информация о пользователе (фамилия, имя, возраст)

# Алгоритм программы
Программа состоит из 4-х файлов: 1 файл Python (main.py) и 3 html-шаблона (main.html, info.html, user.html). Разберем функционал и назначение каждого из них более подробно.

## Файл main.py
В начале программы мы подключаем необходимые для работы библиотеки: Flask, redirect и render_template. Flask необходим для создания нашего локального сервера, а redirect и render_template — для взаимодействия с html-шаблоанми.

Следующим шагом создаем экземпляр класса Flask — "app", с помощью которого запустим наш сервер при помощи команды app.run().

Далее задаем произвольный список пользовтелей в виде списка словарей. В нашем случае в "базе данных" находится 3 пользователя со следующей информацией о себе: фамилия, имя, возраст, id.

На следующем этапе создается группа декораторов, функции которых мы и рассмотрим.
1. Декоратор route('/') — вызывает функцию hello_world(), которая возвращает html-шаблон "main.html"
2. Декоратор route('/users') — вызывается через html-шаблон "main.html". Запускает функцию users(), возвращающую html-шаблон "user.html" и передающую ему переменную "а", содержащую список словарей, созданный в начале программы
3. Декоратор route('/info/<id>') — вызывается через html-шаблон "user.html". Запускает функцию info(id), которая возвращает html-шаблон "info.html" и передает ему словарь с тем пользователем, который был вызван через html-шаблон "user.html"

## Файл main.html
Данный шаблон вызывается функцией hello_world(). Содержит заголовок и ссылку на декоратор route('/users'). 

## Файл user.html
Данный шаблон вызывается функцией users(). Получает на вход список словарей с пользователями. Содержит заголовок и цикл for для вывода фамилии и имени каждого пользователя на экран в виде ссылок, ведущих на декоратор route('/info/<id>'), где <id> принимает значения <id> пользователя из списка. Также содержит ссылку перехода на предыдущую страницу.

## Файл штащ.html
Данный шаблон вызывается функцией info(id). Получает на вход id пользователя, информацию о котором необходимо вывести. Содержит заголовок и строку с полной информацией о выбранном ранее пользователе. Содержит ссылку перехода на гдавную страницу.

# Вывод
В результате лабораторной работы написана программа на языке Python с использованием фреймворка Flask и html-шаблонов.

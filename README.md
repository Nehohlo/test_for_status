# ЗАДАНИЕ
Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.

Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
- getAll() - Должен возвращать изначальный массив элементов.
- getItem(id) - Принимает id элемента и возвращает сам объект элемента;
- getChildren(id) - Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента, 
чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
- getAllParents(id) - Принимает id элемента и возвращает массив из цепочки родительских элементов, 
начиная от самого элемента, чей id был передан в аргументе и до корневого элемента, 
т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

### Решение

Реализация класса находится в файле TreeStore.py.
Для запуска тестов производительности необходимо запустить файл test.py.

#### Результат тестирования
Результат для изначального древа элементов
```
Метод - getAll()
Вывод - [{'id': 1, 'parent': 'root'}, {'id': 2, 'parent': 1, 'type': 'test'}, 
         {'id': 3, 'parent': 1, 'type': 'test'}, {'id': 4, 'parent': 2, 'type': 'test'}, 
         {'id': 5, 'parent': 2, 'type': 'test'}, {'id': 6, 'parent': 2, 'type': 'test'}, 
         {'id': 7, 'parent': 4, 'type': None}, {'id': 8, 'parent': 4, 'type': None}]
Время - 6.999995093792677e-06

Метод - getItem(7)
Вывод - {'id': 7, 'parent': 4, 'type': None}
Время - 2.7999922167509794e-06

Метод - getChildren(4)
Вывод - [{'id': 7, 'parent': 4, 'type': None}, {'id': 8, 'parent': 4, 'type': None}]
Время - 4.6000059228390455e-06

Метод - getChildren(5)
Вывод - []
Время - 1.400010660290718e-06

Метод - getAllParents(8)
Вывод - [{'id': 8, 'parent': 4, 'type': None}, {'id': 4, 'parent': 2, 'type': 'test'}, 
         {'id': 2, 'parent': 1, 'type': 'test'}, {'id': 1, 'parent': 'root'}]
Время - 2.2999884095042944e-06
```

Результат для древа из 10_000_000 элементов

```
Метод - getAll()
Время - 0.44068259999039583

Метод - getItem(4788089)
Время - 0.0005099000118207186

Метод - getChildren(5091859)
Время - 4.7000066842883825e-06

Метод - getChildren(2914456)
Время - 1.200009137392044e-06

Метод - getAllParents(9999999)
Время - 0.004260199988493696
```
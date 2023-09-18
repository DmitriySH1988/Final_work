# Итоговая контрольная работа по блоку специализация
___
## **Pet-management-system**
___
*Информация о проекте*

### Необходимо организовать систему учета для питомника в котором живут домашние и вьючные животные.

*Как сдавать проект*

Для сдачи проекта необходимо создать отдельный общедоступный
репозиторий(Github, gitlub, или Bitbucket). Разработку вести в этом
репозитории, использовать пул реквесты на изменения. Программа должна
запускаться и работать, ошибок при выполнении программы быть не должно.
Программа, может использоваться в различных системах, поэтому необходимо
разработать класс в виде конструктора
### Задание
1. Используя команду cat в терминале операционной системы Linux, создать
   два файла Домашние животные (заполнив файл собаками, кошками,
   хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
   ослы), а затем объединить их. Просмотреть содержимое созданного файла.
   Переименовать файл, дав ему новое имя (Друзья человека).

   ![Task 1](https://github.com/pashtetrus33/pet-management-system/blob/main/Task%201.png)

2. Создать директорию, переместить файл туда.

![Task 2](https://github.com/pashtetrus33/pet-management-system/blob/main/Task%202.png)

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет из этого репозитория.

![Task 3a](https://github.com/pashtetrus33/pet-management-system/blob/main/Task%203a.png)
![Task 3b](https://github.com/pashtetrus33/pet-management-system/blob/main/Task%203b.png)

4. Установить и удалить deb-пакет с помощью dpkg.
   
![Task 4](https://github.com/pashtetrus33/pet-management-system/blob/main/Task%204.png)

5. Выложить [историю команд](https://github.com/pashtetrus33/pet-management-system/blob/main/TerminalCommands.md) в терминале ubuntu


6. Нарисовать [диаграмму](https://github.com/pashtetrus33/pet-management-system/blob/main/diagram.drawio), в которой есть класс родительский класс, домашние
   животные и вьючные животные, в составы которых в случае домашних
   животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
   войдут: Лошади, верблюды и ослы).

![Task 6](https://github.com/pashtetrus33/pet-management-system/blob/main/Task%206.png)

7. В подключенном MySQL репозитории создать базу данных “Друзья человека”

``` mysql 
CREATE DATABASE mans_friends; 
```

8. Создать таблицы с иерархией из диаграммы в БД
```mysql
USE mans_friends;

CREATE TABLE animals
(
	Id INT AUTO_INCREMENT PRIMARY KEY,  
	Animal_class VARCHAR(50)
);

INSERT INTO animals (Animal_class)
VALUES ('pets'),
('pack animals');  

CREATE TABLE pets
(
	Id INT AUTO_INCREMENT PRIMARY KEY,
    Pet_class VARCHAR (50),
    Animal_id INT,
    FOREIGN KEY (Animal_id) REFERENCES animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO pets (Pet_class, Animal_id)
VALUES ('Dog', 1),
('Cat', 1),  
('Hamster', 1); 

CREATE TABLE pack_animals
(
	Id INT AUTO_INCREMENT PRIMARY KEY,
    Pack_animal_class VARCHAR (50),
    Animal_id INT,
    FOREIGN KEY (Animal_id) REFERENCES animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO pack_animals (Pack_animal_class, Animal_id)
VALUES ('Horse', 2),
('Camel', 2),  
('Donkey', 2); 
    

CREATE TABLE dogs
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(50), 
    Birthday DATE,
    Commands VARCHAR(50),
    Pet_id int,
    Foreign KEY (Pet_id) REFERENCES pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE cats
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(50), 
    Birthday DATE,
    Commands VARCHAR(50),
    Pet_id int,
    Foreign KEY (Pet_id) REFERENCES pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE hamsters
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(50), 
    Birthday DATE,
    Commands VARCHAR(50),
    Pet_id int,
    Foreign KEY (Pet_id) REFERENCES pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE horses
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(50), 
    Birthday DATE,
    Commands VARCHAR(50),
    Pack_animal_id int,
    Foreign KEY (Pack_animal_id) REFERENCES pack_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE camels
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(50), 
    Birthday DATE,
    Commands VARCHAR(50),
    Pack_animal_id int,
    Foreign KEY (Pack_animal_id) REFERENCES pack_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE donkeys
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(50), 
    Birthday DATE,
    Commands VARCHAR(50),
    Pack_animal_id int,
    Foreign KEY (Pack_animal_id) REFERENCES pack_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
```

9. Заполнить низкоуровневые таблицы именами(животных), командами которые они выполняют и датами рождения
```mysql
INSERT INTO dogs (Name, Birthday, Commands, Pet_id)
VALUES ('Рэкс', '2022-11-21', 'фас, дай лапу, cидеть, голос', 1),
('Барбос', '2018-03-05', 'лежать, ко мне', 1),  
('Альма', '2019-06-19', 'сидеть, лежать, лапу, след', 1);

INSERT INTO cats (Name, Birthday, Commands, Pet_id)
VALUES ('Муся', '2015-09-04', 'Муся', 2),
('Лея', '2020-10-22', "Лея, брысь", 2),  
('Кисель', '2020-03-03', NULL, 2); 

INSERT INTO hamsters (Name, Birthday, Commands, Pet_id)
VALUES ('Буся', '2020-03-15', NULL, 3),
('Люся', '2022-08-12', "Люся", 3),  
('Зина', '2023-01-11', NULL, 3);

INSERT INTO horses (Name, Birthday, Commands, Pack_animal_id)
VALUES ('Зорька', '2018-11-01', 'рысь, хоп, шагом, тихо', 1),
('Гром', '2019-06-19', 'хоп, тише', 1),  
('Ветер', '2023-02-22', 'шагом, тише', 1); 

INSERT INTO camels (Name, Birthday, Commands, Pack_animal_id)
VALUES ('Вася', '2021-12-16', NULL, 2),
('Рокки', '2017-06-02', 'Рокки', 2),  
('Патрик', '2013-02-22', 'Патрик ко мне', 2);

INSERT INTO donkeys (Name, Birthday, Commands, Pack_animal_id)
VALUES ('Иа', '2016-04-30', NULL, 3),
('Смелый', '2021-09-22', 'Cмелый ко мне', 3),  
('Семен', '2019-01-18', 'шагом, Семен', 3);
```
10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.
    
```mysql
SET SQL_SAFE_UPDATES = 0;
DELETE FROM camels;

SELECT Name, Birthday, Commands FROM horses
UNION ALL SELECT  Name, Birthday, Commands FROM donkeys;
```

11. Создать новую таблицу “молодые животные” в которую попадут все
    животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
    до месяца подсчитать возраст животных в новой таблице.
```mysql    
CREATE TEMPORARY TABLE all_animals AS
    SELECT *, 'Собаки' as class FROM dogs
    UNION SELECT *, 'Кошки' AS class FROM cats
    UNION SELECT *, 'Хомяки' AS class FROM hamsters
    UNION SELECT *, 'Лошади' AS class FROM horses
    UNION SELECT *, 'Ослы' AS class FROM donkeys;

CREATE TABLE young_animals AS
SELECT Name, Birthday, Commands, class, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age_in_month
FROM all_animals WHERE Birthday BETWEEN ADDDATE(curdate(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);
```
12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
    прошлую принадлежность к старым таблицам.
```mysql
SELECT h.Name, h.Birthday, h.Commands, pa.Pack_animal_class, ya.Age_in_month 
FROM horses h
LEFT JOIN young_animals ya ON ya.Name = h.Name
LEFT JOIN pack_animals pa ON pa.Id = h.Pack_animal_id
UNION 
SELECT d.Name, d.Birthday, d.Commands, pa.Pack_animal_class, ya.Age_in_month 
FROM donkeys d 
LEFT JOIN young_animals ya ON ya.Name = d.Name
LEFT JOIN pack_animals pa ON pa.Id = d.Pack_animal_id
UNION
SELECT c.Name, c.Birthday, c.Commands, p.Pet_class, ya.Age_in_month 
FROM cats c
LEFT JOIN young_animals ya ON ya.Name = c.Name
LEFT JOIN pets p ON p.Id = c.Pet_id
UNION
SELECT d.Name, d.Birthday, d.Commands, p.Pet_class, ya.Age_in_month 
FROM dogs d
LEFT JOIN young_animals ya ON ya.Name = d.Name
LEFT JOIN pets p ON p.Id = d.Pet_id
UNION
SELECT hm.Name, hm.Birthday, hm.Commands, p.Pet_class, ya.Age_in_month 
FROM hamsters hm
LEFT JOIN young_animals ya ON ya.Name = hm.Name
LEFT JOIN pets p ON p.Id = hm.Pet_id;
```
13. [Создать класс с Инкапсуляцией методов и наследованием по диаграмме.](https://github.com/pashtetrus33/pet-management-system/tree/main/src/models)
14. Написать программу, имитирующую работу реестра домашних животных.

   В программе должен быть реализован следующий функционал:

   14.1 Завести новое животное

   14.2 определять животное в правильный класс

   14.3 увидеть список команд, которое выполняет животное

   14.4 обучить животное новым командам

   14.5 Реализовать навигацию по меню 

15. Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆ значение внутренней̆ int переменной̆на 1
при нажатие “Завести новое животное” Сделайте так, чтобы с объектом такого типа можно было работать в 
блоке try-with-resources. Нужно бросить исключение, если работа с объектом типа счетчик 
была не в ресурсном try и/или ресурс остался открыт. Значение считать в ресурсе try, если при заведения животного заполнены все поля.
#   F i n a l _ w o r k  
 
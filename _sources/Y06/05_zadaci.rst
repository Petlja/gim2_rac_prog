
Задаци - филтрирање и претраживање
----------------------------------

Задатак 1.
''''''''''''''''''''''

Нутритивни подаци за одређене рибе и морске плодове су дати у следећој табели:

.. code-block:: text

                Енергетска   Угљени
   Намирница    вредност     хидрати   Беланчевине  Масти
   (100г)       (kcal)       (г)       (г)          (г)
   Туна           116         0        26.0         1.0
   Ослић           88         0        17.2         0.8
   Пастрмка       119         0        18.0         5.0
   Лосос          116         0        20.0         3.5
   Скуша          205         0        19.0        14.0
   Сардине        135         0        18.0         5.0
   Харинга        158         0        18.0         9.0
   Бакалар         82         0        18.0         0.7
   Сом             95         0        16.4         2.8
   Шаран          127         0        17.6         5.6
   Орада          115         0        16.5         5.5
   Јегуља         184         0        18.4        11.7
   Шкампи         106         1        20.0         2.0
   Дагње           86         4        12.0         2.0
   Козице          71         1        13.0         1.0
   Лигње           92         3        15.6         1.3
   Хоботница       81         0        16.4         0.9
   Јастог         112         0        20.0         1.5
  
Из ове табеле издвој оне намирнице које не садрже угљене хидрате и имају мање од 10 г масти на 100 г намирнице.

.. activecode:: primer6-Z1

   morski_plodovi = [
      ["Туна", 116, 0, 26, 1],
      ["Ослић", 88, 0, 17.2, 0.8],
      ["Пастрмка", 119, 0, 18, 5],
      ["Лосос", 116, 0, 20, 3.5],
      ["Скуша", 205, 0, 19, 14],
      ["Сардине", 135, 0, 18, 5],
      ["Харинга", 158, 0, 18, 9],
      ["Бакалар", 82, 0, 18, 0.7],
      ["Сом", 95, 0, 16.4, 2.8],
      ["Шаран", 127, 0, 17.6, 5.6],
      ["Орада", 115, 0, 16.5, 5.5],
      ["Јегуља", 184, 0, 18.4, 11.7],
      ["Шкампи", 106, 1, 20, 2],
      ["Дагње", 86, 4, 12, 2],
      ["Козице", 71, 1, 13, 1],
      ["Лигње", 92, 3, 15.6, 1.3],
      ["Хоботница", 81, 0, 16.4, 0.9],
      ["Јастог", 112, 0, 20, 1.5]]

   print(???)

Задатак 2.
''''''''''''''''''''''

Ученици једног разреда су скакали удаљ. Сваки ученик је скакао три пута и резултати су дати у низу испод.
Издвој из табеле оне редове који садрже имена ученика који су начинили бар један преступ. Преступ је у табели означен тако што је
дужина одговарајућег скока постављена на 0.

.. activecode:: primer6-Z2

   takmicari = [["Алексић Алекса", 4.25, 4.31, 4.22],
                ["Бранковић Бранко", 3.89, 4.02, 4.05],
                ["Вуковић Вук", 0, 3.91, 4.1],
                ["Гавриловић Гаврило", 3.78, 3.26, 3.11],
                ["Дејановић Дејан", 4.56, 4.31, 4.27],
                ["Ђорђевић Ђорђе", 4.63, 4.6, 4.52],
                ["Жарковић Жарко", 3.47, 3.51, 3.58],
                ["Зорић Зоран", 4.12, 4.15, 4.09],
                ["Ивановић Иван", 3.91, 3.26, 0],
                ["Јовановић Јован", 4.01, 4.1, 4.12],
                ["Костић Коста", 3.51, 3.72, 3.41],
                ["Лукић Лука", 2.15, 2.17, 2.18],
                ["Марковић Марко", 3.39, 0, 3.26],
                ["Ненадовић Ненад", 4.25, 4.18, 4.22],
                ["Огњановић Огњен", 4.31, 4.26, 4.12],
                ["Петровић Петар", 4.23, 4.34, 4.34],
                ["Ракић Рака", 3.51, 3.54, 3.62],
                ["Станојевић Станоје", 4.57, 4.59, 4.63]]

   print(???)

Задатак 3.
''''''''''''''''''''''

У низу испод се налазе подаци о неколико ученика. За сваког ученика су наведени његово презиме, име, ЈМБГ, пол,
разред који похађа и просек на крају тог разреда. Допуни print наредбе тако да добијеш податке који су наведени у коментару
изнад print наредбе.

.. activecode:: primer6-Z3
   :includesrc: _src/P06/Zad_ucenici.py

.. infonote::

   Реши задатак и у Пајтон окружењу!
   
   Покрени *IDLE*, из фолдера ``P06`` учитај датотеку ``Zad_ucenici.py`` и ту реши задатак.



Задатак 4.
''''''''''''''''''''''

Написати функцију ``nadji_sve(x, L)`` која враћа низ са позицијама свих појављивања елемента ``x`` у низу ``L``.

.. activecode:: primer6-Z4
   :includesrc: _src/P06/Nadji_sve.py

.. infonote::

   Реши задатак и у Пајтон окружењу!
   
   Покрени *IDLE*, из фолдера ``P06`` учитај датотеку ``Nadji_sve.py`` и ту реши задатак.

Задатак 5.
''''''''''''''''''''''

Написати Пајтон функцију ``presek(L, M)`` која враћа низ свих елемената који се јављају и у низу ``L`` и у низу ``M``.

.. activecode:: primer6-Z5
   :includesrc: _src/P06/Presek.py

.. infonote::

   Реши задатак и у Пајтон окружењу!
   
   Покрени *IDLE*, из фолдера ``P06`` учитај датотеку ``Presek.py`` и ту реши задатак.

Задатак 6.
''''''''''''''''''''''

Написати Пајтон функцију ``razlika(L, M)`` која враћа низ свих елемената
који се јављају у првом од ова два низа, а не јављају се у другом.

.. activecode:: primer6-Z6
   :includesrc: _src/P06/Razlika.py

.. infonote::

   Реши задатак и у Пајтон окружењу!
   
   Покрени *IDLE*, из фолдера ``P06`` учитај датотеку ``Razlika.py`` и ту реши задатак.


Задатак 7*.
''''''''''''''''''''''

(Задатак реши у *IDLE* окружењу)
Написати програм који од корисника учитава природан број :math:`n`, потом :math:`n` реалних бројева (сваки у новом реду) и онда
проверава да ли међу учитаним бројевима има једнаких. Ако је то случај, програм треба да испише „IMA JEDNAKIH“,
а у супротном треба да испише „SVI RAZLICITI“.

Задатак 8*.
''''''''''''''''''''''

(Задатак реши у *IDLE* окружењу)
Написати програм који од корисника учитава природан број :math:`n`, потом :math:`n` реалних бројева (сваки у новом реду)
за које се зна да су сви различити (и то не треба проверавати!) и онда проверава да ли међу учитаних :math:`n` реалних бројева
постоје три чији је збир нула.

Задатак 9*.
''''''''''''''''''''''

(Задатак реши у *IDLE* окружењу)
Написати програм који од корисника учитава природан број :math:`n`, потом :math:`n` реалних бројева (сваки у новом реду)
и онда исписује учитане бројеве „по популарности“: прво испише број који се највише пута појавио у низу, потом
испише следећег „по популарност“, све до оног који се најмањи број пута појавио у низу.


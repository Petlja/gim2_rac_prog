Квиз
======

Питање 1.
~~~~~~~~~~~~~~

.. mchoice:: Тест5_Питање1
   :answer_a: [5, 1, 6, 2, 3, 0], тј. ништа се неће променити.
   :answer_b: [0, 1, 2, 3, 5, 6], тј. елементи низа ће бити поређани од мањих ка већим вредностима.
   :answer_c: [6, 5, 3, 2, 1, 0], тј. елементи низа ће бити поређани од већих ка мањим вредностима.
   :answer_d: Систем ће пријавити грешку јер функција sort захтева додатни аргумент.
   :correct: b
   :feedback_a: Пробај поново! (Функција sort сортира низ!)
   :feedback_b: Тачно!
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново!

   Како ће изгледати низ ``L`` након извршења следећег програмчића:

   .. code-block:: python

      L = [5, 1, 6, 2, 3, 0]
      L.sort()

Питање 2.
~~~~~~~~~~~~~~

.. mchoice:: Тест5_Питање2
   :answer_a: [5, 1, 6, 2, 3, 0], тј. ништа се неће променити.
   :answer_b: [0, 1, 2, 3, 5, 6], тј. елементи низа ће бити поређани од мањих ка већим вредностима.
   :answer_c: [6, 5, 3, 2, 1, 0], тј. елементи низа ће бити поређани од већих ка мањим вредностима.
   :answer_d: Систем ће пријавити грешку јер функција sort не сме да садржи додатни аргумент.
   :correct: c
   :feedback_a: Пробај поново! (Функција sort сортира низ!)
   :feedback_b: Пробај поново! (Енглеска реч reverse значи "обрни")
   :feedback_c: Тачно!
   :feedback_d: Пробај поново!

   Како ће изгледати низ ``L`` након извршења следећег програмчића:

   .. code-block:: python

      L = [5, 1, 6, 2, 3, 0]
      L.sort(reverse=True)

Питање 3.
~~~~~~~~~~~~~~

.. mchoice:: Тест5_Питање3
   :answer_a: ["Ана", "Боки", "Цеца", "Деки"]
   :answer_b: ["Деки", "Цеца", "Боки", "Ана"]
   :answer_c: ["Цеца", "Деки", "Боки", "Ана"]
   :answer_d: Систем ће пријавити грешку јер функција sort не може да сортира низове стрингова.
   :correct: c
   :feedback_a: Пробај поново! (Енглеска реч reverse значи "обрни")
   :feedback_b: Пробај поново! (Имена су написана ћирилицом!)
   :feedback_c: Тачно!
   :feedback_d: Пробај поново!

   Како ће изгледати низ ``L`` након извршења следећег програмчића:

   .. code-block:: python

      L = ["Ана", "Боки", "Цеца", "Деки"]
      L.sort(reverse=True)

Питање 4.
~~~~~~~~~~~~~~

.. mchoice:: Тест5_Питање4
   :answer_a: [6, 5, 4, 1, 2, 3]
   :answer_b: [1, 5, 4, 6, 2, 3]
   :answer_c: [5, 4, 1, 2, 3, 6]
   :answer_d: [1, 2, 3, 4, 5, 6]
   :correct: b
   :feedback_a: Пробај поново!
   :feedback_b: Тачно!
   :feedback_c: Пробај поново! (Ово није бабл-сорт!)
   :feedback_d: Пробај поново! (Примени се само први корак!)

   Како изгледа следећи низ

   .. code-block:: text
   
      L = [6, 5, 4, 1, 2, 3]
   
   након што се на њега примени **само први корак** алгоритма за сортирање бирањем најмањег елемента (*selection sort*)?


Питање 5.
~~~~~~~~~~~~~~

.. mchoice:: Тест5_Питање5
   :answer_a: Четири пута.
   :answer_b: Шест пута.
   :answer_c: Једном.
   :answer_d: Ниједном.
   :correct: a
   :feedback_a: Тачно!
   :feedback_b: Пробај поново! (Обрати пажњу на то да је део низа 1, 2, 3 сортиран!)
   :feedback_c: Пробај поново! (Обрати пажњу на то да део низа 6, 5, 4 није сортиран!)
   :feedback_d: Пробај поново! (Обрати пажњу на то да део низа 6, 5, 4 није сортиран!)

   Колико пута ће бабл-сорт алгоритам проћи кроз низ испод пре него што се заустави?

   .. code-block:: text
   
      L = [6, 5, 4, 1, 2, 3]
   
Питање 6.
~~~~~~~~~~~~~~

.. mchoice:: Тест5_Питање6
   :answer_a: Алгоритам за сортирање бирањем најмањег елемента (selection sort).
   :answer_b: Бабл-сорт алгоритам.
   :answer_c: Оба алгоритма ће потрошити исту количину времена.
   :correct: b
   :feedback_a: Пробај поново!
   :feedback_b: Тачно!
   :feedback_c: Пробај поново!

   Низ испод сортирамо прво бабл-сорт алгоритам, па запишемо време које је алгоритму било потребно.
   Потом исти низ сортирамо алгоритмом за сортирање бирањем најмањег елемента (*selection sort*), па опет запишемо време
   које је алгоритму било потребно. Који алгоритам ће се брже извршити?

   .. code-block:: text
   
      L = [10, 9, 1, 2, 3, 4, 5, 6, 7, 8]
   
Тест
===========

Питање 1.
~~~~~~~~~~~~~~

.. mchoice:: Тест6_Питање1
   :answer_a: [x for x in L if x % 2 == 0]
   :answer_b: [x for x in L if x % 2 != 0]
   :answer_c: [x for x in L and x % 2 == 0]
   :answer_d: [x : x in L and x % 2 != 0]
   :correct: a
   :feedback_a: Тачно!
   :feedback_b: Пробај поново! (Број је паран ако при дељењу са 2 даје остатак 0)
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново! (Број је паран ако при дељењу са 2 даје остатак 0)

   Који од понуђених Пајтон израза из низа ``L`` који је наведен испод издваја све парне бројеве?

   .. code-block:: python

      L = [5, 1, 6, 2, 3, 0]

Питање 2.
~~~~~~~~~~~~~~

.. mchoice:: Тест6_Питање2
   :answer_a: [x for x in L if len(x) > 12]
   :answer_b: [x for x in L if len(x) >= 12]
   :answer_c: [x for x in L if len(x) < 12]
   :answer_d: [x for x in L if len(x) <= 12]
   :correct: b
   :feedback_a: Пробај поново!
   :feedback_b: Тачно!
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново!

   Који од понуђених Пајтон израза из низа ``L`` који је наведен испод издваја све стрингове чија дужина је 12 или више?

   .. code-block:: python

      L = ["popokatepetl", "prestolonaslednik", "kolinearno", "korpulentno", "koncentricno"]

Питање 3.
~~~~~~~~~~~~~~

.. mchoice:: Тест6_Питање3
   :answer_a: [x for x in razred if x[2] == "m"]
   :answer_b: [x for x in razred if x[2] == 15]
   :answer_c: [x for x in razred if x[2] == "m" and x[3] == 15]
   :answer_d: [x for x in razred if x[1] == "m" and x[2] == 15]
   :correct: d
   :feedback_a: Пробај поново!
   :feedback_b: Пробај поново!
   :feedback_c: Пробај поново!
   :feedback_d: Тачно!

   Који од понуђених Пајтон израза из низа ``razred`` који је наведен испод издваја редове који садрже податке о дечацима који
   имају 15 година? (За свако дете у групи наведени су име, пол, старост, маса и висина, тим редом.)

   .. code-block:: python
   
      razred = [["Ana",     "ž", 13, 46, 160],
                ["Bojan",   "m", 14, 52, 165],
                ["Vlada",   "m", 13, 47, 157],
                ["Gordana", "ž", 15, 54, 165],
                ["Dejan",   "m", 15, 56, 163],
                ["Đorđe",   "m", 13, 45, 159],
                ["Elena",   "ž", 14, 49, 161],
                ["Žaklina", "ž", 15, 52, 164],
                ["Zoran",   "m", 15, 57, 167],
                ["Ivana",   "ž", 13, 45, 158],
                ["Jasna",   "ž", 14, 51, 162]]

Питање 4.
~~~~~~~~~~~~~~


.. mchoice:: Тест6_Питање4
   :answer_a: [0, 1, 2, 3]
   :answer_b: [1, 2, 3, 0]
   :answer_c: Систем ће пријавити грешку јер функција append није дефинисана.
   :correct: b
   :feedback_a: Пробај поново!
   :feedback_b: Тачно!
   :feedback_c: Пробај поново!

   Како ће изгледати низ ``L`` након извршења следећег програмчића:

   .. code-block:: python

      L = [1, 2, 3]
	  L.append(0)



Питање 5.
~~~~~~~~~~~~~~


.. mchoice:: Тест6_Питање5
   :answer_a: [0, 0, 1]
   :answer_b: [-1, -1, 0]
   :answer_c: [2]
   :answer_d: []
   :correct: d
   :feedback_a: Пробај поново!
   :feedback_b: Пробај поново!
   :feedback_c: Пробај поново!
   :feedback_d: Тачно!

   Како ће изгледати низ ``L`` након извршења следећег програма:

   .. code-block:: python

      def pozicije_pozitivnih(L):
          i = -1
          rez = []
          for x in L:
              i += 1
              if x > 0:
                  rez.append(i)
          return rez

      L = pozicije_pozitivnih([-2, -1, 0])


Питање 6.
~~~~~~~~~~~~~~

.. mchoice:: Тест6_Питање6
   :answer_a: False
   :answer_b: No
   :answer_c: Ништа
   :answer_d: Систем ће пријавити грешку јер in може да се појави само у запису for-циклуса.
   :correct: a
   :feedback_a: Тачно!
   :feedback_b: Пробај поново! (No није логичка вредност!)
   :feedback_c: Пробај поново! (in је логички оператор!)
   :feedback_d: Пробај поново! (in је логички оператор!)

   Шта ће исписати следећи Пајтон програм:

   .. code-block:: python

      A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
      print(20 in A)



Питање 7.
~~~~~~~~~~~~~~


.. mchoice:: Тест6_Питање7
   :answer_a: [2, 5, 8]
   :answer_b: [1, 4, 7]
   :answer_c: 1
   :answer_d: 7
   :correct: b
   :feedback_a: Пробај поново!
   :feedback_b: Тачно!
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново!

   Како ће изгледати низ ``L`` након извршења следећег програма:

   .. code-block:: python

      def pozicije_svih(e, L):
          i = -1
          rez = []
          for x in L:
              i += 1
              if x == e:
                  rez.append(i)
          return rez

      L = pozicije_svih(5, [1, 5, 4, 3, 5, 1, 0, 5, 6])




























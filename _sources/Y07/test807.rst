Тест
===============

Питање 1.
~~~~~~~~~~~~~

.. mchoice:: Тест7_Питање1
   :answer_a: Екстензија
   :answer_b: Експанзија
   :answer_c: Експлозија
   :answer_d: Екстипија
   :correct: a
   :feedback_a: Тачно!
   :feedback_b: Пробај поново!
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново!

   Датотека ``iliad.txt`` је текстуална датотека која садржи енглески превод Хомерове *Илијаде*.
   Последња четири симбола ``.txt`` означавају врсту података која је смештена у датотеку
   и тај део имена датотеке се зове:

Питање 2.
~~~~~~~~~~~~~

.. fillintheblank:: Тест7_Питање2

   На диску се налази неколико текстуалних датотека:
   
   .. code-block:: text
      
	  hamlet.txt
	  iliad.txt
	  poema.txt
	  
   Који стринг треба корисник да унесе у следећи Пајтон програм да би он пребројао редове у датотеци ``hamlet.txt``?
   
   .. code-block:: python
   
      ime = input()
      f = open(ime + ".txt", "r")
      br = 0
      for red in f: br += 1
      f.close()
      print(br)
   
   - :^hamlet$: Тачно!
     :hamlet.txt: Погледај пажљиво други ред програма!
     :.*: Пробај поново!

Питање 3.
~~~~~~~~~~~~~

.. mchoice:: Тест7_Питање3
   :answer_a: open(f, "poema.txt")
   :answer_b: f = open("poema.txt", "r")
   :answer_c: f.open_read("poema.txt")
   :answer_d: f = open_read("poema.txt")
   :correct: b
   :feedback_a: Пробај поново!
   :feedback_b: Тачно!
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново!

   Која од наведених команди ће отворити датотеку ``poema.txt`` за читање?


Питање 4.
~~~~~~~~~~~~~


.. mchoice:: Тест7_Питање4
   :answer_a: 0
   :answer_b: 1
   :answer_c: 7
   :answer_d: 8
   :correct: b
   :feedback_a: Пробај поново!
   :feedback_b: Тачно!
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново!

   На диску се налази текстуална датотека ``sijaj_sijaj.txt`` која садржи следећих 7 редова текста:
   
   .. code-block:: text

      Sijaj, sijaj zvezdice
      tajne svoje pričaj mi.
      Visoko iznad sveta si
      sjajem dijamanta sjajiš ti. 
      
      Sijaj, sijaj zvezdo mala, 
      tajnu tvoju rado bih znala.

   Колико редова текста има та датотека након извршавања следећег Пајтон програма:

   .. code-block:: python

      f = open("sijaj_sijaj.txt", "w")
      f.write("Sijaj, sijaj, zvezdice!\n")
      f.close()



Питање 5.
~~~~~~~~~~~~~

.. mchoice:: Тест7_Питање4-1
   :answer_a: 0
   :answer_b: 1
   :answer_c: 4
   :answer_d: 7
   :correct: b
   :feedback_a: Пробај поново!
   :feedback_b: Тачно!
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново!

   На диску се налази текстуална датотека ``sijaj_sijaj.txt`` која садржи следећих 7 редова текста:
   
   .. code-block:: text

      Sijaj, sijaj zvezdice
      tajne svoje pričaj mi.
      Visoko iznad sveta si
      sjajem dijamanta sjajiš ti. 
      
      Sijaj, sijaj zvezdo mala, 
      tajnu tvoju rado bih znala.

   Колико редова текста има та датотека након извршавања следећег Пајтон програма:

   .. code-block:: python

      f = open("sijaj_sijaj.txt", "w")
      f.write("Sijaj, sijaj, zvezdice!")
      f.write("Sijaj, sijaj, zvezdice!")
      f.write("Sijaj, sijaj, zvezdice!")
      f.write("Sijaj, sijaj, zvezdice!")
      f.close()


Питање 6.
~~~~~~~~~~~~~


.. mchoice:: Тест7_Питање5
   :answer_a: 0
   :answer_b: 1
   :answer_c: 19400
   :answer_d: 19401
   :correct: a
   :feedback_a: Тачно!
   :feedback_b: Пробај поново!
   :feedback_c: Пробај поново!
   :feedback_d: Пробај поново!

   На диску се налази текстуална датотека ``iliad.txt`` која садржи 19400 редова текста.
   Колико редова текста има та датотека након извршавања следећег Пајтон програма:

   .. code-block:: python

      f = open("iliad.txt", "w")
      f.close()


Питање 7.
~~~~~~~~~~~~~


.. mchoice:: Тест7_Питање6
   :answer_a: 0
   :answer_b: 1
   :answer_c: 19400
   :answer_d: 19401
   :correct: c
   :feedback_a: Пробај поново!
   :feedback_b: Пробај поново!
   :feedback_c: Тачно!
   :feedback_d: Пробај поново!

   На диску се налази текстуална датотека ``iliad.txt`` која садржи 19400 редова текста.
   Колико редова текста има та датотека након извршавања следећег Пајтон програма:

   .. code-block:: python

      f = open("iliad.txt", "a")
      f.close()


Питање 8.
~~~~~~~~~~~~~


.. mchoice:: Тест7_Питање7
   :answer_a: 0
   :answer_b: 1
   :answer_c: 19400
   :answer_d: 19401
   :correct: c
   :feedback_a: Пробај поново!
   :feedback_b: Пробај поново!
   :feedback_c: Тачно!
   :feedback_d: Пробај поново!

   На диску се налази текстуална датотека ``iliad.txt`` која садржи 19400 редова текста.
   Колико редова текста има датотека ``analiza.txt`` након извршавања следећег Пајтон програма:

   .. code-block:: python

      f = open("iliad.txt", "r")
      g = open("analiza.txt", "w")
      for red in f:
          g.write(str(len(red)) + "\n")
      f.close()
      g.close()






















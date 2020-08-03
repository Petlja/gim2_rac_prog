Тест
---------

.. mchoice:: Тест29_Питање1
   :answer_a: Програм исписује оцене ученика.
   :answer_b: Програм исписује колико ученика је добило оцену 5.
   :answer_c: Програм исписује ученике и њихове оцене.
   :answer_d: Програм исписује колико ученика је добило коју оцену.
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   У низу ocene наведене су оцене из информатике у једном разреду.
   Погледај пажљиво следећи Пајтон програм па означи исказ који садржи највише тачних
   информација (*само један*):

   .. code-block:: python

      ocene = [3, 4, 5, 4, 5, 3, 4, 5, 2, 4, 5, 4, 5, 4, 2, 3, 1, 4, 5, 4, 3, 2, 3, 4, 5, 4, 5, 5, 4, 3]
	  for i in [5, 4, 3, 2, 1]:
          print("Ocenu", i, "ima", ocene.count(i), "ucenika")

.. mchoice:: Тест29_Питање2
   :answer_a: Фреквенцијска анализа.
   :answer_b: Фреквенцијална анализа.
   :answer_c: Фреквенцијска анализа и секторски дијаграми.
   :answer_d: Ништа од понуђеног.
   :correct: a
   :feedback_a: Тачно!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Покушај поново!

   Процес током кога се утврђује колико пута се који податак појављује у датом низу података се зове:

.. mchoice:: Тест29_Питање3
   :answer_a: plt.plot(frekvencije, labels=ocene)
   :answer_b: plt.bar(frekvencije, labels=ocene)
   :answer_c: plt.cake(frekvencije, labels=ocene)
   :answer_d: plt.pie(frekvencije, labels=ocene)
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   Библиотека `matplotlib.pyplot` је увезена у програм овако:
   
   .. code-block:: python
   
      import matplotlib.pyplot as plt
   
   Помоћу ње је нацртан следећи дијаграм:

   .. image:: ../../_images/test809sl1.png
      :width: 600

   Којом од понуђених наредби је дијаграм нацртан?

.. mchoice:: Тест29_Питање4
   :answer_a: labels
   :answer_b: expand
   :answer_c: explode
   :answer_d: lateral
   :correct: c
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Тачно!
   :feedback_d: Покушај поново!

   Помоћу функције за цртање секторских дијаграма библиотеке `matplotlib.pyplot` је
   нацртан овај дијаграм:
   
   .. image:: ../../_images/test809sl2.png
      :width: 600

   Како се зове опција ове функције која омогућује измештање сектора из центра дијаграма, као што је
   то случај са секторима "Угљен диоксид" и "Аргон" на слици?
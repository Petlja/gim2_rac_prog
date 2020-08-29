Квиз
---------

.. mchoice:: Тест28_Питање1
   :answer_a: Збир елемената низа а
   :answer_b: Дужину низа а
   :answer_c: Медијану низа а
   :answer_d: Просек елемената низа а
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   Шта рачуна функција ``f``:
   
   .. code-block:: python
   
      def f(a):
          return sum(a)/len(a)

.. mchoice:: Тест28_Питање2
   :answer_a: 37
   :answer_b: 59
   :answer_c: 407
   :answer_d: 102
   :correct: a
   :feedback_a: Тачно!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Покушај поново!

   Шта је медијана низа [37, 11, 25, 59, 10, 407, 102]?

.. mchoice:: Тест28_Питање3
   :answer_a: [5, 1, 6, 2, 3, 0], тј. ништа се неће променити.
   :answer_b: [0, 1, 2, 3, 5, 6], тј. елементи низа ће бити поређани од мањих ка већим вредностима.
   :answer_c: [6, 5, 3, 2, 1, 0], тј. елементи низа ће бити поређани од већих ка мањим вредностима.
   :answer_d: Систем ће пријавити грешку јер функција sort захтева додатни аргумент.
   :correct: b
   :feedback_a: Покушај поново!
   :feedback_b: Тачно!
   :feedback_c: Покушај поново!
   :feedback_d: Покушај поново!

   Како ће изгледати низ L након извршења следећег програмчића:

   .. code-block:: python

      L = [5, 1, 6, 2, 3, 0]
      L.sort()

.. mchoice:: Тест28_Питање4
   :answer_a: [5, 1, 6, 2, 3, 0], тј. ништа се неће променити.
   :answer_b: [0, 1, 2, 3, 5, 6], тј. елементи низа ће бити поређани од мањих ка већим вредностима.
   :answer_c: [6, 5, 3, 2, 1, 0], тј. елементи низа ће бити поређани од већих ка мањим вредностима.
   :answer_d: Систем ће пријавити грешку јер функција sort не сме да садржи додатни аргумент.
   :correct: c
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Тачно!
   :feedback_d: Покушај поново!

   Како ће изгледати низ ``L`` након извршења следећег програмчића:

   .. code-block:: python

      L = [5, 1, 6, 2, 3, 0]
      L.sort(reverse=True)

.. mchoice:: Тест28_Питање5
   :answer_a: [x for x in L if x % 2 == 0]
   :answer_b: [x for x in L if x % 2 != 0]
   :answer_c: [x for x in L and x % 2 == 0]
   :answer_d: [x : x in L and x % 2 != 0]
   :correct: a
   :feedback_a: Тачно!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Покушај поново!

   Који од понуђених Пајтон израза из низа L = [5, 1, 6, 2, 3, 0] издваја све парне бројеве?

.. mchoice:: Тест28_Питање6
   :answer_a: [x for x in L if len(x) > 12]
   :answer_b: [x for x in L if len(x) >= 12]
   :answer_c: [x for x in L if len(x) < 12]
   :answer_d: [x for x in L if len(x) <= 12]
   :correct: b
   :feedback_a: Покушај поново!
   :feedback_b: Тачно!
   :feedback_c: Покушај поново!
   :feedback_d: Покушај поново!

   Који од понуђених Пајтон израза из низа ``L`` који је наведен испод издваја све стрингове чија дужина је 12 или више?

   .. code-block:: python

      L = ["popokatepetl", "prestolonaslednik", "kolinearno", "korpulentno", "koncentricno"]

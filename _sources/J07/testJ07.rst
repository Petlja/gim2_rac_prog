Квиз
---------

.. mchoice:: Тест11_Питање1
   :answer_a: plt.bar(tabela1["Ime"], tabela1["Visina"])
   :answer_b: plt.bar(tabela1.index, tabela1["Visina"])
   :answer_c: plt.bar(tabela1["Ime"], tabela1.index)
   :answer_d: Ниједан од понуђених одговора.
   :correct: b
   :feedback_a: Покушај поново!
   :feedback_b: Тачно!
   :feedback_c: Покушај поново!
   :feedback_d: Покушај поново!

   Погледај пажљиво следећи Пајтон програм

   .. code-block:: python

      import pandas as pd
      podaci = [["Ana",     "ž", 13, 46, 160],
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
      tabela = pd.DataFrame(podaci)
      tabela.columns=["Ime", "Pol", "Starost", "Masa", "Visina"]
      tabela1=tabela.set_index("Ime")

   па означи наредбу која црта следећи дијаграм:

   .. image:: ../../_images/test811sl1.png
      :width: 600

.. mchoice:: Тест11_Питање2
   :answer_a: tabela["Đorđe"]
   :answer_b: tabela1["Đorđe"]
   :answer_c: tabela.loc["Đorđe"]
   :answer_d: tabela1.loc["Đorđe"]
   :answer_e: Ниједан од понуђених одговора.
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   Погледај пажљиво Пајтон програм у претходном задатку па означи наредбу која исписује податке о Ђорђу.

.. mchoice:: Тест11_Питање3
   :answer_a: ocene1["Đorđe"].average()
   :answer_b: ocene1["Đorđe"].mean()
   :answer_c: ocene1.loc["Đorđe"].average()
   :answer_d: ocene1.loc["Đorđe"].mean()
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   Погледај пажљиво следећи Пајтон програм

   .. code-block:: python

      import pandas as pd
      razred = [["Ana",     5, 3, 5, 2, 4, 5],
                ["Bojan",   5, 5, 5, 5, 5, 5],
                ["Vlada",   4, 5, 3, 4, 5, 4],
                ["Gordana", 5, 5, 5, 5, 5, 5],
                ["Dejan",   3, 4, 2, 3, 3, 4],
                ["Đorđe",   4, 5, 3, 4, 5, 4],
                ["Elena",   3, 3, 3, 4, 2, 3],
                ["Žaklina", 5, 5, 4, 5, 4, 5],
                ["Zoran",   4, 5, 4, 4, 3, 5],
                ["Ivana",   2, 2, 2, 2, 2, 5],
                ["Jasna",   3, 4, 5, 4, 5, 5]]
      ocene = pd.DataFrame(razred)
      ocene.columns=["Ime", "Informatika", "Engleski", "Matematika", "Fizika", "Hemija", "Likovno"]
      ocene1 = ocene.set_index("Ime")

   па означи наредбу која рачуна просек Ђорђетових оцена.

.. mchoice:: Тест11_Питање4
   :answer_a: tabela2 има 11 врста и 5 колона.
   :answer_b: tabela2 има исти број врста као tabela1 и исти број колона као tabela1.
   :answer_c: tabela2 има онолико колона колико врста има tabela1.
   :answer_d: tabela2 има онолико колона колико врста има tabela1 и онолико врста колико колона има tabela1.
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   Погледај пажљиво следећи Пајтон програм

   .. code-block:: python

      import pandas as pd
      podaci = [["Ana",     "ž", 13, 46, 160],
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
      tabela = pd.DataFrame(podaci)
      tabela.columns=["Ime", "Pol", "Starost", "Masa", "Visina"]
      tabela1=tabela.set_index("Ime")
	   tabela2=tabela1.T

   па означи исказ који садржи навише тачних информација (*само један*):

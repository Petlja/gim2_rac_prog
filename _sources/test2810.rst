Тест
---------

.. mchoice:: Тест10_Питање1
   :answer_a: Библиотека pandas садржи информације о егзотичним животињама.
   :answer_b: Библиотека pandas садржи функције за цртање графикона.
   :answer_c: Библиотека pandas садржи функције за ефикасан рад са табелама.
   :answer_d: Библиотека pandas садржи функције за рад са табелама, али само по колонама.
   :correct: c

   Означи исказ који садржи највише тачних информација (*само један*):

.. mchoice:: Тест10_Питање2
   :answer_a: Нема разлике у начину на који су организоване табелe у променљивим podaci и tabela.
   :answer_b: У променљивој podaci подаци су представљени на ефикаснији начин него у променљивој tabela.
   :answer_c: У променљивој tabela подаци су представљени на ефикаснији начин него у променљивој podaci.
   :correct: c

   Погледај пажљиво следећи Пајтон програм па означи исказ који садржи највише тачних
   информација (*само један*):

   .. code-block:: python

      import pandas as pd
      podaci = [["Ana",     "ž", 13, 46, 160],
                ["Bojan",   "m", 14, 52, 165],
                ["Vlada",   "m", 13, 47, 157],
                ["Gordana", "ž", 15, 54, 165],
                ["Dejan",   "m", 15, 56, 163],
                ["Đorđe",   "m", 13, 45, 159]]
      tabela = pd.DataFrame(podaci)

.. mchoice:: Тест10_Питање3
   :answer_a: tabela["Visina"].min()
   :answer_b: tabela["Visina"].mean()
   :answer_c: tabela["Visina"].median()
   :answer_d: Ниједан од понуђених одговора.
   :correct: b

   Погледај пажљиво следећи Пајтон програм па означи Пајтон израз који рачуна просечну висину ученика чији
   подаци су наведени:

   .. code-block:: python

      import pandas as pd
      podaci = [["Ana",     "ž", 13, 46, 160],
                ["Bojan",   "m", 14, 52, 165],
                ["Vlada",   "m", 13, 47, 157],
                ["Gordana", "ž", 15, 54, 165],
                ["Dejan",   "m", 15, 56, 163],
                ["Đorđe",   "m", 13, 45, 159]]
      tabela = pd.DataFrame(podaci)
      tabela.columns=["Ime", "Pol", "Starost", "Masa", "Visina"]

.. mchoice:: Тест10_Питање4
   :answer_a: plt.bar(tabela["Ime"], tabela["Visina"])
   :answer_b: plt.bar(tabela["Ime", "Visina"])
   :answer_c: plt.bar("Ime", "Visina")
   :answer_d: Ниједан од понуђених одговора.
   :correct: a

   Погледај пажљиво Пајтон програм у претходном задатку па означи наредбу која црта следећи дијаграм:

   .. image:: test810sl1.png
      :width: 600

.. mchoice:: Тест10_Питање5
   :answer_a: Comma Stored Values
   :answer_b: Comma Separated Values
   :answer_c: Completly Separated Values
   :answer_d: Completly Stored Values
   :answer_e: Ниједан од понуђених одговора.
   :correct: b

   Име CSV формата записа података је настало као акроним енглеског израза


.. mchoice:: Тест10_Питање6
   :answer_a: Опција header=None функције read_csv значи да табела у датотеци TemperaturneAnomalije.csv нема заглавље.
   :answer_b: Опција header=None функције read_csv значи да табела у датотеци TemperaturneAnomalije.csv има заглавље, али га током учитавања табеле треба игнорисати.
   :answer_c: Систем пријављује грешку зато што функције read_csv не познаје опцију header=None.
   :correct: a

   Погледај пажљиво следећи Пајтон програм па означи тачан исказ (*само један*):

   .. code-block:: python

      import pandas as pd
      temp_anomalije = pd.read_csv("podaci/TemperaturneAnomalije.csv", header=None)
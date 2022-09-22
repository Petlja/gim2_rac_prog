Квиз
---------

.. mchoice:: Тест14_Питање1
   :answer_a: obrada = pd.read_excel("Podaci.xlsx", sheet_name="Podaci")
   :answer_b: podaci = pd.read_excel("Podaci.xlsx", sheet="Obrada")
   :answer_c: finalno = pd.read_excel("Podaci.xlsx", sheet="2")
   :answer_d: sirovi_podaci = pd.read_excel("Podaci.xlsx", sheet_name="Obrada")
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   Ексел датотека ``Podaci.xlsx`` има три радна листа: ``Sirovi podaci``, ``Obrada`` и ``Finalno``.
   Којом наредбом ћемо учитати само табелу која се налази на другом радном листу?
   Подразумева се да је библиотека ``pandas`` учитана наредбом ``import pandas as pd``.
   
.. mchoice:: Тест14_Питање2
   :answer_a: Опција na_filter=False функције read_excel значи да табела у датотеци Aditivi.xlsx није филтрирана.
   :answer_b: Опција na_filter=False функције read_excel значи да табела у датотеци Aditivi.xlsx има заглавље, али га током учитавања табеле треба игнорисати.
   :answer_c: Опција na_filter=False функције read_excel значи да табела у датотеци Aditivi.xlsx има непопуњена поља која ће остати празна након учитавања табеле.
   :answer_d: Систем пријављује грешку зато што функција read_csv не познаје опцију header=None.
   :correct: c
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Тачно!
   :feedback_d: Покушај поново!

   Погледај пажљиво следећи Пајтон програм па означи тачан исказ (*само један*):

   .. code-block:: python

      import pandas as pd
      aditivi = pd.read_excel("Aditivi.xlsx", na_filter=False)
	  
.. mchoice:: Тест14_Питање3
   :answer_a: Овај програм снима учитане податке на рачунар на коме се програм извршава у формату CSV.
   :answer_b: Овај програм учитава податке из CSV датотеке.
   :answer_c: Овај програм снима учитане податке на рачунар на коме се програм извршава у формату XLSX.
   :answer_d: Овај програм учитава податке из CSV датотеке и снима податке на рачунар на коме се програм извршава у облику Ексел табеле.
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   Погледај пажљиво следећи Пајтон програм

   .. code-block:: python

      import pandas as pd
      podaci = pd.read_csv("podaci.csv")
      podaci.to_excel("podaci.xlsx")

   па означи исказ који садржи навише тачних информација (*само један*):

.. mchoice:: Тест14_Питање4
   :answer_a: Овај програм снима учитане податке на удаљени ресурс (интернет) у формату XLSX.
   :answer_b: Овај програм снима учитане податке на рачунар на коме се програм извршава у формату CSV.
   :answer_c: Овај програм снима учитане податке на рачунар на коме се програм извршава у формату CSV и при томе у датотеку записује и садржај индексне колоне.
   :answer_d: Овај програм снима учитане податке на рачунар на коме се програм извршава у формату XLSX и при томе у датотеку не записује садржај индексне колоне.
   :correct: d
   :feedback_a: Покушај поново!
   :feedback_b: Покушај поново!
   :feedback_c: Покушај поново!
   :feedback_d: Тачно!

   Погледај пажљиво следећи Пајтон програм

   .. code-block:: python

      import pandas as pd
      podaci = pd.read_csv("podaci.csv")
      podaci.to_excel("podaci.xlsx", encoding="utf-8", index=False))

   па означи исказ који садржи навише тачних информација (*само један*):
Задаци - процесирање низова
---------------------------

.. questionnote::

    Направите листу помоћу *list comprehension* у којој су вредности 1, 3, 6, 10, 15 ..., односно збирови узастопних природних бројева од 1 до n за свако n од 1 до 20.

.. moguće rešenje - [sum(range(1,n+1)) for n in range(1,21)]

.. activecode:: zadatak1_1_1
   :runortest: lista
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-

   lista = [??? for n in range(?,?)]

   # -*- acsection: after-main -*-
   print(lista)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           run_test = acMainSection(lista = [sum(range(1,n+1)) for n in range(1,21)])
           self.assertEqual(run_test, [sum(range(1,n+1)) for n in range(1,21)], "")
   myTests().main()


Задатак 2.
''''''''''

.. questionnote:: 
    
    Направите листу ["1. broj", "2. broj" ... "20. broj"] помоћу list comprehension.

.. moguće rešenje - [str(i)+'. broj' for i in range(1,21)]

.. activecode:: zadatak1-2_2
   :runortest: 
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-

   lista = [??? +'. broj' ???] 

   # -*- acsection: after-main -*-
   print(lista)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           run_test = acMainSection(lista = [sum(range(1,n+1)) for n in range(1,21)])
           self.assertEqual(run_test, [sum(range(1,n+1)) for n in range(1,21)], "")
   myTests().main()

Задатак 3.
''''''''''

.. questionnote::
    
    Направите листу свих цифара свих бројева од 1 до 100.

.. moguće rešenje - [str(i)[j] for i in range(1,21) for j in range(len(str(i)))]

.. activecode:: zadatak1-3_3
   :runortest: test1, test2, test3, test4, test5
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-
   
    lista = []

   # -*- acsection: after-main -*-
   print(lista)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           run_test = acMainSection(lista = [sum(range(1,n+1)) for n in range(1,21)])
           self.assertEqual(run_test, [sum(range(1,n+1)) for n in range(1,21)], "")
   myTests().main()



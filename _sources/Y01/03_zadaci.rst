Задаци - процесирање низова
---------------------------

Задатак 1.
''''''''''

Напиши функцију ``najveci_od_tri(A0, A1, A2)`` која рачуна  и враћа највећи од три дата броја, али без употребе стандардне функције ``max``.
Напиши тело функције, па онда провери како функција ради.

.. activecode:: zadatak1-1
   :runortest: test1, test2, test3
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-
   def najveci_od_tri(A0, A1, A2):
       # Овде напиши функцију која рачуна највећи од бројева A0, A1, A2
       return -1234  # поправи овај ред!

   # Провера
   test1 = najveci_od_tri(5, 7, 11)
   test2 = najveci_od_tri(5, 75, 11)
   test3 = najveci_od_tri(55, 7, 11)
   # -*- acsection: after-main -*-
   print(test1, test2, test3)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           rez1 = max([5, 7,  11])
           rez2 = max([5, 75, 11])
           rez3 = max([55, 7, 11])
           run_test = acMainSection(test1=test1,test2=test2,test3=test3)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде %s" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде %s" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде %s" % rez3)
   myTests().main()


Задатак 2.
''''''''''

Напиши функцију ``najveci_od_pet(A0, A1, A2, A3, A4)``
која рачуна и враћа највећи од пет датих бројева, али без употребе стандардне функције ``max``.
Напиши тело функције, па онда провери како функција ради.

.. activecode:: zadatak1-2
   :runortest: test1, test2, test3, test4, test5
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-
   def najveci_od_pet(A0, A1, A2, A3, A4):
       # Овде напиши функцију која рачуна највећи од бројева A0, A1, A2, A3, A4
       return -1234  # поправи овај ред!

   # Провера
   test1 = najveci_od_pet(1, 2, 3, 4, 55)
   test2 = najveci_od_pet(1, 2, 3, 44, 5)
   test3 = najveci_od_pet(1, 2, 33, 4, 5)
   test4 = najveci_od_pet(1, 22, 3, 4, 5)
   test5 = najveci_od_pet(11, 2, 3, 4, 5)
   # -*- acsection: after-main -*-
   print(test1, test2, test3, test4, test5)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           rez1 = max(1, 2, 3, 4, 55)
           rez2 = max(1, 2, 3, 44, 5)
           rez3 = max(1, 2, 33, 4, 5)
           rez4 = max(1, 22, 3, 4, 5)
           rez5 = max(11, 2, 3, 4, 5)
           run_test=acMainSection(test1=test1,test2=test2,test3=test3,test4=test4,test5=test5)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде %s" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде %s" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде %s" % rez3)
           self.assertEqual(run_test["test4"], rez4, "Вредност променљиве 'test4' треба да буде %s" % rez4)
           self.assertEqual(run_test["test5"], rez5, "Вредност променљиве 'test5' треба да буде %s" % rez5)
   myTests().main()


Задатак 3.
''''''''''

Напиши функцију ``max_niza(A)`` која за дати низ ``А``
рачуна и враћа највећи елемент, али без употребе стандардне функције ``max``.
Напиши тело функције, па онда провери како функција ради.

.. activecode:: zadatak1-3
   :runortest: test1, test2, test3, test4, test5
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-
   def max_niza(A):
       # Овде напиши функцију
       return -1234  # поправи овај ред!

   # Провера
   test1 = max_niza([1, 2, 3, 4, 55, 6])
   test2 = max_niza([1, 2, 3, 4, 55, 777])
   test3 = max_niza([111, 2, 3, 4])
   test4 = max_niza([1, 222])
   test5 = max_niza([22])
   # -*- acsection: after-main -*-
   print(test1, test2, test3, test4, test5)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           rez1 = max([1, 2, 3, 4, 55, 6])
           rez2 = max([1, 2, 3, 4, 55, 777])
           rez3 = max([111, 2, 3, 4])
           rez4 = max([1, 222])
           rez5 = max([22])
           run_test=acMainSection(test1=test1,test2=test2,test3=test3,test4=test4,test5=test5)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде %s" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде %s" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде %s" % rez3)
           self.assertEqual(run_test["test4"], rez4, "Вредност променљиве 'test4' треба да буде %s" % rez4)
           self.assertEqual(run_test["test5"], rez5, "Вредност променљиве 'test5' треба да буде %s" % rez5)
   myTests().main()




Задатак 4.
'''''''''''

На контролној провери из Информатике у једној школи се ради шест задатака од којих сваки носи по 20 поена, али наставник даје оцену
на основу пет најбоље урађених задатака. Напиши функцију ``zbir_najboljih_5(Z1, Z2, Z3, Z4, Z5, Z6)`` која
за списак поена по задацима које је освојио неки ученик на тој контролној провери враћа збир поена пет најбоље урађених задатака.
Напиши тело функције, па онда провери како функција ради.
(Упутство: Задатак можеш решити употребом неколико if-ова, али и употребом стандардних функција ``sum`` и ``min``).

.. activecode:: zadatak1-4
   :runortest: test1, test2, test3
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-
   def zbir_najboljih_5(Z1, Z2, Z3, Z4, Z5, Z6):
       # Овде напиши функцију
       return -1234  # поправи овај ред!

   # Провера
   test1 = zbir_najboljih_5(20, 20, 20, 20, 20, 20)
   test2 = zbir_najboljih_5(10,  0, 15, 20,  0, 20)
   test3 = zbir_najboljih_5( 5,  7, 10, 15, 17, 20)
   # -*- acsection: after-main -*-
   print(test1, test2, test3)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           L = [20, 20, 20, 20, 20, 20]; rez1 = sum(L) - min(L)
           L = [10,  0, 15, 20,  0, 20]; rez2 = sum(L) - min(L)
           L = [ 5,  7, 10, 15, 17, 20]; rez3 = sum(L) - min(L)
           run_test = acMainSection(test1=test1,test2=test2,test3=test3)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде %s" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде %s" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде %s" % rez3)
   myTests().main()


Задатак 5.
''''''''''

Напиши функцију ``srednji_od_tri(A0, A1, A2)`` која рачуна и враћа средњи од три дата броја.
Напиши тело функције, па онда провери како функција ради.
(Упутство: Задатак можеш решити употребом неколико if-ова, али и употребом функција ``sum``, ``min`` и ``max``!)


.. activecode:: zadatak1-5
   :runortest: test1, test2, test3, test4
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-
   def srednji_od_tri(A0, A1, A2):
       # Овде напиши функцију
       return -1234  # поправи овај ред!

   # Провера
   test1 = srednji_od_tri(2, 7, 5)
   test2 = srednji_od_tri(2, 5, 5)
   test3 = srednji_od_tri(5, 5, 1)
   test4 = srednji_od_tri(2, 2, 2)
   # -*- acsection: after-main -*-
   print(test1, test2, test3, test4)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           L = [2, 7, 5]; rez1 = sum(L) - min(L) - max(L)
           L = [2, 5, 5]; rez2 = sum(L) - min(L) - max(L)
           L = [5, 5, 1]; rez3 = sum(L) - min(L) - max(L)
           L = [2, 2, 2]; rez4 = sum(L) - min(L) - max(L)
           run_test=acMainSection(test1=test1,test2=test2,test3=test3,test4=test4)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде %s" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде %s" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде %s" % rez3)
           self.assertEqual(run_test["test4"], rez4, "Вредност променљиве 'test4' треба да буде %s" % rez4)
   myTests().main()



Задатак 6.
'''''''''''

Један наставник информатике закључује оцене тако што пре рачунања средње оцене одбаци највећу и најмању оцену,
па средњу вредност рачуна на основу преосталих оцена. Напиши функцију ``srednja_vrednost_bez_ekstrema(ocene)`` која
за списак оцена које је неки ученик добио из Информатике рачуна средњу оцену на описани начин.
Напиши тело функције, па онда провери како функција ради.
(Упутство: Задатак можеш решити употребом стандардних функција ``sum``, ``min``, ``max`` и ``len``).

.. activecode:: zadatak1-6
   :runortest: test1, test2, test3
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-
   def srednja_vrednost_bez_ekstrema(ocene):
       # Овде напиши функцију
       return -1234  # поправи овај ред!

   # Провера
   test1 = srednja_vrednost_bez_ekstrema([5, 5, 5, 5, 5])
   test2 = srednja_vrednost_bez_ekstrema([1, 2, 5])
   test3 = srednje_vrednost_bez_ekstrema([1, 2, 3, 4, 5])
   # -*- acsection: after-main -*-
   print(test1, test2, test3)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           L = [5, 5, 5, 5, 5]; rez1 = (sum(L) - min(L) - max(L))/(len(L) - 2)
           L = [1, 2, 5];       rez2 = (sum(L) - min(L) - max(L))/(len(L) - 2)
           L = [1, 2, 3, 4, 5]; rez3 = (sum(L) - min(L) - max(L))/(len(L) - 2)
           run_test = acMainSection(test1=test1,test2=test2,test3=test3)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде %s" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде %s" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде %s" % rez3)
   myTests().main()





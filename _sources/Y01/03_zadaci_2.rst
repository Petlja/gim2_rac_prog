Задаци - креирање листа
-----------------------

Задатак 1.
''''''''''

.. questionnote::

    Направите листу помоћу *list comprehension* у којој су вредности 1, 3, 6, 10, 15 ..., односно збирови узастопних природних бројева од 1 до n за свако n од 1 до 20.

.. moguće rešenje

    [sum(range(1,n+1)) for n in range(1,21)]


.. activecode:: zadatak1_1_1
    :runortest: n
    :nocodelens:

    # -*- acsection: general-init -*-
    # Izmeni prvu liniju koda tako da bude oblika
    # lista = [___ for n in range(___, ___)]
    # i umesto linija stavi odgovarajuce izraze
    # -*- acsection: main -*-
    lista = []
    print(lista)
    # -*- acsection: after-main -*-
    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):
        def testOne(self):
            for n in [20]:
                lista = [sum(range(1,k+1)) for k in range(1, n+1)]
                expected = str(lista)
                actual = "\n".join(acStdout(n=n))
                correct = (actual == expected)
                expected = expected.replace("\n", "<br>")
                actual = actual.replace("\n","<br>")
                if correct:
                    comment = 'Добијен је исправан резултат' % (n,)
                else:
                    comment = 'Програм даје погрешан резултат:<br>добијено је<br>%s<br>а очекивано<br>%s'
                    comment = comment % (actual, expected)
                self.appendResult(correct, actual, expected, comment)
                
    myTests().main()



Задатак 2.
''''''''''

.. questionnote:: 
    
    Направите листу ["1. broj", "2. broj" ... "20. broj"] помоћу list comprehension.

.. moguće rešenje 

    [str(i)+'. broj' for i in range(1,21)]

.. activecode:: zadatak1-2_2
    :runortest: n
    :nocodelens:

    # -*- acsection: general-init -*-
    # Izmeni prvu liniju koda tako da bude oblika
    # lista = [___ +'. broj' ___] 
    # i umesto linija stavi odgovarajuce izraze
    # -*- acsection: main -*-
    lista = []
    print(lista)
    # -*- acsection: after-main -*-
    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):
        def testOne(self):
            for n in [20]:
                lista = [str(i)+'. broj' for i in range(1,n+1)]
                expected = str(lista)
                actual = "\n".join(acStdout(n=n))
                correct = (actual == expected)
                expected = expected.replace("\n", "<br>")
                actual = actual.replace("\n","<br>")
                if correct:
                    comment = 'Добијен је исправан резултат' % (n,)
                else:
                    comment = 'Програм даје погрешан резултат:<br>добијено је<br>%s<br>а очекивано<br>%s'
                    comment = comment % (actual, expected)
                self.appendResult(correct, actual, expected, comment)
                
    myTests().main()



Задатак 3.
''''''''''

.. questionnote::
    
    Направите листу свих цифара свих бројева од 1 до 100.

.. moguće rešenje 

    [str(i)[j] for i in range(1,101) for j in range(len(str(i)))]

.. activecode:: zadatak1-3_3
    :runortest: n
    :nocodelens:

    # -*- acsection: general-init -*-
    # Izmeni prvu liniju koda tako da bude oblika
    # lista = [___ for i in range(___) for j in range(___)]
    # i umesto linija stavi odgovarajuce izraze
    # -*- acsection: main -*-
    lista = []
    print(lista)
    # -*- acsection: after-main -*-
    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):
        def testOne(self):
            for n in [100]:
                lista = [str(i)[j] for i in range(1,n+1) for j in range(len(str(i)))]
                expected = str(lista)
                actual = "\n".join(acStdout(n=n))
                correct = (actual == expected)
                expected = expected.replace("\n", "<br>")
                actual = actual.replace("\n","<br>")
                if correct:
                    comment = 'Добијен је исправан резултат' % (n,)
                else:
                    comment = 'Програм даје погрешан резултат:<br>добијено је<br>%s<br>а очекивано<br>%s'
                    comment = comment % (actual, expected)
                self.appendResult(correct, actual, expected, comment)
                
    myTests().main()

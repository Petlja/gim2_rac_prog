Коришћење текстуалних датотека
------------------------------

Текст можемо да чувамо у текстуалној датотеци у спољашњој меморији и да
га одатле по потреби учитавамо. У општем случају, текст у датотеци може
да буде низ симбола непознате дужине који нема никакву посебну
структуру. Овде нема индекса и датотеке се увек читају од почетка до
краја. На крају фајла се налази контролни кôд за крај фајла (EOF, од
енгл. *end of file*). Када Пајтон прочита овај кôд, прекида са читањем.
Садржај датотеке можемо да читамо знак по знак, линију по линију или да
цео текст прочитамо одједном.

Свака датотека мора да има име, а обично последњих неколико симбола у
имену означава тип података који је у датотеку смештен. Тај део имена се
обично одвоји тачком од остатка имена и зове се **екстензија**.
Текстуалне датотеке обично имају екстензију .txt.

Податке из неке датотеке можемо или само да читамо, или је могућ само
упис у датотеку. Није могуће истовремено и писати у неку датотеку и
читати из ње. Због тога при отварању датотеке морамо да нагласимо да ли
отварамо због читања или због писања. Свакој отвореној датотеци
придружујемо променљиву. За даљу комуникацију са датотеком на диску
користимо назив ове променљиве.

Пре било какве акције са текстуалном датотеком (писање у датотеку или
читање из датотеке) она мора да се „отвори”, а након акције мора да се
„затвори”. Свако ново позивање функције за читање из датотеке враћа нас
на место где смо прошли пут стали са читањем. Датотеке се увек читају
секвенцијално и немамо начина да прочитамо нпр. 1000. ред у тексту, а да
претходно не причитамо претходних 999. Показивач који говори Пајтону
који ред следећи треба да прочита ресетује се када датотеку затворимо.
Када пишемо у датотеку која већ има неки садржај, ми нови садржај
додајемо на крај.

Читање из датотеке
~~~~~~~~~~~~~~~~~~

Користићемо датотеку ``A_Very_Short_Story.txt`` у којој се налази
текст Хемингвејеве кратке приче на енглеском језику. Ову датотеку можете да
отворите помоћу било ког едитора, као што је нпр. Notepad, али нам је
овде важније да текст отворимо у Пајтону. За то користимо функцију
``open()``. Аргументи ове функције су стринг са локацијом и називом
фајла и мод (стринг у ком пише са којом наменом отварамо фајл). Мод може
имати више вредности. Нама су најважније ове три: ``"r"`` отвара
датотеку за читање, ``"a"`` отвара датотеку за повремено додавање текста
и ``"w"`` за отварање нове датотеке у коју уписујемо текст.

.. activecode:: fajl
    :nocodelens:
    :available_files: A_Very_Short_Story.txt
    :passivecode: True

    f = open("A_Very_Short_Story.txt", "r")

Променљива ``f`` није стринг већ отворена конекција према датотеци на
диску. Да бисмо прочитали текст коришћењем отворене конекције,
користићемо функцију ``.readline()`` која чита један цео ред текста и
враћа га као стринг. На крају сваког реда се налази контролни кôд за
крај реда (EOL, од енгл. *end of line* који сеу текстуалној датотеци
означава са ``\n``). Функција ``.readln()`` чита од почетка до знака за
крај реда. Пошто не знамо колико редова има текст у датотеци, овде ћемо
прочитати и исписати само првих осам редова.

.. activecode:: prvih_8_ilijada
    :nocodelens:
    :include: fajl

    for i in range(8):
        r=f.readline()
        print(i, r)
    

Уколико немамо намеру даље да читамо текст из датотеке, пожељно је да
фајл затворимо помоћу функције ``.close()``.

.. activecode:: close
    :passivecode: True
    :nocodelens:
    :include: fajl

    f.close()

Да бисмо сазнали колико редова има текст у датотеци, потребно је да
прочитамо и пребројимо све редове. Следећи програм управо то ради.

.. activecode:: brojanje1
    :nocodelens:
    :include: fajl

    f = open("A_Very_Short_Story.txt", "r")
    br_redova = 0
    for red in f:
        br_redova += 1
    f.close()
    print("Datoteka 'A_Very_Short_Story.txt' ima", br_redova, "redova.")

Функција ``.read()`` чита онолико карактера из датотеке колико наведемо
у аргументу. Међу њима може да буде и контролних. Зависно од типа обраде
текста који планирамо, бирамо начин читања из датотеке. Овде ћемо само
дати пример читања првих 100 карактера из текста Илијаде. Да бисмо
приказали кодове уместо преломљеног текста користимо функцију ``repr()``
која враћа “сирови” стринг. Тако ћемо јасно видети где су који контролни
карактери, нпр. крај реда ``\n``. Уколико не наведемо колико карактера
хоћемо да учитамо, функција ``.read()`` ће прочитати цео текст.

.. activecode:: karakteri_Citanje
    :nocodelens:

    f = open("A_Very_Short_Story.txt", "r")
    s=f.read(100)
    f.close()
    print(repr(s))

Коначно, функција ``.readlines()`` чита све редове текста и памти их као
елементе листе.

.. activecode:: readlines

    f = open("A_Very_Short_Story.txt", "r")
    lista=f.readlines()
    f.close()
    print(lista[:10])

Обрада текста
-------------

Обрада текста учитаног из датотеке само се по обиму разликује од обраде
текста у једном стрингу. Све што можемо са стрингом од неколико
карактера, можемо и са стрингом у који стаје цела књига. Овде ћемо на
примеру Илијаде приказати неке могућности за обраду текста коришћењем
стандардне библиотеке. Када бисмо увезли библиотеку *pandas* или неку
библиотеку специјализовану за рад са текстом, број опција за обраду које
би нам биле на располагању био би много већи. Ми се oвде тиме
нећемо бавити. Држаћемо се само структура и функција које можемо да
користимо без увожења додатних библиотека.

.. activecode:: citaj
    :passivecode: True
    :nocodelens:

    f=open("A_Very_Short_Story.txt", "r")  # otvaramo fajl za čitanje
    s=f.read()                     # čitamo ceo tekst i smeštamo ga u string s
    f.close()                      # zatvaramo fajl

Прво, можемо да погледамо којих све карактера има у овом фајлу.
Приказивање целог текста не би било баш практично, зато ћемо прибегнемо
статистици. У листу ``l`` стављамо све карактере из стринга ``s``.

.. activecode:: broj_karaktera
    :nocodelens:
    :include: citaj

    duzina = len(s)    # ukupan broj karaktera u tekstu
    print(duzina)


.. activecode:: prvi_karakteri
    :nocodelens:
    :include: citaj

    prvih_500 = s[:500]   # prikazujemo prvih 500 karaktera stringa s
    print(prvih_500)


.. activecode:: lista_karakteri
    :nocodelens:
    :include: citaj

    l=[x for x in s]
    print(l[:20])

У 3265 хиљада карактера сигурно има много оних који се често понављају.
Да ли знате како бисте издвојили јединствене карактере и утврдили колико
се пута понављају? Потребне су нам две листе: једна у коју слажемо
јединствене вредности карактера и друга у коју записујемо колико пута се
поновио одговарајући карактер.

.. activecode:: jedinstveni
    :nocodelens:
    :include: citaj, lista_karakteri

    jk=[]                            # lista jedinstvenih karaktera
    bp=[]                            # lista broja ponavljanja svakog jedinstvenog karaktera
    for x in l:                      # za svaki karakter iz liste
        if x not in jk:              # proveravamo da li je već u listi jedistvenih
            jk.append(x)             # ako nije, dodajemo taj karakter u listu jk
            bp.append(l.count(x))    # i dodajemo broj ponavljanja u listi bp
    print(len(jk))


Број различитих карактера који се појављују у тексту је 76. Осим великих
и малих слова ту су цифре, знаци интерпункције и неки контролни
карактери. Ево који су то карактери и колико пута се понављају.

.. activecode:: range2
    :nocodelens:
    :include: citaj, lista_karakteri, jedinstveni

    for i in range(len(jk)):
        print(repr(jk[i]),bp[i])   # koristimo repr() da bismo prikazali "sirovi" karakter
    

Није тешко установити који се карактер понавља највише пута: размак, тј.
’ ’, чак 605 пута.

Сличну анализу коју смо урадили за карактере можемо да урадимо и за речи
у тексту. Мали је проблем што речи не можемо тако лако да издвојимо као
карактере. Обично су речи низови слова између два размака, али имамо и
разне друге карактере који нам сметају. Да погледамо како изгледа првих
1000 карактера “сировог” текста кратке приче.

.. activecode:: prvih_1000
    :nocodelens:
    :include: citaj

    prvih_1000 = s[:1000]
    print(prvih_1000)

Оно што можемо да видимо је да речи често одваја знак за нови ред. Било
би нам лакше да је на том месту размак. Што се тиче зареза, тачака и
осталих знака интерпункције, укључујући наводнике, лакше би нам било да
их нема. Зато ћемо себи олакшати посао тако што ћемо знак за нови ред
заменити размаком помоћу функције ``.replace()``, док ћемо остале знаке
заменити празним стрингом, ““. То је исто као да смо их избрисали. Исто
ћемо урадити и са стрингом”–” који има декоративну функцију.

.. activecode:: replace_metod
    :nocodelens:
    :passivecode: True
    :include: citaj

    s=s.replace("\n", " ")
    for x in "!?.,:;()[]*0123456789":
        s=s.replace(x, "")
    for x in "\"\'":
        s=s.replace(x, "")
    s=s.replace("--","")

Када прикажемо текст добијен овим кодом, видећемо да изгледа много чистије и можемо да испитамо која се реч колико
пута појављује у тексту.

.. activecode:: print_cisti
    :nocodelens:
    :include: citaj, replace_metod

    print(s)

Мали проблем нам представља што иста реч може
имати различит облик ако је на почетку реда. Због тога “The” и “the” не
би биле препознате као исте речи. Уколико сва слова сведемо на мала
помоћу функције ``.lower()``, биће лакше да их пребројимо.

.. activecode:: ukljuci_lower
    :nocodelens:
    :passivecode: True
    :include: citaj, replace_metod

    s=s.lower()

Ако сада одштампамо текст, видећемо да је сваки карактер претворен у мало слово. 

.. activecode:: print_cisti_lower
    :nocodelens:
    :include: citaj, replace_metod, ukljuci_lower

    print(s)

    
.. activecode:: prvih400
    :nocodelens:
    :include: citaj, replace_metod, ukljuci_lower

    print(s[:400])

Сада је лако да препознамо појединачне речи. Довољно је да узмемо низове
карактера који су раздвојени размацима и да их сачувамо у листи.

.. activecode:: split_reci
    :nocodelens:
    :passivecode: True
    :include: citaj, replace_metod, ukljuci_lower

    ssp=s.split()

.. activecode:: printaj_split
    :nocodelens:
    :include: citaj, replace_metod, ukljuci_lower, split_reci

    print(ssp[:10])


Сада да видимо можемо ли да поновимо оно тражење јединствених елемената
листе и њихово пребројавање које смо урадили са карактерима. Имајте у
виду да је ово заметан посао за који ће рачунару бити потребно 20-30
секунди. Велики је посао пронаћи хиљаде различитих речи и за сваку проћи
кроз цео текст како бисмо их пребројали.

.. activecode:: broj_reci
    :passivecode: True
    :nocodelens:
    :include: citaj, replace_metod, ukljuci_lower, split_reci

    jr=[]                            # lista jedinstvenih reči
    bpr=[]                           # lista broja ponavljanja svake jedinstvene reči
    for x in ssp:                    # za svaku reč iz liste
        if x not in jr:              # proveravamo da li je već u listi jedistvenih
            jr.append(x)             # ako nije, dodajemo taj karakter u listu jr
            bpr.append(ssp.count(x)) # i dodajemo broj ponavljanja u listu bpr

.. activecode:: print_broj_reci
    :nocodelens:
    :include: citaj, replace_metod, ukljuci_lower, split_reci, broj_reci

    print('broj jedinstvenih reči je: ', len(jr))   # broj jedinstvenih reči


.. activecode:: najveci_broj, 
    :include: citaj, replace_metod, ukljuci_lower, split_reci, broj_reci
    :nocodelens:

    print(max(bpr))                 # najveći broj ponavljanja
    print(jr[bpr.index(max(bpr))])  # jedinstvena reč sa indkesom koji odgovara reči sa najvećim brojem ponavljanja


Не улазећи у фреквенцијску анализу речи у тексту, само да погледамо
почетак листе, односно које су то речи и колико се пута понављају.

.. activecode:: brojevi_po_reci
    :include: citaj, replace_metod, ukljuci_lower, split_reci, broj_reci
    :nocodelens:

    for i in range(20):
        print(jr[i],bpr[i])

За анализу ових података згодно је да фреквенције речи упишемо у фајл.
Касније можемо да изаберемо алат којим ћемо радити анализу.

Уписивање података у датотеку
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

За уписивање података у фајл користим функцију ``.write()`` са истим
функцијама за отварање и затварање датотеке као што је то било код
читања. Оно што уписујемо мора да буде стринг. У следећем примеру у
датотеку уписујемо по један стринг за сваку јединствену реч. Тај стринг
добијамо спајањем јединствене речи, зареза, броја понављања у облику
стринга и знака за крај реда.

.. code:: ipython3

    g = open("data/Iliad stat.txt", "w") # otvaramo fajla sa ovim imenom za upisivanje
    for i in range(len(jr)):             # za svaku jedinstvenu reč
        zapis=jr[i]+','+str(bpr[i])+'\n' # napravi string u kom su jed. reč, broj pojavljivanja i znak za kraj reda
        g.write(zapis)                   # zapiši string kao novi red u fajlu
    g.close()

Иако у текстуални фајл можемо да упишемо податке на произвољно много
начина, у овом примеру смо се трудили да направимо неку структуру. Сваки
запис има две речи одвојене зарезом, а сваки запис иде у посебан ред. То
је формат познат као CSV (*comma separated values*) који је стандард за
табеларно приказане податке. Овакав фајл можете лако да увезете у Ексел
или да га прочитате из Пајтона помоћу *pandas* библиотеке. Пробајте то
да урадите.


.. datafile:: A_Very_Short_Story.txt
    :hide:

    A Very Short Story
    Ernest Hemingway
    One hot evening in Padua they carried him up onto the roof and he could look out over the top of the town.
    There were chimney swifts in the sky. After a while it got dark and the searchlights came out. The others went down
    and took the bottles with them. He and Luz could hear them below on the balcony. Luz sat on the bed. She was cool
    and fresh in the hot night.
    Luz stayed on night duty for three months. They were glad to let her. When they operated on him she
    prepared him for the operating table; and they had a joke about friend or enema. He went under the anaesthetic
    holding tight on to himself so he would not blab about anything during the silly, talky time. After he got on crutches
    he used to take the temperatures so Luz would not have to get up from the bed. There were only a few patients, and
    they all knew about it. They all liked Luz. As he walked back along the halls he thought of Luz in his bed.
    Before he went back to the front they went into the Duomo and prayed. It was dim and quiet, and there
    were other people praying. They wanted to get married, but there was not enough time for the banns, and neither of
    them had birth certificates. They felt as though they were married, but they wanted everyone to know about it, and to
    make it so they could not lose it.
    Luz wrote him many letters that he never got until after the armistice. Fifteen came in a bunch to the front
    and he sorted them by the dates and read them all straight through. They were all about the hospital, and how much
    she loved him and how it was impossible to get along without him and how terrible it was missing him at night.
    After the armistice they agreed he should go home to get a job so they might be married. Luz would not come home
    until he had a good job and could come to New York to meet her. It was understood he would not drink, and he did
    not want to see his friends or anyone in the States. Only to get a job and be married. On the train from Padua to
    Milan they quarreled about her not being willing to come home at once. When they had to say good-bye, in the
    station at Milan, they kissed good-bye, but were not finished with the quarrel. He felt sick about saying good-bye
    like that.
    He went to America on a boat from Genoa. Luz went back to Pordonone to open a hospital. It was lonely
    and rainy there, and there was a battalion of arditi quartered in the town. Living in the muddy, rainy town in the
    winter, the major of the battalion made love to Luz, and she had never known Italians before, and finally wrote to
    the States that theirs had only been a boy and girl affair. She was sorry, and she knew he would probably not be able
    to understand, but might some day forgive her, and be grateful to her, and she expected, absolutely unexpectedly, to
    be married in the spring. She loved him as always, but she realized now it was only a boy and girl love. She hoped
    he would have a great career, and believed in him absolutely. She knew it was for the best.
    The major did not marry her in the spring, or any other time. Luz never got an answer to the letter to
    Chicago about it. A short time after he contracted gonorrhea from a sales girl in a loop department store while riding
    in a taxicab through Lincoln Park. 
 






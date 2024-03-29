Програмирање у Пајтону - текстуални подаци
==========================================

Постоје два основна формата рачунарских фајлова: текстуални и бинарни.
Текстуалне можемо да читамо и ми људи. Бинарни су резервисани за машине.
Фајлови са екстензијама .txt, .py, .csv или .srt (титл за филмове обично
има ову екстензију) су текстуални. Њих можемо да отворимо у било коме
едитору (нпр. *Notepad*) и да видимо текст, знакове интерпункције,
децималне бројеве, размаке итд. Бинарне фајлове (нпр. .zip, .docx или
.pdf) не можемо да отворимо у едиторима за текст. Чак и кад бисмо успели
на неки начин, видели бисмо бесмислени низ чудних знакова попут
``©ãGnû–¼5º¼Z6ÖÅ_¹.]p®\5«†`` који не бисмо знали да растумачимо.

Текстуални начин записивања података је веома практичан за памћење и
преношење података. Због тога се нпр. изворни кôд рачунарских програма и
табеларни подаци чувају као текст. Основни елемент ових записа је
**карактер**. То је једно слово, цифра, знак интерпункције или можда
неки контролни знак (нпр. знак за крај реда). Текст није ништа друго до
низ карактера. Тип података у Пајтону у који можемо да ставимо текст је
стринг (или ниска карактера).

Конверзија карактера у бајтове и обрнуто
----------------------------------------

Рачунар у својој меморији чува само нуле и јединице организоване у
бајтове. Без обзира на то што ми кажемо да су у некој променљивој карактери,
рачунар тим карактерима придружује број и онда тај број памти. Сваки
карактер има свој број. Ако је карактер из ASCII скупа од 256 знакова,
довољан је један бајт за чување. Уколико су то ћирилички знаци или знаци
са дијакритикама (нпр. *ž* или *ć*), за чување ће бити потребно два
бајта. Функција ``ord()`` нам даје број који је придружен знаку који
наводимо као аргумент. 

.. activecode:: konverzija_str
    :nocodelens:

    print(ord("a"))

У супротном смеру, функција ``chr()`` нам за број у аргументу враћа одговарајући карактер.

.. activecode:: konverzija_ord
    :nocodelens:

    print(chr(97))

Пробајте функцију ``ord()`` за различита ћирилична и латинична слова. Да
ли је број који добијате мањи или већи од 255? Ако је мањи или једнак,
за меморисање ће користити само један бајт.

За сваки број од 0 до 255 постоји одговарајући карактер. Неки од њих су
контролни па не можемо лепо да их прикажемо. Почевши од броја 32 који
одговара знаку ” ” то су „нормални“ карактери које можемо да испишемо.

.. activecode:: petlja_chr
    :nocodelens:

    for i in range(32,256):
        print(chr(i), end="")


.. questionnote:: 
    
    Напишите програм који генерише стринг са свим великим словима енглеског алфабета (ABCD…WXYZ) не укуцавајући ручно свако слово.

.. activecode:: string_slova
    :nocodelens:

    #ovde napiši program

Стринг као листа карактера
--------------------------

Стрингови се чувају као низови карактера. Пошто се у Пајтону низови
стандардно представљају листама, онда стринг овде представља листу
карактера. Начин на који приступамо карактерима у стрингу је исти као
што приступамо елементима у листи: помоћу индекса и слајсова.

.. activecode:: strin_lista
    :nocodelens:

    S="String je lista karaktera: slova, cifara i ostalih znakova."
    print(S[1])     # karakter sa indeksom 1
    print(S[3:6])   # slajs karaktera sa indeksima od 3 do 5
    print(S[-1])    # poslednji karakter u stringu


.. mchoice:: pajton_1
    :answer_a: 1 2 3
    :answer_b: 1 2 3 4
    :answer_c: 2
    :answer_d: 4 3 2 1
    :correct: d
    :feedback_a: Покушај поново!
    :feedback_b: Покушај поново!
    :feedback_c: Покушај поново!
    :feedback_d: Тачно!

    Шта је излаз следећег блока инструкција? 

    .. code-block:: python

        for i in [1, 2, 3, 4][::-1]:
            print (i)

   

Оператор ``in``
~~~~~~~~~~~~~~~

Када проверавамо да ли се одређени карактер или стринг (s) налазе у
неком већем стрингу (S), користимо оператор ``in``. Резултат операције је
булеан који има вредност тачно ако се s садржи у S, односно нетачно ако
тај услов није испуњен. Слично, можемо да проверимо и да ли се s не
садржи у S са ``not in``.

.. activecode:: in
    :nocodelens:

    S="String je lista karaktera: slova, cifara i ostalih znakova."
    print("ta" in S)     # string "ta" se pojavljuje u stringu S
    print(";" in S)      # znak ";" se ne pojavljuje u S
    print("R" not in S)  # tačno je da se "R" ne pojavljuje u S


Функције за рад са стринговима
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функције које имамо за рад са листама углавном постоје и за стрингове. У
следећој ћелији су примери две функције: прва враћа дужину стринга S,
док друга враћа број колико пута се карактер „а“ појављује у стрингу S.

.. activecode:: funkcije1
    :nocodelens:

    S="String je lista karaktera: slova, cifara i ostalih znakova."
    print(len(S))
    print(S.count("a"))



..  Questionnote:: 
    
    Напишите функцију која враћа број карактера у стрингу не користећи функцију ``len()``.


.. activecode:: funkcije2
    :nocodelens:

    s = 'neki_string'
    def duzina(a):
        # dopuni funkciju
        print(???)
    duzina(s)

..  Questionnote:: 
    
    Напишите функцију која враћа број знакова интерпункције.

.. activecode:: funkcije_interpuncija_stringovi
    :nocodelens:

    s = 'Prebroj koliko u ovoj rečenici ima znakova interpunkcije! Na primer: ! ili ? kao i . ili ,'
    def broj_znakova_interpunkcije(a):
        # dopuni funkciju
        print(???)
    broj_znakova_interpunkcije(s)

.. suggestionnote:: 
    
    Функција за рад са стринговима има више десетина. Овде их нећемо све помињати. Извршите ``dir(str)`` да видите које све постоје.

Функција ``.index()``
~~~~~~~~~~~~~~~~~~~~~

Уколико се „мали“ стринг (s) налази у „великом“ (S), функција
``.index()`` може да дам каже којим индексом великог стринга почиње
мали. Синтакса ове функције је ``S.index(s,start,end)``. Приметите да
функцију примењујемо на велики стринг, а да мали стављамо као њен
аргумент. Уколико унесемо само један аргумент, што је овде дозвољено,
функција ``.index()`` ће стринг s тражити почевши од индекса 0, тј. од
почетка великог стринга и вратиће нам само индекс где се стринг s први
пут појављује. Уколико унесемо и други аргумент функције (*start* -
индекс од ког почиње претрагу), можемо да нађемо и каснија појављивања.
Уколико желимо, можемо да ставимо и индекс (*end*) за крај претраге као
трећи аргумент.

.. activecode:: string_index
    :nocodelens:
    
    S="String je lista karaktera: slova, cifara i ostalih znakova."
    i=S.index("ta")           # gde se string "ta" prvi put pojavljuje u stringu S
    print(i)
    print(S.index("ta",i+1))  # gde se "ta" pojavljuje prvi put posle toga
    

Наравно, један стринг у другом може да се појави више пута. Немамо
функцију која аутоматски враћа све те позиције, али бисмо могли да је
напишемо помоћу петље, слајсова и функције ``.index()``.

.. questionnote:: 
    
    Напишите функцију која приказује све индексе са којима у стрингу S=“String je lista karaktera: slova, cifara i ostalih znakova.” почиње произвољни стринг s.

.. activecode:: funkcije3
    :nocodelens:

    S = 'String je lista karaktera: slova, cifara i ostalih znakova.'
    def index_podstringa(a):
        # dopuni funkciju
        print(???)
    index_podstringa(S)

Токенизација
------------

Анализа текста заснива се на анализи токена, односно јединица текста.
Токен може да буде слово, слог, реч, синтагма итд. Сваки текст у
дигиталном облику можемо да поделимо на токене и да их онда статистички
обрађујемо. Уколико текст није чист него има и контролне знакове, то
неће бити сасвим једноставно.

Једна од најважнијих функција за рад са стринговима је она која стринг
дели на делове и појединачне делове ставља у листу. У примеру где је
цела реченица један стринг, тај стринг можемо да поделимо на низ мањих у
којима су речи. Најједноставнији начин да то урадимо јесте да одвојимо
делове стринга између којих је размак, тј. знак ” “. Функција коју за то
користимо је ``.split()``. Аргумент ове функције може да буде било који
карактер. Уколико не наведемо који је, Пајтон ће подразумевати да је то
размак.

.. activecode:: tokenizacija
    :nocodelens:

    S="String je lista karaktera: slova, cifara i ostalih znakova."
    print(S.split())


Наравно, постоје детаљи, као што су знаци интерпункције, који нам не
дозвољавају да речи једноставно издвојимо као део стринга између два
размака. Згодно решење, мада ни оно није свеобухватно, јесте да прво
уклонимо све „проблематичне“ знаке помоћу функције ``.replace()``. Ова
функција има два аргумента којима означавамо који карактер у стрингу
желимо да заменимо којим другим. На пример, ако хоћемо да избришемо
тачку из стринга ``S``, онда карактер “.” мењамо празним стрингом ,
тј. са ““.

.. activecode:: tokenizacija2
    :nocodelens:

    S="String je lista karaktera: slova, cifara i ostalih znakova."
    S2=S.replace(".","")
    S2=S2.replace(",","")
    S2=S2.replace(":","")
    print(S2)


Функција која извршава супротну радњу од ``.split()`` je ``.join()``.
Она спаја елементе листе у један стринг раздвајајући их одређеним
карактером. Синтакса је мало необична јер се функција примењује на
сепаратор, а листа се наводи као аргумент. Свеједно, једноставна је за
употребу.

.. activecode:: spajanje
    :nocodelens:

    a = "_".join(["Ovo","treba","spojiti","donjom","crtom"])
    print(a)

Спајање стрингова
-----------------

Слично као и са листама, оператори ``+`` и ``*`` раде и са стринговима.
„Сабирање“ стрингова је заправо спајање два стринга у један, док је
„множење“ стринга неким природним бројем понављање истог стринга толико
пута.

.. activecode:: spajanje2   
    :nocodelens:

    s1="Prvi"
    s2="Drugi"
    print(s1+s2)
    print(s1*3)
    
.. mchoice:: pajton_2
    :answer_a: a
    :answer_b: abc
    :answer_c: bc
    :answer_d: bca
    :correct: b
    :feedback_a: Покушај поново!
    :feedback_b: Тачно!
    :feedback_c: Покушај поново!
    :feedback_d: Покушај поново!

    Шта је излаз следећег израза у Пајтону?

    .. code-block:: python

        "a"+"bc"
	  
Контролни карактери
-------------------

Како бисте у стринг ставили текст који у себи има део под наводницима,
нпр. ``OŠ "Vuk Karadžić"``? Ово не можемо да изведемо тако што просто у
стринг (који иначе стављамо под наводнике) убацимо још неколико истих
наводника. То би само разбило стринг на два и добили бисмо информацију
да унети кôд има синтаксну грешку. Пробајте.

Једно могуће решење је да унутар стринга који смо ставили између
двоструких наводника ставимо део текста под једноструким наводницима,
или обрнуто. То ће Пајтон разумети и прихватити.

.. activecode:: kotrnolni
    :nocodelens:

    s1="OŠ 'Vuk Karadžić', Loznica"  # prva mogućnost
    print(s1)
    s2='OŠ "Vuk Karadžić", Loznica'  # druga mogućnost
    print(s2)

Друго решење је да користимо контролне карактере. Има карактера који се
не исписују као „нормални“ знаци већ пребацују испис текста у нови ред,
враћају курсор за једно место уназад или додају већи размак (таб). За
њих постоје контролни кодови. Тај код је за нови ред ``\n``. Погледајте
како изгледа испис стринга у ком је садржан овај карактер.

.. activecode:: novired
    :nocodelens:

    print("Prvi red\ndrugi red")
    

За наводнике такође постоје контролни кодови. Потребно је само да испред
наводника ставимо обрнуту косу црту (*backslash*). Проблем од малопре са
наводницима у стрингу могли смо да решимо и овако.

.. activecode:: navodnici
    :nocodelens:

    s1="OŠ \"Vuk Karadžić\", Loznica"
    print(s1)
    

.. suggestionnote:: 
    
    Сви контролни кодови почињу обрнутом косом цртом. Ево неких од њих. Пробајте да их ставите у неки стринг који исписујете.

    ``\'`` једноструки наводници

    ``\"`` двоструки наводници

    ``\n`` крај реда

    ``\t`` таб

    ``\\`` обрнута коса црта

.. questionnote:: 
    
    Напишите Пајтон функцију која за два стринга утврђује да ли је први анаграм оног другог. На пример, стринг „I am Lord Voldemort” је анаграм стринга „Tom Marvolo Riddle”. Обратити пажњу на то да приликом провере да ли је један стринг анаграм оног другог празнине и величина слова не играју никакву улогу.


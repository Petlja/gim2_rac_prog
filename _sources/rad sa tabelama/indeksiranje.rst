
Индексирање и транспоновање табеле
----------------------------------

У овој лекцији говорићемо о: 

1. индексирању табеле ради флексибилнијег приступа елементима табеле;

2. приступу врстама и појединачним локацијама индексиране табеле;

3. рачунању са целим редовима и колонама табеле и 

4. транспоновању табеле.

Индексирање
~~~~~~~~~~~

Видели смо да је рад са колонама табеле веома једноставан.

Да бисмо могли да радимо са редовима табеле треба прво да нађемо једну
колону чија вредност једнозначно одређује цео ред табеле. На пример, у
табели са прошлог часа:

======= === ======= ==== ======
Ime     Pol Starost Masa Visina
======= === ======= ==== ======
Ana     ž   13      46   160
Bojan   m   14      52   165
Vlada   m   13      47   157
Gordana ž   15      54   165
Dejan   m   15      56   163
Đorđe   m   13      45   159
Elena   ž   14      49   161
Žaklina ž   15      52   164
Zoran   m   15      57   167
Ivana   ž   13      45   158
Jasna   ž   14      51   162
======= === ======= ==== ======

колона „Ime“ је таква колона (колона „Visina“ није погодна јер имамо
двоје деце са висином 165 цм, па, када кажемо „дете са висином 165“, није
јасно о коме се ради; исто тако ни колоне „Pol“, „Starost“ и „Masa“ нису
погодне).

Таква колона се зове кључ јер је она кључна за приступање редовима
табеле. Ако желимо да приступамо елементима табеле по редовима, морамо
систему да пријавимо коју колону ћемо користити као кључ. То се постиже
позивом функције ``set_index`` којој проследимо име колоне, а она врати
нову табелу „индексирану по датом кључу“:

.. code:: ipython3

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

Нова табела (``tabela1``) се од старе (``tabela``) разликује само по
томе што редови више нису индексирани бројевима (0, 1, 2...) већ именима
деце (Ana, Bojan, Vlada…). Ево старе (неиндексиране табеле) која има
колону „Ime“ и чији редови су индексирани бројевима:

.. code:: ipython3

    tabela




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Ime</th>
          <th>Pol</th>
          <th>Starost</th>
          <th>Masa</th>
          <th>Visina</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Ana</td>
          <td>ž</td>
          <td>13</td>
          <td>46</td>
          <td>160</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Bojan</td>
          <td>m</td>
          <td>14</td>
          <td>52</td>
          <td>165</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Vlada</td>
          <td>m</td>
          <td>13</td>
          <td>47</td>
          <td>157</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Gordana</td>
          <td>ž</td>
          <td>15</td>
          <td>54</td>
          <td>165</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Dejan</td>
          <td>m</td>
          <td>15</td>
          <td>56</td>
          <td>163</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Đorđe</td>
          <td>m</td>
          <td>13</td>
          <td>45</td>
          <td>159</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Elena</td>
          <td>ž</td>
          <td>14</td>
          <td>49</td>
          <td>161</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Žaklina</td>
          <td>ž</td>
          <td>15</td>
          <td>52</td>
          <td>164</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Zoran</td>
          <td>m</td>
          <td>15</td>
          <td>57</td>
          <td>167</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Ivana</td>
          <td>ž</td>
          <td>13</td>
          <td>45</td>
          <td>158</td>
        </tr>
        <tr>
          <th>10</th>
          <td>Jasna</td>
          <td>ž</td>
          <td>14</td>
          <td>51</td>
          <td>162</td>
        </tr>
      </tbody>
    </table>
    </div>



А ево и нове табеле у којој су редови индексирани именима деце:

.. code:: ipython3

    tabela1




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Pol</th>
          <th>Starost</th>
          <th>Masa</th>
          <th>Visina</th>
        </tr>
        <tr>
          <th>Ime</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Ana</th>
          <td>ž</td>
          <td>13</td>
          <td>46</td>
          <td>160</td>
        </tr>
        <tr>
          <th>Bojan</th>
          <td>m</td>
          <td>14</td>
          <td>52</td>
          <td>165</td>
        </tr>
        <tr>
          <th>Vlada</th>
          <td>m</td>
          <td>13</td>
          <td>47</td>
          <td>157</td>
        </tr>
        <tr>
          <th>Gordana</th>
          <td>ž</td>
          <td>15</td>
          <td>54</td>
          <td>165</td>
        </tr>
        <tr>
          <th>Dejan</th>
          <td>m</td>
          <td>15</td>
          <td>56</td>
          <td>163</td>
        </tr>
        <tr>
          <th>Đorđe</th>
          <td>m</td>
          <td>13</td>
          <td>45</td>
          <td>159</td>
        </tr>
        <tr>
          <th>Elena</th>
          <td>ž</td>
          <td>14</td>
          <td>49</td>
          <td>161</td>
        </tr>
        <tr>
          <th>Žaklina</th>
          <td>ž</td>
          <td>15</td>
          <td>52</td>
          <td>164</td>
        </tr>
        <tr>
          <th>Zoran</th>
          <td>m</td>
          <td>15</td>
          <td>57</td>
          <td>167</td>
        </tr>
        <tr>
          <th>Ivana</th>
          <td>ž</td>
          <td>13</td>
          <td>45</td>
          <td>158</td>
        </tr>
        <tr>
          <th>Jasna</th>
          <td>ž</td>
          <td>14</td>
          <td>51</td>
          <td>162</td>
        </tr>
      </tbody>
    </table>
    </div>



Колона „Ime“ је и даље присутна у табели ``tabela1``, али има посебан
статус. Ако покушамо да јој приступимо као „обичној“ колони

.. code:: ipython3

    tabela1["Ime"]

добићемо грешку. Међутим, она је ту као *индексна колона*:

.. code:: ipython3

    tabela1.index




.. parsed-literal::

    Index(['Ana', 'Bojan', 'Vlada', 'Gordana', 'Dejan', 'Đorđe', 'Elena',
           'Žaklina', 'Zoran', 'Ivana', 'Jasna'],
          dtype='object', name='Ime')



Приступ врстама и појединачним ћелијама индексиране табеле
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Структура података DataFrame је оптимизована за рад са колонама табеле.
Срећом, када имамо индексирану табелу као што је то ``tabela1``,
користећи „аксесоре“, тј. функције чији су аргументи индекси у угластим
заградама. Конкретно, помоћу аксесора ``loc`` (од енгл. *location*, што
значи „локација, положај, место“) можемо да приступамо редовима табеле,
као и појединачним ћелијама табеле.

Податке о појединачним редовима табеле можемо да видимо овако:

.. code:: ipython3

    tabela1.loc["Dejan"]




.. parsed-literal::

    Pol          m
    Starost     15
    Masa        56
    Visina     163
    Name: Dejan, dtype: object



Као аргумент аксесора ``.loc`` можемо да наведемо и распон, и тако ћемо
добити одговарајући део табеле:

.. code:: ipython3

    tabela1.loc["Dejan":"Zoran"]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Pol</th>
          <th>Starost</th>
          <th>Masa</th>
          <th>Visina</th>
        </tr>
        <tr>
          <th>Ime</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Dejan</th>
          <td>m</td>
          <td>15</td>
          <td>56</td>
          <td>163</td>
        </tr>
        <tr>
          <th>Đorđe</th>
          <td>m</td>
          <td>13</td>
          <td>45</td>
          <td>159</td>
        </tr>
        <tr>
          <th>Elena</th>
          <td>ž</td>
          <td>14</td>
          <td>49</td>
          <td>161</td>
        </tr>
        <tr>
          <th>Žaklina</th>
          <td>ž</td>
          <td>15</td>
          <td>52</td>
          <td>164</td>
        </tr>
        <tr>
          <th>Zoran</th>
          <td>m</td>
          <td>15</td>
          <td>57</td>
          <td>167</td>
        </tr>
      </tbody>
    </table>
    </div>



Ако као други аргумент аксесора ``.loc`` наведемо име колоне, рецимо
овако ``tabela1.loc["Dejan", "Visina"]``, добићемо информацију о
Дејановој висини.

.. code:: ipython3

    tabela1.loc["Dejan", "Visina"]




.. parsed-literal::

    163



Ево како можемо да добијемо информацију о телесној маси и висини
неколико деце:

.. code:: ipython3

    tabela1.loc["Dejan":"Zoran", "Masa":"Visina"]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Masa</th>
          <th>Visina</th>
        </tr>
        <tr>
          <th>Ime</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Dejan</th>
          <td>56</td>
          <td>163</td>
        </tr>
        <tr>
          <th>Đorđe</th>
          <td>45</td>
          <td>159</td>
        </tr>
        <tr>
          <th>Elena</th>
          <td>49</td>
          <td>161</td>
        </tr>
        <tr>
          <th>Žaklina</th>
          <td>52</td>
          <td>164</td>
        </tr>
        <tr>
          <th>Zoran</th>
          <td>57</td>
          <td>167</td>
        </tr>
      </tbody>
    </table>
    </div>



Рачун по врстама и колонама табеле
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Кренимо од једног примера. У ћелији испод дате су оцене неких ученика из
информатике, енглеског, математике, физике, хемије и ликовног:

.. code:: ipython3

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

Сада ћемо од ових података направити табелу чије колоне ће се звати
„Ime“, „Informatika“, „Engleski“, „Matematika“, „Fizika“, „Hemija“,
„Likovno“ и која ће бити индексирана по колони „Ime“:

.. code:: ipython3

    ocene = pd.DataFrame(razred)
    ocene.columns=["Ime", "Informatika", "Engleski", "Matematika", "Fizika", "Hemija", "Likovno"]
    ocene1 = ocene.set_index("Ime")
    ocene1




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Informatika</th>
          <th>Engleski</th>
          <th>Matematika</th>
          <th>Fizika</th>
          <th>Hemija</th>
          <th>Likovno</th>
        </tr>
        <tr>
          <th>Ime</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Ana</th>
          <td>5</td>
          <td>3</td>
          <td>5</td>
          <td>2</td>
          <td>4</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Bojan</th>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Vlada</th>
          <td>4</td>
          <td>5</td>
          <td>3</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Gordana</th>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Dejan</th>
          <td>3</td>
          <td>4</td>
          <td>2</td>
          <td>3</td>
          <td>3</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Đorđe</th>
          <td>4</td>
          <td>5</td>
          <td>3</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Elena</th>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>4</td>
          <td>2</td>
          <td>3</td>
        </tr>
        <tr>
          <th>Žaklina</th>
          <td>5</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Zoran</th>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>4</td>
          <td>3</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Ivana</th>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Jasna</th>
          <td>3</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
          <td>5</td>
        </tr>
      </tbody>
    </table>
    </div>



Ако желимо да израчунамо просек по предметима, треба на сваку колону ове
табеле да применимо функцију ``.mean``. Листа са именима свих колона
табеле ``ocene1`` се добија као ``ocene1.columns``, па сада само треба
да прођемо кроз ову листу и за сваку колону да израчунамо просек:

.. code:: ipython3

    for predmet in ocene1.columns:
        print(predmet, "->", round(ocene1[predmet].mean(), 2))


.. parsed-literal::

    Informatika -> 3.91
    Engleski -> 4.18
    Matematika -> 3.73
    Fizika -> 3.82
    Hemija -> 3.91
    Likovno -> 4.55
    

Да бисмо израчунали просечне оцене сваког ученика функцију ``.mean`` ћемо
применити на врсте табеле које добијамо позивом аксесора ``.loc``.
Погледајмо, прво, како то можемо да урадимо за једног ученика:

.. code:: ipython3

    print("Đorđe ima sledeće ocene:")
    print(ocene1.loc["Đorđe"])
    print("Prosek njegovih ocena je:", 
          round(ocene1.loc["Đorđe"].mean(), 2))  # računamo sr. vrednost ocena za Đorđa pa zaokružujemo na dve cifre"


.. parsed-literal::

    Đorđe ima sledeće ocene:
    Informatika    4
    Engleski       5
    Matematika     3
    Fizika         4
    Hemija         5
    Likovno        4
    Name: Đorđe, dtype: int64
    Prosek njegovih ocena je: 4.17
    

Списак свих ученика се налази у индексној колони, па просеке по свим
ученицима можемо да израчунамо овако:

.. code:: ipython3

    for ucenik in ocene1.index:
        print(ucenik, "->", round(ocene1.loc[ucenik].mean(), 2))


.. parsed-literal::

    Ana -> 4.0
    Bojan -> 5.0
    Vlada -> 4.17
    Gordana -> 5.0
    Dejan -> 3.17
    Đorđe -> 4.17
    Elena -> 3.0
    Žaklina -> 4.67
    Zoran -> 4.17
    Ivana -> 2.5
    Jasna -> 4.33
    

Ево и кратке видео-илустрације:

.. ytpopup:: fTmkDR6HLxI
    :width: 735
    :height: 415
    :align: center

Транспоновање табеле
~~~~~~~~~~~~~~~~~~~~

Замена врста и колона табеле се зове транспоновање. Приликом
транспоновања имена колона полазне табеле постају индекси нове табеле,
док индексна колона полазне табеле одређује имена колона нове табеле:

Транспоновање се често користи када табела има мало веома дугачких
редова, па је у неким ситуацијама лакше посматрати транспоновану табелу
која онда има много релативно кратких редова. Функције ``.head()`` и
``.tail()`` нам тада омогућују да се брзо упознамо са почетком и крајем
табеле и да стекнемо неку интуицију о томе како табела изгледа.

Важно је рећи и то да се са табелама може радити и без транспоновања,
јер све што можемо да урадимо на колонама табеле можемо да урадимо и на
врстама. И поред тога, транспоновање се често користи јер је библиотека
*pandas* оптимизована за рад по колонама табеле.

Табела се транспонује тако што се на њу примени функција ``.Т`` која као
резултат враћа нову, транспоновану табелу.

Ево примера са оценама:

.. code:: ipython3

    ocene1




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Informatika</th>
          <th>Engleski</th>
          <th>Matematika</th>
          <th>Fizika</th>
          <th>Hemija</th>
          <th>Likovno</th>
        </tr>
        <tr>
          <th>Ime</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Ana</th>
          <td>5</td>
          <td>3</td>
          <td>5</td>
          <td>2</td>
          <td>4</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Bojan</th>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Vlada</th>
          <td>4</td>
          <td>5</td>
          <td>3</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Gordana</th>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Dejan</th>
          <td>3</td>
          <td>4</td>
          <td>2</td>
          <td>3</td>
          <td>3</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Đorđe</th>
          <td>4</td>
          <td>5</td>
          <td>3</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Elena</th>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>4</td>
          <td>2</td>
          <td>3</td>
        </tr>
        <tr>
          <th>Žaklina</th>
          <td>5</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Zoran</th>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>4</td>
          <td>3</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Ivana</th>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Jasna</th>
          <td>3</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
          <td>5</td>
        </tr>
      </tbody>
    </table>
    </div>



Транспоновану табелу добијамо овако:

.. code:: ipython3

    ocene2 = ocene1.T

.. code:: ipython3

    ocene2




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th>Ime</th>
          <th>Ana</th>
          <th>Bojan</th>
          <th>Vlada</th>
          <th>Gordana</th>
          <th>Dejan</th>
          <th>Đorđe</th>
          <th>Elena</th>
          <th>Žaklina</th>
          <th>Zoran</th>
          <th>Ivana</th>
          <th>Jasna</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Informatika</th>
          <td>5</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
          <td>3</td>
          <td>4</td>
          <td>3</td>
          <td>5</td>
          <td>4</td>
          <td>2</td>
          <td>3</td>
        </tr>
        <tr>
          <th>Engleski</th>
          <td>3</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
          <td>3</td>
          <td>5</td>
          <td>5</td>
          <td>2</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Matematika</th>
          <td>5</td>
          <td>5</td>
          <td>3</td>
          <td>5</td>
          <td>2</td>
          <td>3</td>
          <td>3</td>
          <td>4</td>
          <td>4</td>
          <td>2</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Fizika</th>
          <td>2</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
          <td>3</td>
          <td>4</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>2</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Hemija</th>
          <td>4</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>3</td>
          <td>5</td>
          <td>2</td>
          <td>4</td>
          <td>3</td>
          <td>2</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Likovno</th>
          <td>5</td>
          <td>5</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>4</td>
          <td>3</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
        </tr>
      </tbody>
    </table>
    </div>



Хајде још да се уверимо да су врсте и колоне замениле места и у пољима
``index`` и ``columns``. У полазној табели је:

.. code:: ipython3

    ocene1.index




.. parsed-literal::

    Index(['Ana', 'Bojan', 'Vlada', 'Gordana', 'Dejan', 'Đorđe', 'Elena',
           'Žaklina', 'Zoran', 'Ivana', 'Jasna'],
          dtype='object', name='Ime')



.. code:: ipython3

    ocene1.columns




.. parsed-literal::

    Index(['Informatika', 'Engleski', 'Matematika', 'Fizika', 'Hemija', 'Likovno'], dtype='object')



У транспонованој табели је:

.. code:: ipython3

    ocene2.index




.. parsed-literal::

    Index(['Informatika', 'Engleski', 'Matematika', 'Fizika', 'Hemija', 'Likovno'], dtype='object')



.. code:: ipython3

    ocene2.columns




.. parsed-literal::

    Index(['Ana', 'Bojan', 'Vlada', 'Gordana', 'Dejan', 'Đorđe', 'Elena',
           'Žaklina', 'Zoran', 'Ivana', 'Jasna'],
          dtype='object', name='Ime')



Како смо раније већ видели, просек оцена по предметима добијамо лако:

.. code:: ipython3

    for predmet in ocene1.columns:
        print(predmet, "->", round(ocene1[predmet].mean(), 2))


.. parsed-literal::

    Informatika -> 3.91
    Engleski -> 4.18
    Matematika -> 3.73
    Fizika -> 3.82
    Hemija -> 3.91
    Likovno -> 4.55
    

Да бисмо добили просек оцена по ученицима, можемо да приступимо врстама
табеле користећи аксесор ``loc`` како смо то већ видели, али можемо и да
употребимо транспоновану табелу (рачунање просека по колонама, јер су
колоне транспоноване табеле заправо врсте полазне табеле):

.. code:: ipython3

    for ucenik in ocene2.columns:
        print(ucenik, "->", round(ocene2[ucenik].mean(), 2))


.. parsed-literal::

    Ana -> 4.0
    Bojan -> 5.0
    Vlada -> 4.17
    Gordana -> 5.0
    Dejan -> 3.17
    Đorđe -> 4.17
    Elena -> 3.0
    Žaklina -> 4.67
    Zoran -> 4.17
    Ivana -> 2.5
    Jasna -> 4.33
    
Задаци
~~~~~~~

.. technicalnote::

    Препоручујемо да примере из ове лекције покренеш на свом рачунару тако што ћеш у `пакету фајлова за вежбу <https://github.com/Petlja/gim2_rac_prog_radni/archive/refs/heads/master.zip>`_ покренути Џупитер свеску ``08_indeksiranje.ipynb``, или тако што ћеш отићи на `овај линк <https://petlja.github.io/gim2_rac_prog_radni/lab?path=08_indeksiranje.ipynb>`_ и тамо радити задатке. За детаљније инструкције погледај поглавље Фајлови за вежбу и коришћење Џупитер окружења.
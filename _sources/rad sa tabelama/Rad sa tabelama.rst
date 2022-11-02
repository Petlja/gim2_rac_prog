Рад са табелама
===============

До сада смо обрађивали и анализирали податке смештене у листе и
стрингове. Неке функције за рад са њима већ постоје у Пајтоновој
стандардној библиотеци, док смо за неке морали да пишемо своје функције.
Сада је тренутак да пређемо на следећи ниво – да податке организујемо у
табеле. Пракса нам говори да су табеларно сложени подаци најзгоднији за
употребу. Базе података све што имају чувају у разним табелама које
повезују по одређеним атрибутима или променљивим, како их зовемо у
Пајтону. За рад са табелама нам је неопходно да увеземо библиотеку која
табелу има као тип података. За ову намену најчешће коришћена библиотека
је *pandas*. Она има мноштво функција које ће нам олакшати посао. Неће
бити потребе да поново пишемо функције као што су биле оне за средњу
вредност или медијану.

Табеларно представљени подаци
-----------------------------

У овој лекцији ћемо говорити о:

1. представљању табеларно задатих података помоћу листи у Пајтону,

2. ефикаснијем представљању табеларних података користећи библиотеку pandas, 

3. визуелизацији табеларно представљених података, и 

4. учитавању табела из локалних и удаљених ресурса.

Представљање табеларно задатих података помоћу листи
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Најчешћи начин да организујемо велике количине података је да их
представимо табелом. Рецимо, ова табела садржи податке о једној групи
деце (при чему је, наравно, старост изражена у годинама, тежина у
килограмима, а висина у центиметрима):

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

Да бисмо могли машински да обрађујемо и анализирамо податке прво их
морамо представити у облику неке структуре података. Један једноставан
начин да се то уради је да сваки ред табеле представимо једном листом и
да потом све те листе запакујемо у једну велику листу, рецимо овако:

.. code:: ipython3

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

Из овако представљених података лако можемо добити податке о сваком
појединачном детету у групи. Рецимо, податке о Дејану добијамо тако што
испишемо елемент листе са индексом 4.

.. code:: ipython3

    podaci[4]




.. parsed-literal::

    ['Dejan', 'm', 15, 56, 163]



Овај начин представљања података, међутим, није погодан за обраде по
колонама. Рецимо, ако желимо да израчунамо просечну висину деце у групи,
морамо да пишемо програм. То није немогуће, чак није ни тешко, али је
непрактично. Ево програма:

.. code:: ipython3

  sum = 0                # početna vrednost sume je 0
  for dete in podaci:    # za svaki red u tabeli
      sum += dete[4]     # uzimamo vrednost sa indeksom 4 (visina) i dodajemo je na sumu
  sum/len(podaci)        # sumu na kraju delimo sa brojem redova tabele




.. parsed-literal::

    161.9090909090909



Програм ради на следећи начин: 

- прво помоћну променљиву ``sum`` поставимо на нулу (у њој ће се полако акумулирати збир висина све деце у групи),
- након тога циклус ``for dete in podaci:`` прође кроз свако дете у групи (јер сваки елемент листе ``podaci`` представља податке о једном детету) и на суму дода његову висину (висина детета се налази на петом месту у групи података за то дете, а то је елемент листе са индексом 4),
- коначно, добијени збир поделимо бројем података да бисмо израчунали просек.

Као што смо већ рекли, ово није нарочито тешко, али је непрактично. Треба
нам флексибилнија структура података.

Библиотека *pandas*, структура података *DataFrame* и рад са колонама табеле
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. technicalnote::

    Остатак ове лекције препоручујемо да читаш на свом рачунару тако што ћеш у `фолдеру за рад офлајн <https://github.com/Petlja/revizija_2_radni/archive/refs/heads/main.zip>`_ покренути Џупитер свеску `07_tabele.ipynb` на начин на који је то објашњено у поглављу `Покретање Џупитер радних свески <https://petlja.org/kurs/478/1/6141>`_ у уводу овог приручника, или тако што ћеш отићи на `овај линк <https://petlja.github.io/gim2_rac_prog_radni/lab/index.html>`_ и тамо радити задатке.  

За ефикасно манипулисање табеларно представљеним подацима у Пајтону
развијена је библиотека *pandas*. Њу можемо увести као што смо увозили и
остале библиотеке (и уз пут ћемо јој дати надимак да бисмо мање морали
да куцамо):

.. code:: ipython3

    import pandas as pd

Из ове библиотеке ћемо користити структуру података која се зове
*DataFrame* (енгл. *data* значи „подаци“, *frame* значи „оквир“, тако да
*DataFrame* значи „оквир са подацима“, односно „табела“).

Податке о деци сада лако можемо да препакујемо у *DataFrame* позивом
функције са истим именом:

.. code:: ipython3

    tabela = pd.DataFrame(podaci)

Претходна команда није дала никакав излаз. Она је просто препаковала
податке наведене у листи ``podaci`` у нову структуру података. Да бисмо
се уверили да се ради само о препакивању, исписаћемо садржај променљиве
``tabela``:

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
          <th>0</th>
          <th>1</th>
          <th>2</th>
          <th>3</th>
          <th>4</th>
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



Ево и кратког видеа:

.. ytpopup:: _AJYNXq53hk
    :width: 735
    :height: 415
    :align: center

Да би табела била прегледнија, даћемо колонама називе.
овако:

.. code:: ipython3

    tabela = pd.DataFrame(podaci)                               # tabelu iz formata liste pretvaramo u DataFrame
    tabela.columns=["Ime", "Pol", "Starost", "Masa", "Visina"]  # kolonama u tabeli pridružujemo nazive
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



Када свака колона има своје име, можемо да приступимо појединачним
колонама:

.. code:: ipython3

    tabela["Ime"]




.. parsed-literal::

    0         Ana
    1       Bojan
    2       Vlada
    3     Gordana
    4       Dejan
    5       Đorđe
    6       Elena
    7     Žaklina
    8       Zoran
    9       Ivana
    10      Jasna
    Name: Ime, dtype: object



.. code:: ipython3

    tabela["Visina"]




.. parsed-literal::

    0     160
    1     165
    2     157
    3     165
    4     163
    5     159
    6     161
    7     164
    8     167
    9     158
    10    162
    Name: Visina, dtype: int64



Имена свих колона су увек доступна у облику листе овако:

.. code:: ipython3

    tabela.columns




.. parsed-literal::

    Index(['Ime', 'Pol', 'Starost', 'Masa', 'Visina'], dtype='object')



Позивом једне од следећих функција лако можемо да вршимо елементарну
анализу података који су представљени табелом:

- ``.sum()`` – рачуна збир елемената у колони (сума),
- ``.mean()`` – рачуна средњу вредност елемената у колони,
- ``.median()`` – рачуна медијану елемената у колони,
- ``.min()`` – рачуна најмању вредност у колони (минимум),
- ``.max()`` – рачуна највећу вредност у колони (максимум).

На пример, висина најнижег детета у групи је:

.. code:: ipython3

    tabela["Visina"].min()




.. parsed-literal::

    157



Најстарије дете у групи има оволико година:

.. code:: ipython3

    tabela["Starost"].max()




.. parsed-literal::

    15



Средња вредност висине деце у групи је:

.. code:: ipython3

    tabela["Visina"].mean()




.. parsed-literal::

    161.9090909090909



Медијална висина:

.. code:: ipython3

    tabela["Visina"].median()




.. parsed-literal::

    162.0



Да ли цела група може да стане у лифт чија носивост је 600 кг?

.. code:: ipython3

    if tabela["Masa"].sum() <= 600:
        print("Mogu svi da stanu u lift.")
    else:
        print("Ne. Zajedno su preteški.")


.. parsed-literal::

    Mogu svi da stanu u lift.

Пример скупа података за пројектно учење
========================================

Идеја пројектног учења је да оно што сте научили примените на конкретан
проблем и онда пустите исти тај проблем да вас још нешто научи. При
томе, наравно, нико не очекује да решавање проблема буде праволинијско.
Има детаља којих ћете морати да се подсетите, док ћете неке трикове
„успут“ морати да научите. Тражење сличних примера и решења је увек
дозвољено и врло пожељно.

.. technicalnote::

    Препоручујемо да примере из ове лекције покренеш на свом рачунару тако што ћеш у `пакету фајлова за вежбу <https://github.com/Petlja/gim2_rac_prog_radni/archive/refs/heads/master.zip>`_ покренути Џупитер свеску ``11_projektna.ipynb``, или тако што ћеш отићи на `овај линк <https://petlja.github.io/gim2_rac_prog_radni/lab?path=11_projektna.ipynb>`_ и тамо радити задатке. За детаљније инструкције погледај поглавље Фајлови за вежбу и коришћење Џупитер окружења.

Пројектни задатак – Квалитет ваздуха
------------------------------------

Ваш пројектни задатак је да обрадите податке о квалитету ваздуха у
Србији који су доступни на `Порталу отворенихподатака <https://data.gov.rs/en/datasets/kvalitet-vazduha/>`__.
Оно што нас посебно интересује су различити параметри квалитета ваздуха
прикупљени са свих доступнх станица у последњих месец дана. Јасно вам
је да се ови подаци стално ажурирају због чега нема смисла да их
учитавамо из унапред припремљеног фајла. Табелу са овим подацима морамо
да преузмемо директно са веб-сајта који објављује последње доступне
податке. На овој страни имате више табела (скупова података) у
различитим форматима. Осим табеле у којој су тражени подаци за последњих
месеца дана (`Kvalitet vazduha po
stanicama <http://data.sepa.gov.rs/dataset/11104dfd-b110-4b25-b350-9253e9233b6b/resource/0b6a7aa5-9b13-4a7c-8a80-f964e1c67bc3/download/air_quality_by_station.csv>`__)
још две су нам потребне: `Stanice za merenje kvaliteta vazduha -
šifarnik <http://data.sepa.gov.rs/dataset/11104dfd-b110-4b25-b350-9253e9233b6b/resource/dd7f4e4b-2375-4657-bb91-d541a2759891/download/station.csv>`__
и `Merene komponente -
šifarnik <http://data.sepa.gov.rs/dataset/11104dfd-b110-4b25-b350-9253e9233b6b/resource/7fa4ab3f-423a-4016-8508-37164b49c087/download/component.csv>`__.
Тренутно су ове табеле доступне на локацијама датим у хиперлинку. Могуће
је да Портал промени локацију ових фајлова у будућности. Погледајте онда
који је “*Latest URL*” за одговарајући скуп података и примените га.

Конкретно, изаберите вама најближу станицу која прикупља тражене
параметре ваздуха. Изаберите параметар или параметре које желите да
анализирате и прикажете. Проверите да ли та станица стварно има податке
за тражени период. Издвојте потребне податке из табеле са свим доступним
подацима. Прикажите податке као временску серију (време мерења на
*x* оси, параметар на *y* оси) и као хистограм за вредности изабраног
параметра. Покушајте да протумачите резултате и видите колико често је
квалитет ваздуха био одличан, добар, прихватљив, загађен или незагађен. Ово тумачење није једноставно. Можда вам помогне текст `CAQI,
AQI, SAQI… Srbiji treba jasan pristup tumačenju zagađenosti
vazduha <https://balkangreenenergynews.com/rs/caqi-aqi-saqi-srbiji-treba-jasan-pristup-tumacenju-zagadenosti-vazduha/>`__.

Прво увезите библиотеке за рад са табелама и цртање графикона.

.. code:: ipython3

    import pandas as pd
    import matplotlib.pyplot as plt

На основу URL адреса које се завршавају са CSV, јасно је да су фајлови
које треба учитати управо у овом формату. Оно што се не види из адресе
јесте који је сепаратор коришћен за одвајање суседних вредности.
Подразумева се да је зарез тај сепаратор, али то у већини европских
земаља није згодно јер се децимални бројеви пишу са зарезом. Због тога
се као сепаратор често користи знак тачка зарез (;). У Србији се користе обе
варијанте. Који је сепаратор у ком фајлу коришћен, углавном видимо тек
кад учитавање са једним од њих не успе, односно кад добијемо нераздојене
вредности. У сваком случају, учитајте све три табеле помоћу функције
``pd.read_csv()``.

.. code:: ipython3

    stanice=pd.read_csv('https://data.gov.rs/en/datasets/r/dd7f4e4b-2375-4657-bb91-d541a2759891',sep=";")
    komponente=pd.read_csv('https://data.gov.rs/en/datasets/r/7fa4ab3f-423a-4016-8508-37164b49c087',sep=";")
    podaci=pd.read_csv('https://data.gov.rs/en/datasets/r/0b6a7aa5-9b13-4a7c-8a80-f964e1c67bc3',sep=",")

.. code:: ipython3

    podaci.head()




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
          <th>date_time</th>
          <th>station_id</th>
          <th>so2</th>
          <th>pm10</th>
          <th>o3</th>
          <th>no2</th>
          <th>nox</th>
          <th>co</th>
          <th>benzene</th>
          <th>toluene</th>
          <th>no</th>
          <th>pm2_5</th>
          <th>pm1</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>2022-06-24 00:00:00</td>
          <td>1</td>
          <td>10.549119</td>
          <td>NaN</td>
          <td>57.495900</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>0.178599</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>2022-06-24 00:00:00</td>
          <td>2</td>
          <td>8.010171</td>
          <td>18.566102</td>
          <td>NaN</td>
          <td>47.382533</td>
          <td>68.781508</td>
          <td>0.157805</td>
          <td>0.227148</td>
          <td>6.058088</td>
          <td>13.80288</td>
          <td>12.512833</td>
          <td>10.150000</td>
        </tr>
        <tr>
          <th>2</th>
          <td>2022-06-24 00:00:00</td>
          <td>3</td>
          <td>5.254099</td>
          <td>NaN</td>
          <td>51.986375</td>
          <td>15.060899</td>
          <td>21.328835</td>
          <td>0.273868</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>4.07056</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>3</th>
          <td>2022-06-24 00:00:00</td>
          <td>4</td>
          <td>18.783293</td>
          <td>2.522000</td>
          <td>NaN</td>
          <td>6.210549</td>
          <td>11.375379</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>3.36544</td>
          <td>2.115254</td>
          <td>1.659932</td>
        </tr>
        <tr>
          <th>4</th>
          <td>2022-06-24 00:00:00</td>
          <td>5</td>
          <td>11.628788</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>13.173505</td>
          <td>23.608374</td>
          <td>0.291652</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>6.82448</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



Примећујемо да су у колони ``date_time`` датум и време мерења. Судећи по
првих пет редова, мерења су бележена на сваких сат времена. Да бисмо ову
колону могли да користимо као континуалну независно променљиву, потребно
је да буде препозната као тип ``datetime``. То се вероватно није
догодило. Пајтон при учитавању податка из фајла покушава да препозна тип
податка који је заједнички за све елементе сваке појединачне колоне, али
ће целу колону оставити као објекат, односно колону стрингова уколико
има икакву дилему. Проверите помоћу функције ``.dtypes`` који су типови
податка у појединачним колонама табеле.

.. code:: ipython3

    podaci.dtypes




.. parsed-literal::

    date_time      object
    station_id      int64
    so2           float64
    pm10          float64
    o3            float64
    no2           float64
    nox           float64
    co            float64
    benzene       float64
    toluene       float64
    no            float64
    pm2_5         float64
    pm1           float64
    dtype: object



Функција ``.to_datetime()`` ће претворити све текстуалне податке у датум
и време уколико је то могуће. Урадите то за све вредности у колони
``date_time``.

.. code:: ipython3

    podaci.date_time=pd.to_datetime(podaci.date_time)

Подаци у табели ``stanice`` садрже називе станица и њихове географске
локације. То су кључни подаци помоћу којих ћемо закључити која је
станица најближа. Пошто имена променљивих нису иста у свим табелама,
потребна нам је вредност ``id`` из табеле ``stanice`` која одговара
вредности ``station_id`` у табели ``podaci``. У табели ``komponente`` су
пуни називи и јединице мерених компоненти. Ови подаци су неопходни да
бисмо могли да тумачимо резултате.

.. code:: ipython3

    stanice.head()




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
          <th>id</th>
          <th>k_eoi_code</th>
          <th>k_airbase_code</th>
          <th>k_network_id</th>
          <th>k_local_code</th>
          <th>k_name</th>
          <th>k_start_date</th>
          <th>k_stop_date</th>
          <th>latitude</th>
          <th>longitude</th>
          <th>altitude</th>
          <th>aq_stationclassification</th>
          <th>aq_areaclassification</th>
          <th>k_char_of_zone</th>
          <th>k_ozone_classification</th>
          <th>k_main_emission_source</th>
          <th>k_city</th>
          <th>k_city_population</th>
          <th>k_street_name</th>
          <th>k_report</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>1</td>
          <td>RS1002A</td>
          <td>RS0034A</td>
          <td>1</td>
          <td>0001</td>
          <td>Kikinda Centar</td>
          <td>2010-02-01</td>
          <td>NaN</td>
          <td>45.821483</td>
          <td>20.454008</td>
          <td>78.0</td>
          <td>background</td>
          <td>urban</td>
          <td>residential</td>
          <td>suburban</td>
          <td>Agriculture</td>
          <td>Kikinda</td>
          <td>38.0</td>
          <td>Svetosavska bb</td>
          <td>t</td>
        </tr>
        <tr>
          <th>1</th>
          <td>2</td>
          <td>RS1007A</td>
          <td>RS0029A</td>
          <td>1</td>
          <td>1007</td>
          <td>Novi Sad SPENS</td>
          <td>2015-06-08</td>
          <td>NaN</td>
          <td>45.245065</td>
          <td>19.841190</td>
          <td>78.0</td>
          <td>traffic</td>
          <td>urban</td>
          <td>residential/commercial</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>Novi Sad</td>
          <td>342.0</td>
          <td>Bulevar oslobodjenja</td>
          <td>t</td>
        </tr>
        <tr>
          <th>2</th>
          <td>3</td>
          <td>RS1008A</td>
          <td>RS0031A</td>
          <td>1</td>
          <td>1008</td>
          <td>Novi Sad Liman</td>
          <td>2015-06-01</td>
          <td>NaN</td>
          <td>45.238642</td>
          <td>19.835704</td>
          <td>81.0</td>
          <td>background</td>
          <td>urban</td>
          <td>residential</td>
          <td>urban</td>
          <td>NaN</td>
          <td>Novi Sad</td>
          <td>342.0</td>
          <td>Narodnog fronta 45</td>
          <td>t</td>
        </tr>
        <tr>
          <th>3</th>
          <td>4</td>
          <td>RS1009A</td>
          <td>RS0001A</td>
          <td>1</td>
          <td>1009</td>
          <td>Beočin Centar</td>
          <td>2015-07-02</td>
          <td>NaN</td>
          <td>45.208386</td>
          <td>19.721709</td>
          <td>87.0</td>
          <td>background</td>
          <td>urban</td>
          <td>residential/industrial</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>Beočin</td>
          <td>15.0</td>
          <td>Kralja Petra bb</td>
          <td>t</td>
        </tr>
        <tr>
          <th>4</th>
          <td>5</td>
          <td>RS1010A</td>
          <td>RS1010A</td>
          <td>1</td>
          <td>1010</td>
          <td>Sremska Mitrovica</td>
          <td>2015-07-02</td>
          <td>NaN</td>
          <td>44.972185</td>
          <td>19.609349</td>
          <td>82.0</td>
          <td>traffic</td>
          <td>urban</td>
          <td>residential/commercial</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>Sremska Mitrovica</td>
          <td>86.0</td>
          <td>NaN</td>
          <td>t</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    print("Najbliža stanica je", stanice['k_name'].iloc[0], "sa vrednošću id=", stanice['id'][0],".")


.. parsed-literal::

    Najbliža stanica je Kikinda Centar sa vrednošću id= 1 .
    

Обратите пажњу да неименовани индекс табеле није исти као вредност
променљиве која се налази у колони ``id``. Да бисмо издвојили, тј.
филтрирали табелу ``podaci`` по тој вредности, треба да је препознамо у
колони ``station_id``.

Сад кад имате све тражене табеле и податке одговарајућег типа, треба да
издвојите само оне податке који се тичу вама најближе станице. У примеру
који следи узета је станица са индексом 0. Ако ваша најближа станица
није „Кикинда Центар“, унесите прави индекс у приступник тамо где треба.

.. code:: ipython3

    podaci_najbliza=podaci.loc[podaci['station_id']==1]

Користите функцију ``.head()`` да проверите има ли података за тражену
станицу у последњих месец дана. Ако их из било којих разлога нема, онда
узмите другу најближу станицу.

.. code:: ipython3

    podaci_najbliza.head()




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
          <th>date_time</th>
          <th>station_id</th>
          <th>so2</th>
          <th>pm10</th>
          <th>o3</th>
          <th>no2</th>
          <th>nox</th>
          <th>co</th>
          <th>benzene</th>
          <th>toluene</th>
          <th>no</th>
          <th>pm2_5</th>
          <th>pm1</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>2022-06-24 00:00:00</td>
          <td>1</td>
          <td>10.549119</td>
          <td>NaN</td>
          <td>57.495900</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>0.178599</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>61</th>
          <td>2022-06-24 01:00:00</td>
          <td>1</td>
          <td>9.001029</td>
          <td>NaN</td>
          <td>46.433625</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>0.170444</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>122</th>
          <td>2022-06-24 02:00:00</td>
          <td>1</td>
          <td>8.604286</td>
          <td>NaN</td>
          <td>37.881725</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>0.168619</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>183</th>
          <td>2022-06-24 03:00:00</td>
          <td>1</td>
          <td>8.970360</td>
          <td>NaN</td>
          <td>29.526000</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>0.158601</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>244</th>
          <td>2022-06-24 04:00:00</td>
          <td>1</td>
          <td>8.687549</td>
          <td>NaN</td>
          <td>28.728000</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>0.203100</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



Ми ћемо, примера ради, да прикажемо измерене вредности из прве колоне са
параметрима квалитета ваздуха, :math:`SO_2`. Ви изаберите који желите. Иако
нам је за цртање овог графика потребна само једна линија кôда, ми ћемо
да бисмо побољшали изглед графика, употребити још три. Подразумевани график
у Џупитеру је прилично узан због чега није погодан за дуже временске
серије. Да би график покрио ширину расположивог екрана, ставићемо да су
димензије графика 18 пута 6 инча. Друго, временске ознаке садрже велики
број карактера па се зато преклапају ако их све хоризонтално испишемо на
*x* оси. То можемо да решимо ако ознаке исписујемо вертикално. Треће,
ставићемо мрежу (*grid*) преко графика како бисмо лакше очитавали
вредности.

.. code:: ipython3

    plt.figure(figsize=(18,6)) # dimenzije grafika
    plt.plot(podaci_najbliza['date_time'],podaci_najbliza['so2'])
    plt.xticks(rotation=90);   # date_time podatke ispisujemo vertikalno
    plt.grid()



.. image:: ../../_images/output_23_01.png


Исте ове податке можемо да прикажемо и хистограмом. Тада ћемо јасно
видети расподелу измерених вредности, односно колико је пута очитана
која вредност за месец дана. Са друге стране, изгубићемо информацију о
времену када је вршено мерење. Да би график био прегледнији, нагласићемо
да интервал од 0 до 30 делимо на 30 делова.

.. code:: ipython3

    podaci_najbliza['so2'].hist(bins=30,range=(0,30))




.. parsed-literal::

    <AxesSubplot:>




.. image:: ../../_images/output_25_11.png


Овде анализа података о квалитету ваздуха тек почиње. Тумачење ћемо
препустити вама. Још боље би било да то радите тимски са професорима у
школи. Уз мало труда, могли бисте да на направите „контролну таблу“ где
би у рeалном времену били исцртавани актуелни подаци са упозорењем када
је квалитет ваздуха испод прихватљивог нивоа.
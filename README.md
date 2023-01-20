<h1 align="center"> :computer: Это репозиторий для анализа новостного сайта :computer: novostivolgograda</h1>
<h3 align="center"> (ссылка: https://www.novostivolgograda.ru/) </h3>

### Наш программный модуль умеет следующее: 
### :heavy_check_mark: "Парсинг" 10 000 новостных статей с сайта novostivolgograda,
### :heavy_check_mark: Выявление упоминаний об известных людях Волгограда,
### :heavy_check_mark: Выявление упоминаний об известных местах Волгограда, 
### :heavy_check_mark: Отображение проанализированной информации на веб-странице,
### :heavy_check_mark: Хранение данных в БД,
### :heavy_check_mark: Анализ тональности высказывания об известных людях и местах Волгограда, 
### :heavy_check_mark: Выявлять контекстные синонимы для известнхы людей и мест Волгограда,
### :heavy_check_mark: Вычисление среднего рейтинга п оперсоне или месту Волгограда на основе проанализирвоаннхы статей,
### :heavy_check_mark: Предоставлять визуализацию статистики упоминаний и тональности
#
<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>

<h3 align="center"> :fire: Наша команда: :fire: </h3>

#### :construction_worker: Samorokov Nikolay (nickname на GitHub: QuanRy)
#### :cop: Grigoriev Ivan (nickname на GitHub: Negibkaya)
#### :guardsman: Novruzov Sergey (nickname на GitHub: Sergey854223)

<h3 align="center"> :mag_right: Распределение обязанностей: :mag_right: </h3>

#### :hammer: Samorokov Nikolay (QuanRy) IVT-363 спарсил сайт (https://www.novostivolgograda.ru/). Новости помещаются в базу данных, далее хранятся там (если  новость уже присутствует в БД она не заносится в нее, а игнорируется). В качетсве БД используется SQlite
#### :wrench: Grigoriev Ivan (Negibkaya) IVT-363 оформил веб-интерфейс, выделил среди всех новостей, хранящихся в БД, с помощью tomita-парсера упоминание значимых персон Волгоградской области и достопримечательностей. Зафиксировал в БД предложения с их упоминанием для дальнейшего анализа тональности.
#### :nut_and_bolt: Novruzov Sergey (Sergey854223) IVT-363 проанализировал имеющиеся упоминания об известных людях и достопримечательностях в БД и выделил их "тональность". Создал программный модуль для проведения с помощью Spark MlLib анализа модели Word2Vec на всем объеме новостных статей из БД. Для персон Волгоградской области и достопримечательностей определил контекстные синонимы и слова, с которыми они упоминались в тексте.

<div id="header" align="ri">
  <img src="https://raw.githubusercontent.com/trinib/trinib/a5f17399d881c5651a89bfe4a621014b08346cf0/images/marquee.svg" width="1000"/>
</div>

<div id="header" align="center">
  <img src="https://raw.githubusercontent.com/trinib/trinib/82213791fa9ff58d3ca768ddd6de2489ec23ffca/images/footer.svg" width="1000"/>
</div>

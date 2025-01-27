"""
Prestanda, förenklingar och ekonomi

Här ska jag försöka mig på att förklara behovet att förminska en bild och att förenkla en bild för att den ska ta mindre tid att processa.

Jag använder bilden på vår klass som är tagen med en iPhone och relativt utzoomad. Den bilden är 1,6MB stor - hyffsad standardstorlek för ett fotografi med mobilkamera.
I sitt orginalckick är bilden 3264 × 2448 pixlar. Dvs 7 990 272 pixlar. Betänker vi att man behöver 10 000 bilder för att träna en modell så landar vi på att beräkningarna måste, om bilden inte först manipuleras, göras nästan 80 miljarder gånger.
Att göra den kalkylen och den testmatrisen Linus skrev (100 000 rader med 10 kategorier i varje, alltså 100 000 "pixlar") tog knappt fem sekunder. Den träningsdatan har flertalet skillnader från en bild, för att inte tala om att en bild kan behöva bearbetas i flera nivåer per pixel.
"""
time_to_process_one_picture_with_yolo_object_detection = 5*60

"""
att generera 10 000 rader i databasen:
[2025-01-27 01:01:17] 10,000 rows affected in 179 ms
"""

performance_chart = {
    'grunddata':['Linus 100 000 rader','klassbilden'],
    'tidsåtgång':[f'{5/60/60} timmar',f'{time_to_process_one_picture_with_yolo_object_detection}']
}

# 100 000 rader, multipliceras med 10 weights tog 43 ms
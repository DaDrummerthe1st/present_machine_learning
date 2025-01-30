from hashlib import sha256

import streamlit as st
import pandas as pd
from requests import session

from libraries.model_learning.logistic_regression import ModelTraining
from libraries.file_handling.list_files import CollectFiles
from libraries.database.connect import DbConnection
from libraries.file_handling.list_files import CollectFiles
from libraries.generate_data.hash import Hash

# retrieving example data
model = ModelTraining()
X = model.create_X()

# initialising Hash
hash_creation = Hash()

description, mockup, results = st.tabs(['Beskrivning', 'Mockup', 'Resultaten'])

with description:
    brief_info, data_handling, information_sources, methods, hashtag = st.tabs(
        ['Introduktion', 'Datahantering', 'Informationskällor', 'Metoderna', 'Hashtag'])
    with brief_info:
        st.header('Differentiate Pictures for Auto Sync')
        st.image('static/media/qr/differentiate_pictures_for_auto_sync.png')
        st.link_button("Länk till repot på Github",
                       "https://github.com/DaDrummerthe1st/differentiate-pictures-for-auto-sync",
                       icon=":material/link:")

        st.markdown("""
        DPFAS är ett tankeexperiment, som kanske någon gång ser dagens ljus.
        
        **Målet** är att minimera utrymmet mediafiler tar upp genom att bl a föreslå bilder att ta bort, enligt användarens tidigare mönster.
    
        Framtida användning kan även inkludera att komprimera, beskära, tagga filer samt flytta filer mellan enheter etc.
    
        Det är en app för alla enheter användaren har bilder på.
        
        Den består i ett användarinterface för att lära modellen och flertalet maskinlärningsmetoder samt flertalet maskininlärningsmodeller bakom denna.
        """)

    with data_handling:
        st.subheader("Datahantering")
        st.markdown("""
        Bakom kulisserna sparar modellen stora mängder metadata om bilden och lär sig korrelationen mot användningen.
        Varje bild går igenom några faser:
        1. Bildens metadata sparas i en tabell. Det kan röra sig om kamerainformation och gps-positioner från [EXIF-data](https://en.wikipedia.org/wiki/Exif)), sökväg och storlek
        2. Bilden kategoriseras med ett antal metoder enligt en given mall (se nästa flik)
        3. Användarens användning av bilden (alltså metadata om t ex hur ofta användaren flyttat eller på annat sätt manipulerat bilden i numerärt förhållande till andra bilder, användarens olika labels etc)
        4. En matris skapas över all information om bilden - alltså är matrisen en representation av bilden och inte själva bilden.
        5. Bilden får ett unikt namn, som tas fram genom en hash-process inkluderat all framtagen META-data
        """)

    with information_sources:
        st.header('Sammansättning')
        st.markdown("""
        När en fil läses in har den flertalet egenskaper
        #### Filinformation
        Filnamn, sökväg, storlek, filtyp
        #### Metadata
        - Datum den skapades o senast ändrades
        - Storlek
        - Format (x * y pixlar)
        ##### EXIF-data
        - Kamerainformation, kamerainställningar
        - GPS-koordinater
        - Användarinformation
        ##### Underlag för ID genom hashtag
        Denna information används för att skapa ett unikt ID för varje bild men också för att förutspå användarens intention med bilden.
        I den händelse bilden ändras så skapas också ett nytt id
        """)

    with methods:
        st.markdown("""
        Samtliga nedanstående egenskaper är probabiliteter framtagna av anpassade modeller.
        
        Vissa kategorier kan vara flerdimensionella i sig själva. Det är här komplexiteten men också logiken börjar bli tydlig!
        
        I många av metoderna minskar man mängde processad data genom att "förenkla" bilden. Man kan t ex omvandla bilden till gråskala innan modellen körs.
        """)
        # TODO: visa på potentiella modeller för resp kategori
        categories = pd.Series(model.categories)
        technologies_used = pd.Series(
            ['OpenCV', 'YOLO', 'YOLO', 'OpenCV, (OCR)', 'PIL._getexif()', 'Python module os', '', '', 'OpenCV',
             'OpenCV'])
        headlines = ['Attribute', 'Technology used']
        # categories_techs = pd.concat([pd.DataFrame(model.categories), pd.DataFrame(technologies_used)], axis=1)
        categories_techs = pd.concat([categories.rename(headlines[0]), technologies_used.rename(headlines[1])], axis=1)
        # categories_techs = pd.DataFrame(categories_techs, columns=headlines)
        print(categories_techs)
        st.dataframe(categories_techs, use_container_width=True, hide_index=True)
        opencv, yolo = st.tabs(['OpenCV', 'YOLO'])

        with opencv:
            st.image('static/media/OpenCV_logo_white_.png', width=100)
            st.markdown("""
            OpenCV är världens största computer vision-bibliotek, det är dessutom open source och väldigt väl underhållet.
            Den innehåller enorma mängder färdigtränade modeller för olika typer av applikationer.OpenCV finns tillgänglig för flertalet programmeringsspråk, däribland Python och C[++].
            """)
        with yolo:
            st.header('YOLO - You Only Look Once')
            st.markdown("""Lägg namnet Joseph Redmond på minnet!""")
            st.markdown("""
            Började som en forskningsartikel, övergick till ett community, där grundaren lämnade eftersom han insåg hur objektidentifikation nu hade effektiviserats så mycket att bl a mycket små drönare skulle kunna skickas ut och ha ihjäl människor med extrem precision.
            """)
            st.link_button('Killer Drones', 'https://www.youtube.com/watch?v=TlO2gcs1YvM')
            col1, col2, col3 = st.columns(3)
            col1.image('static/media/qr/article_about_yolo_and_joseph_redmond.png', caption='Article about Yolo and Joseph Redmond')
            col2.image('static/media/qr/yolos_first_homepage.png', caption='YOLOs first homepage')
            col3.image('static/media/qr/facial_recognition_drones_military.png', caption='Facial recognition drones military')

    with hashtag:
        st.header('Hur byggs en hashtag?')
        with st.echo():
            # from hashlib import sha256

            inputinformation = "ett ord"
            st.write(sha256(inputinformation.encode('utf-8')).hexdigest())
            st.write(sha256(str(model.categories).encode('utf-8')).hexdigest())
        st.markdown("""
        #### TL;DR
        Förenklat kan man säga att en input-textsträng räknar fram en output, bestående av ett förutbestämt antal tecken.
        #### Kryptering
        Det är oftast väldigt svårt att reverse engineera en hashtag - vilket gör de optimala för kryptering. När du skriver in ditt lösenord på en sida på nätet så skickas endast hashtagen till hemsidan, som sedan jämförs med den i databasen sparade hashtagen. Inget lösenord är därmed synligt och inte heller längde går att gissa.
        #### Representation
        I DPFAS representeras varje filidentifiering av en hash, som räknas fram enligt ovan. Denna utgör därmed en unik nyckel i tabellerna.
        Det betyder att "samma" fil, som blir manipulerad och därmed får andra förutsättningar, också få en annan hash.
        Systemet med hashar (med tillräckligt hög upplsning) medger också att det finns ett mycket stort antal potentiella nycklar. 
        """)

with mockup:
    st.header('Delete or Keep?')

    path = 'static/media/demopictures/accumulated'
    files = CollectFiles(path=path)
    files.make_list_of_files()

    col1, col2 = st.columns(2)

    result = [None, None]
    if 'file_index' not in st.session_state:
        st.session_state['file_index'] = 0

    this_picture_id = hash_creation.sha256(files.files_list[st.session_state['file_index']])
    result[0] = col1.button('delete', icon=':material/delete:')
    result[1] = col2.button('save', icon=':material/save:')
    #st.write(st.session_state['file_index'])
    if result[0]:
        # save file_id to database as deleted and move to next
        if st.session_state['file_index'] == len(files.files_list):
            st.image(files.files_list[st.session_state['file_index']])
            st.session_state.file_index += 1
        elif st.session_state['file_index'] < len(files.files_list):
            st.image(files.files_list[st.session_state['file_index']])
            st.session_state.file_index += 1
        elif st.session_state['file_index'] > len(files.files_list):
            st.session_state.file_index = 0
            st.image(files.files_list[st.session_state['file_index']])

    if result[1]:
        if st.session_state['file_index'] == len(files.files_list):
            st.image(files.files_list[st.session_state['file_index']])
            st.session_state.file_index += 1
        elif st.session_state['file_index'] < len(files.files_list):
            st.image(files.files_list[st.session_state['file_index']])
            st.session_state.file_index += 1
        elif st.session_state['file_index'] > len(files.files_list):
            st.session_state.file_index = 0
            st.image(files.files_list[st.session_state['file_index']])
        # save file_id to database and move to next
    #st.image(files.files_list[st.session_state['file_index']])
    st.write(this_picture_id)



    # with st.form('picture_choser'):
    #     st.radio(
    #         'Släng eller spara?',
    #         [':material/delete:',':material/save:'],
    #         horizontal=True
    #     )
    #     st.form_submit_button('Verkställ')

    # files_list = CollectFiles('static/media/demopictures/accumulated/')
    # files_list = files_list.make_list_of_files()
    # db = DbConnection()
    #
    # picture_info = []

    # def status(path, status):
    #     db.write('picture_status',
    #              [
    #                  # 'timestamp',
    #                  'path',   # filename should be replaced by file hash from the categories listed in the
    #                                 # file matrix for the model
    #                      'status'], data=picture_info)
    #
    # for file_name in files_list:
    #     st.button('Delete', on_click=(status(file_name, 0) ))
    #     st.button('Keep', on_click=(status(file_name, 1) ))

    # db.__cleanup__()

    # TODO: create buttons
    # for submit-button:
    # icon="material/delete"
    # icon="material/save"
    # icon="material/favorite"
    # icon="material/bookmark"

    # TODO: is not correctly displayed
    # number_of_columns = 3
    # number_of_rows = ceil(len(files_list.make_list_of_files()) / number_of_columns)
    # st.write(number_of_rows)
    #
    # picture_order = 0
    #
    # for row in range(number_of_rows):
    #     row = st.columns(number_of_columns)
    #     for col in row:
    #         tile = col.container(height=120)
    #         image = files_list.make_list_of_files()[picture_order]
    #         st.image(image, use_container_width=True)
    #         picture_order += 1

with results:
    answers, logreg, live = st.tabs(['Svar', 'LogReg','Live'])
    with answers:
        id_answer = pd.DataFrame(
            ([0, 'ea5286ce55462128d83118f056e493450ac80e36e6ea87294cd97ff93dc6d4c4'],
             [1, 'ea5286ce55462128d83118f056e493450ac80e36e6ea87294cd97ff93dc6d4c4']),
            columns=['keep_or_delete', 'file_id'])

        st.dataframe(id_answer, height=100, hide_index=True)

    with logreg:
        st.header("Logistic Regression")
        st.markdown(""""
        Regression = deterministisk metod att beräkna framtida svaret på en nu okänd faktor mha olika givna faktorer.""")
        st.markdown("""
        Enkelt kan man beskriva det så här.
        
        Flertalet andra delar av en ekvation är kända som en funktion av _X_. Vi kan kalla det efterlängtade svaret för _y_.
        Vi har tränat modellen på flertalet rader där både **_y_** och **_x_** är kända
        """)

    with live:
        st.dataframe(model.X, hide_index=True, height=100)
        model.create_answers()
        #st.dataframe(model.y, hide_index=True, height=100)

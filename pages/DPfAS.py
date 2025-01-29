from hashlib import sha256

import streamlit as st
import pandas as pd
from streamlit import columns
from webcolors import names

from libraries.model_learning.logistic_regression import ModelTraining

# retrieving example data
model = ModelTraining()
X = model.create_X()

description, mockup, results = st.tabs(['Beskrivning','Mockup', 'Resultaten'])

with description:
    brief_info, data_handling, information_sources, methods, hashtag = st.tabs(['Introduktion', 'Datahantering', 'Informationskällor', 'Metoderna', 'Hashtag'])
    with brief_info:
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
        technologies_used = pd.Series(['OpenCV', 'YOLO', 'YOLO', 'OpenCV, (OCR)', 'PIL._getexif()', 'Python module os', '','','OpenCV','OpenCV'])
        headlines = ['Attribute','Technology used']
        # categories_techs = pd.concat([pd.DataFrame(model.categories), pd.DataFrame(technologies_used)], axis=1)
        categories_techs = pd.concat([categories.rename(headlines[0]), technologies_used.rename(headlines[1])], axis=1)
        # categories_techs = pd.DataFrame(categories_techs, columns=headlines)
        print(categories_techs)
        st.dataframe(categories_techs, use_container_width=True, hide_index=True)
        opencv, yolo = st.tabs(['OpenCV', 'YOLO'])

        with opencv:
            st.markdown(
                "[![qr-code for github repo](app/static/media/qr/differentiate_pictures_for_auto_sync.png)](https://github.com/DaDrummerthe1st/differentiate-pictures-for-auto-sync)")

        with yolo:
            st.markdown('Objektidentifikation ingår i kategorierna "contains_common_identified_objects" och "has_identified_objects".')

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

with results:
    identity, logreg = st.tabs(['Identitet', 'LogReg'])
    with identity:
        id_answer = pd.DataFrame(
            ([0, 'ea5286ce55462128d83118f056e493450ac80e36e6ea87294cd97ff93dc6d4c4'],
             [1, 'ea5286ce55462128d83118f056e493450ac80e36e6ea87294cd97ff93dc6d4c4']),
            columns=['keep_or_delete', 'file_id'])

        st.dataframe(id_answer, height=100)

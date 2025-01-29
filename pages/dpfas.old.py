import streamlit as st

from libraries.model_learning.logistic_regression import ModelTraining

brief_info, data_handling, matrix, identity, hashtag, information_sources = st.tabs(['Sammanfattning','Datahantering', 'Matrisen', 'Identitet', 'Hashtag', 'Informationskällor'])
description, app, result = st.tabs(['DPFAS', 'App', 'Result'])

# retrieving example data
model = ModelTraining()
X = model.create_X()

with description:
    with brief_info:
        st.header('Differentiate Pictures for Auto Sync')
        st.link_button("", "https://github.com/DaDrummerthe1st/differentiate-pictures-for-auto-sync",
                       icon=":material/link:")
        st.markdown("""
        DPFAS är ett tankeexperiment, som kanske någon gång ser dagens ljus.
        Målet är att minimera utrymmet mediafiler tar upp genom att bl a föreslå bilder att ta bort, enligt användarens tidgiare mönster.

        Framtida användning kan inkludera att komprimera, beskära, tagga filer samt flytta filer mellan enheter etc.

        Det är en app för alla enheter användaren har bilder på.
        Den består i ett användarinterface för att lära modellen och flertalet maskinlärningsmetoder.

        Använddaren använder appen för att visa modellen vilka preferenser användaren har relaterat bildens innehåll.
        """)

    with data_handling:
        data_handling2, methods = st.tabs(['Datahantering', 'Modeller'])
        with data_handling2:
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

        with methods:
            st.dataframe(model.categories)

    with matrix:
        st.header('Beståndsdelarna i matrisen')

        st.dataframe(X, height=100)
        st.markdown("""

        """)

    with identity:
        id_answer = pd.DataFrame(
            ([0, 'ea5286ce55462128d83118f056e493450ac80e36e6ea87294cd97ff93dc6d4c4'],
             [1, 'ea5286ce55462128d83118f056e493450ac80e36e6ea87294cd97ff93dc6d4c4']),
            columns=['keep_or_delete', 'file_id'])

        st.dataframe(id_answer, height=100)

    with hashtag:
        st.header('Hur byggs en hashtag?')
        with st.echo():
            # from hashlib import sha256

            inputinformation = "ett ord"
            st.write(sha256(inputinformation.encode('utf-8')).hexdigest())
            st.write(sha256(str(model.categories).encode('utf-8')).hexdigest())

        st.markdown("""
        Förenklat kan man säga att en input-textsträng räknar fram en output, bestående av ett förutbestämt antal tecken.
        #### Kryptering
        Det är oftast väldigt svårt att reverse engineera en hashtag - vilket gör de optimala för kryptering. När du skriver in ditt lösenord på en sida på nätet så skickas endast hashtagen till hemsidan, som sedan jämförs med den i databasen sparade hashtagen. Inget lösenord är därmed synligt och inte heller längde går att gissa.
        #### Representation
        I DPFAS representeras varje filidentifiering av en hash, som räknas fram enligt ovan. Denna utgör därmed en unik nyckel i tabellerna.
        Det betyder att "samma" fil, som blir manipulerad och därmed får andra förutsättningar, också få en annan hash.
        Systemet med hashar (med tillräckligt hög upplsning) medger också att det finns ett mycket stort antal potentiella nycklar. 
        """)

    with information_sources:
        st.header('Sammansättning')
        st.markdown("""
        När en fil läses in har den flertalet egenskaper:
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
        All denna information kan användas för att skapa ett unikt ID för varje bild.
        I den händelse bilden ändras så skapas också ett nytt id
        """)


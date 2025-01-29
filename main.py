import os

import pandas as pd
import streamlit as st

from libraries.database.connect import TestConnection

# # The whole app lives inside a sidebar.
# # Relation to the rest of file system from respective page goes out from main-root
# with st.sidebar:

#     pages = []
#     for (root, subdirs, files) in os.walk('pages/'):
#         for filename in files:
#             pages.append(os.path.splitext(filename)[0])
#     print(pages)
#     for page in pages:
#         st.page_link(page)

# class CreateSideBar(CollectFiles):
#     def __init__(self, path):
#         super().__init__(path)
#
#     @staticmethod
#     def create_sidebar():
#         with st.sidebar:
#             st.header('Dessa områden har jag bearbetat')
#         # with st.sidebar:
#         #     for page in (os.path.splitext(self.make_list_of_files())[0]):
#         #         st.page_link(page)


# st.sidebar.title('Agenda') " also not on top

intro, dpfas, the_matrix = st.tabs(['Introduktion', 'DPFAS', 'Matrisen'])

with intro:
    st.header('Processen')
    st.link_button("", "https://github.com/DaDrummerthe1st/present_machine_learning", icon=":material/link:")
    st.markdown("""
    Det här projektet är till för att jag själv ska få en övergripande bild av machine learning och även för stt testa lite hur det kan fungera.
    Begrepp och definitioner har tagits fram bl a av några av de främsta matematikerna genom tiderna. För att metoderna ska kunna användas krävs bl a körbarhet i form av prestanda och en tillräckligt tydlig förståelse för vad metoden gör. Anpassad pedagogik har alltså helt plötsligt en roll i huruvida metoden ska användas och därmed rendera utveckling och pengar.
    
    Fel kan förekomma och jag tar mer än gärna emot feedback.
    
    Jag har begränsat detta förberedande projjekt till att bara handla om bilder, mest för att det är avsevärt mycket mindre datahantering än t ex filmkläpp.
    """)

with (dpfas):
    st.header('Differentiate Pictures for Auto Sync')
    st.link_button("","https://github.com/DaDrummerthe1st/differentiate-pictures-for-auto-sync", icon=":material/link:")
    st.markdown("""
    DPFAS är ett tankeexperiment, som kanske någon gång ser dagens ljus.
    Målet är att minimera utrymmet mediafiler tar upp genom att bl a föreslå bilder att ta bort, enligt användarens tidgiare mönster.
    
    Framtida användning kan inkludera att komprimera, beskära, tagga filer samt flytta filer mellan enheter etc.
    
    Det är en app för alla enheter användaren har bilder på.
    Den består i ett användarinterface för att lära modellen och flertalet maskinlärningsmetoder.
    
    Använddaren använder appen för att visa modellen vilka preferenser användaren har relaterat bildens innehåll.
    
    """)
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

with the_matrix:
    st.header('Beståndsdelarna i matrisen')

    st.markdown("""
    
    """)



class TestRun:
    def __init__(self):
        test_connection = TestConnection()
        print(test_connection.connect())

        df = pd.DataFrame(test_connection.connect())

        headlines = {0:'id of enginetype', 1:'engine model'}
        df = df.rename(columns=headlines)

        print(df)

        display = StreamlitMainpage()
        display.testpage(df)

#t1 = TestRun()
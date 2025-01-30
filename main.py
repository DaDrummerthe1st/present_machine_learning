import os

import numpy as np
import pandas as pd
import streamlit as st
from hashlib import sha256

from libraries.database.connect import TestConnection


col1, col2, col3 = st.columns(3)
col1.link_button("Länk till repot på Github", "https://github.com/DaDrummerthe1st/present_machine_learning", icon=":material/link:")
col2.markdown(
    "[![qr-code for github repo](app/static/media/qr/present_machine_learning.png)](https://github.com/DaDrummerthe1st/present_machine_learning)")
col3.image('static/media/qr/present_machine_learning.png')
st.markdown("""
Det här projektet är till för att jag själv ska få en övergripande bild av ML (Machine Learning) och även för stt testa lite hur det kan fungera.

Begrepp och definitioner i den här världen har tagits fram bl a av några av de främsta matematikerna genom tiderna. För att metoderna ska kunna användas krävs bl a körbarhet i form av prestanda och en tillräckligt tydlig förståelse för vad metoden gör. Anpassad pedagogik har alltså helt plötsligt en roll i huruvida metoden ska användas och därmed rendera utveckling och pengar.

Fel kan förekomma och jag tar mer än gärna emot feedback.

Jag har begränsat detta förberedande projekt till att bara handla om bilder, mest för att det är avsevärt mycket mindre datahantering än t ex filmkläpp.
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
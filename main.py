import os
from fileinput import filename

import pandas as pd
import streamlit as st

from libraries.database.test_connection import TestConnection

# The whole app lives inside a sidebar.
# Relation to the rest of file system from respective page goes out from main-root
with st.sidebar:
    # TODO: relative path to project root
    # TODO: Cross-platform enabled
    # https://www.linkedin.com/advice/3/how-do-you-manage-path-differences-python-nwxnf
    pages = []
    for (root, subdirs, files) in os.walk('pages/'):
        for filename in files:
            pages.append(os.path.splitext(filename)[0])
    print(pages)
    for page in pages:
        st.page_link(page)


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
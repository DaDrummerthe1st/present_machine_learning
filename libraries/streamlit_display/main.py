import streamlit as st


class StreamlitMainPage:
    def __init__(self, pages, page_index):
        self.title = "Machine Learning"
        self.pages = pages  # a list of all pages
        self.page_index = page_index

    def skeleton(self, title, sidebar_objects):
        st.title(str(self.pages[self.page_index] + " - " + str(title)))

    def sidebar(self):
        pass

    def testpage(self, input_dataframe):
        st.write(input_dataframe)
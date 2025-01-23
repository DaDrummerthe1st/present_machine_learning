

from libraries.database.test_connection import TestConnection
from libraries.streamlit_display.main import StreamlitMainpage


test_connection = TestConnection()
display = StreamlitMainpage()
display.testpage(test_connection.connect())
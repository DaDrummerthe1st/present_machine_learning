from math import ceil
from operator import index
from os import path

import streamlit as st

from libraries.file_handling.list_files import CollectFiles
from libraries.database.connect import DbConnection

description, app, result = st.tabs(['DPFAS', 'App', 'Result'])

with description:  # tab
    st.subheader('Differentiate Pictures for auto sync')
    st.markdown("""
    Projektet, som är initierat av mig, är sprunget ur behovet att minska platsen mediafiler tar på datorn.
    """)
    # st.markdown("""
    # Visst är det nice att kunna dela, spara och intuitivt bläddra bland bilder?
    # Det är [Google Photos](https://youtu.be/CcnwFJqEnxU) väldigt bra på!
    #
    # För några år sedan gick Google ut med nyheten att samtliga bilder skulle börja räknas mot den totala kvoten man har där. Innan detta kunde man välja att komprimera den säerhetskopierade bilden och därmed spara den gratis. Ett fenomenalt sätt att få in användare som blir vana vid appen.
    # Google One ger användaren 15GB, vilket räcker rätt långt för de flesta, OM MAN rensar i gDrive, gPhotos och gMail.
    #
    # När den nyheten kom ut började jag fila på en lösning för att lättare ta bort och behålla RÄTT bilder. Rätt fort gick mina tankar till maskininlärning.
    # Idén är att lära sig hur anvndaren gör med sina bilder för att på så sätt börja kunna föreslå åtgärder i linje med detta.
    # """)
    st.markdown(
        "[![qr-code for github repo](app/static/media/qr/differentiate_pictures_for_auto_sync.png)](https://github.com/DaDrummerthe1st/differentiate-pictures-for-auto-sync)")
    st.link_button("Länk till repot på Github", "https://github.com/DaDrummerthe1st/differentiate-pictures-for-auto-sync", icon=":material/link:")


with app:  # tab
    st.header('Delete or Keep?')

    st.form('picture_choser')

    files_list = CollectFiles('static/media/demopictures/accumulated/')
    files_list = files_list.make_list_of_files()
    db = DbConnection()

    picture_info = []

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

    db.__cleanup__()

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

with result:
    st.header('Renderad data')


import streamlit as st
import webbrowser
import pandas as pd
from trubrics.integrations.streamlit import FeedbackCollector
from PIL import Image
import streamlit.components.v1 as components
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from streamlit_star_rating import st_star_rating
import plotly.express as px 
import matplotlib.pyplot as plt


scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('BdClientes')

#spreadsheet.share('mantillaalverniajimmystiveen@gmail.com', perm_type='user', role='writer')


# Define a class to represent the rows
class RowData:
    def __init__(self, title, comment, rating):
        self.title = title
        self.comment = comment
        self.rating = rating

# Open the worksheet
worksheet = spreadsheet.sheet1

# Define the headers
headers = ['Title', 'Comment', 'Rating']

# Insert the headers in the first row
#worksheet.append_row(headers)

# Read the rows from the worksheet
title_values = worksheet.col_values(1)  # Column A
comment_values = worksheet.col_values(2)  # Column B
rating_values = worksheet.col_values(3)  # Column C

rows = []
# export df to a sheet

# # Configuración de la página
st.set_page_config(page_title="Proyecto MyResidence")
# 
# # Título de la página
st.markdown("<h1 style='text-align: center; color: Black;'>Proyecto MyResidence</h1>", unsafe_allow_html=True)
# 
# # Establecer la página por defecto
state = "page1"
# 
# # Barra lateral con botones para navegar entre páginas
option = st.sidebar.button("1. Descripcion de la app")
option2 = st.sidebar.button("2. Esquema base de datos")
option3 = st.sidebar.button("3. Funcionalidades de la app")
# 
# # Variable de estado para determinar cuál página mostrar
if option:
     state = "page1"
elif option2:
     state = "page2"
elif option3:
     state = "page3"

# # Página 1
if state == "page1":
     image1 = Image.open('motel.jpg')
     col1, col2,col3,col4 = st.columns(4)
     with col2:
         st.image(image1, width=400)
     st.markdown("<h3 style='text-align: Left; color: Black;'>Descripcion de la app</h3>", unsafe_allow_html=True)
     st.markdown("<h5 style='text-align: justify; color: Gray;'>my Residence es una app centrada en el apoyo logistico a pequeñas residencias, "
         "permitiendoles llevar un manejo de sus instalaciones, clientes, empleados y inventarios de productos. "
         "La aplicación cuenta con diferentes funcionalidades que facilitan la administración y organización de la residencia, "
         "tales como la gestión de reservas y pagos, el seguimiento del inventario y la planificación de horarios de los empleados.</h5>", unsafe_allow_html=True)
     col1, col2 = st.columns(2)
     col1.image("https://i.ibb.co/1T66920/logo.jpg", width=250)
     # Print results.
     star1 = 0
     star2 = 0
     star3 = 0
     star4 = 0
     star5 = 0
     puntuaciones = [1,2,3,4,5]
     for title, comment, rating in zip(title_values, comment_values, rating_values):
         row = RowData(title, comment, rating)
         rows.append(row)
     for row in rows:
         if(row.title != "Title"):
             if(row.rating == "1"):
                 star1 = star1+1
             elif(row.rating == "2"):
                 star2 = star2+1
             elif(row.rating == "3"):
                 star3 = star3+1
             elif(row.rating == "4"):
                 star4 = star4+1
             elif(row.rating == "5"):
                 star5 = star5+1
     fig, ax = plt.subplots(figsize=(10, 7))
     cantidad = [star1,star2,star3,star4,star5]
     ax.bar(puntuaciones, cantidad)
     col2.pyplot(fig)
     prom = round((star1+(star2*2)+(star3*3)+(star4*4)+(star5*5))/(star1+star2+star3+star4+star5),2)
     col1.subheader(f"Calificacion promedio:({prom}/5.0)")
     st.markdown("<h3 style='text-align: Left; color: Black;'>Deja una reseña</h3>", unsafe_allow_html=True)
     stars = st_star_rating("Calificacion", maxValue=5, defaultValue=3, key="rating")
     st.markdown("<h5 style='text-align: Left; color: Gray;'>Comentario:</h5>", unsafe_allow_html=True)
     titulo = st.text_input('Titulo: ', '')
     comentario = st.text_input('Comentario: ', '')
     if st.button('Enviar reseña'):
         st.write('Gracias por su reseña')
         data = [titulo, comentario, stars]
         worksheet.append_row(data)
     st.markdown("<h3 style='text-align: Left; color: Black;'>Reviews</h3>", unsafe_allow_html=True)
     for row in rows:
         if(row.title != "Title"):
             st.divider()
             st.subheader(f"{row.title} ({row.rating}.0/5.0)")
             st.write(f"{row.comment}")
# 
# # Página 2
elif state == "page2":
     st.title("Esquema base de datos:")
     st.write("A continuación se muestra el esquema de la base de datos utilizada en el proyecto:")
     img1 = Image.open('schema.jpg')
     st.image(img1, width=700)
     st.write("La app cuenta con una base de datos no relacional con una libreria que cambia la sintaxix de sqlite, lo que hace mas facil la programacion")
 
# # Página 3
else:
     st.header("Funcionalidades de la app:")
     st.write("Este es un video de la version beta de la app donde se muestra su modo de uso:")
     st.video("https://youtu.be/SukK6yr5KaI", format='video/mp4', start_time=0)
     st.write("Si despues de ver el video te conveces y quieres tener la app dale click al boton de abajo:")
     link = '[Descarga ](https://www.mediafire.com/file/q219usprke25vlb/app-debug.apk/file)'
     st.markdown(link, unsafe_allow_html=True)
#


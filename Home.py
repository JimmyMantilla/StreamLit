import streamlit as st
import webbrowser
from trubrics.integrations.streamlit import FeedbackCollector
from PIL import Image

# # Configuración de la página
st.set_page_config(page_title="Proyecto MyResidence")
# 
# # Título de la página
st.title("Proyecto MyResidence")
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
     col1, col2 = st.columns(2)
     st.title("Descripcion de la app:")
     image1 = Image.open('motel.jpg')
     col1.image(image1, caption='Game art', width=400)
     col2.image("https://i.ibb.co/1T66920/logo.jpg", width=250)
     st.write("my Residence es una app centrada en el apoyo logistico a pequeñas residencias, "
              "permitiendoles llevar un manejo de sus instalaciones, clientes, empleados y inventarios de productos. "
              "La aplicación cuenta con diferentes funcionalidades que facilitan la administración y organización de la residencia, "
              "tales como la gestión de reservas y pagos, el seguimiento del inventario y la planificación de horarios de los empleados.")
     collector = FeedbackCollector()
     collector.st_feedback(feedback_type="issue")
     feedback = collector.st_feedback(
 	 feedback_type="faces",
 	 path="thumbs_feedback.json")
     feedback.dict() if feedback else None
# 
# # Página 2
elif state == "page2":
     st.title("Esquema base de datos:")
     st.write("A continuación se muestra el esquema de la base de datos utilizada en el proyecto:")
     img1 = Image.open('schema.jpg')
     st.image(img1, caption='Game art', width=1000)
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


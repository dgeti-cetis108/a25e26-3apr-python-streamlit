import time
import streamlit as st

st.write("# Hola Streamlit desde mi equipo")
st.write(
    """
## Bienvenidos
It is a long established fact that a reader will be distracted by the readable
content of a page when looking at its layout. The point of using Lorem Ipsum 
is that it has a more-or-less normal distribution of letters, as opposed to 
using 'Content here, content here', making it look like readable English. 
"""
)
st.write("## Elementos Básicos")
st.write("### Texto simple")
st.text("Texto simple")

st.write("### Botones")
st.button("Saludar")

st.write("### Checkboxes")
st.checkbox("Guardar inicio de sesión")

st.write("### Radios")
st.radio("Elige tu género", ["Hombre","Mujer","Prefiero no decirlo"])

st.write("### SelectBox")
st.selectbox("Elige un elemento", ["El1","El2", "El3", "El4"])

st.write("### Slider")
st.slider("Volumen del espoti", 0, 100)

st.write("### Entradas")
st.text_input("¿Cuál es tu nombre?")
st.number_input("¿Cuál es tu edad?", min_value=0, step=1)

st.write("### Fechas/Horas")
st.date_input("Elige la fecha")
st.time_input("¿Que hora es?")

st.write("## Elementos intermedios")

st.write("### Subir archivo")
st.file_uploader("Sube las calificaciones", type="pdf")

st.write("### Imagen")
st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.delftstack.com%2Fimg%2FPython%2Fpython-feature-image.webp&f=1&nofb=1&ipt=d85ed3ce469c2109eb794146b79f11c7d4e92bf864f63dda207a323912ab8cb1")


st.write("### Video")
st.video("https://youtu.be/8DvywoWv6fI?si=8y5QRUQ6-g3dBl6m")

st.write("### Audio")
st.audio("rolita.mp3")

st.write("### Spinner")
with st.spinner("Procesando..."):
    time.sleep(2)
st.success("Listo")

st.write("### Metric")
st.metric("Temperatura", value="36°C", delta="+1.2°C")

st.write("### Tabs")
tab1, tab2 = st.tabs(["Uno","Dos"])
with tab1:
    st.write("Pestaña uno")
with tab2:
    st.write("Pestaña dos")


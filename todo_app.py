import streamlit as st

st.set_page_config(page_title="Todo App", page_icon="☑️")

# variables de sesión
# validar la existencia de la variable tareas en la sesión
# de no encontrarse significa que es la primera vez que 
# se ejecuta la aplicación por lo tanto la declara e inicializa
if "tareas" not in st.session_state:
    st.session_state.tareas = []

st.title("☑️ Todo App")
st.text("Aplicación para gestionar tareas simples")

with st.form("frm_agregar", clear_on_submit=True):
    col1, col2 = st.columns([6,2])

    with col1:
        nueva = st.text_input("Nueva tarea", placeholder="Nueva tarea", 
                      label_visibility="collapsed")

    with col2:
        submit = st.form_submit_button("Agregar", use_container_width=True)

    # validar si se presionó el botón submit
    if submit:
        # obtener el texto de la caja sin espacios al principio o fin
        texto = nueva.strip()
        # validar que la variable exista y sea diferente de null
        if texto:
            # agregar a la lista de tareas
            st.session_state.tareas.append(texto)
        else:
            # alertar que deben agregar texto para poder ingresar una tarea nueva
            st.warning("Para agregar tareas nuevas escribe algo")


st.subheader("Tareas")

# unpack enumerations
for i, tarea in enumerate(st.session_state.tareas):
    st.checkbox(tarea, key=f"tarea_{i}")

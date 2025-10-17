import streamlit as st

# Inicializar la lista de tareas solo si no existe
if "tareas" not in st.session_state:
    st.session_state.tareas = ["Tarea 1", "Tarea 2", "Tarea 3"]

# Inicializar la caja de texto
if "tarea_nueva" not in st.session_state:
    st.session_state.tarea_nueva = ""

st.write("# ☑️Todo-App")
st.text("Bienvenido a mi aplicación de tareas pendientes.")

col1, col2 = st.columns(2, vertical_alignment="bottom")

with col1:
    tarea_input = st.text_input("Ingresa una tarea", value=st.session_state.tarea_nueva, key="input_tarea")

with col2:
    if st.button("Agregar"):
        if tarea_input.strip():  # Solo agregar si no está vacío
            st.session_state.tareas.append(tarea_input)
            st.session_state.tarea_nueva = ""
            st.rerun()  # Recargar la app para limpiar el input

for tarea in st.session_state.tareas:
    st.checkbox(tarea)

import streamlit as st

st.set_page_config(page_title="Todo App", page_icon="☑️")

# variables de sesión
tareas = ["Tarea 1", "Tarea 1", "Tarea 3"]

st.title("☑️ Todo App")
st.text("Aplicación para gestionar tareas simples")

with st.form("frm_agregar", clear_on_submit=True):
    col1, col2 = st.columns([6,2])

    with col1:
        st.text_input("Nueva tarea", placeholder="Nueva tarea", 
                      label_visibility="collapsed")

    with col2:
        st.form_submit_button("Agregar", use_container_width=True)

st.subheader("Tareas")

for i, tarea in enumerate(tareas):
    st.checkbox(tarea, key=f"tarea_{i}")

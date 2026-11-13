import datetime as dt
import streamlit as st


st.title("Stack To-Do List")

today = dt.date.today()
st.write(today.strftime("%A, %B %d, %Y"))

# Create the list once, then keep it across Streamlit reruns.
if "tasks" not in st.session_state:
    st.session_state.tasks = ["Learn Python", "Add extensions to project"]

text_task = st.text_input("Add your task")
add_button = st.button("Add")

if add_button and text_task.strip():
    st.session_state.tasks.append(text_task.strip())



for task in st.session_state["tasks"]:
    with st.container(border=True):
        st.write(task)



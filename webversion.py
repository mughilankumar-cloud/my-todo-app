import streamlit as st

import func



def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    func.write_todos(todos)

todos = func.get_todos()

st.title("my todo app")
st.subheader("tis is my todo application")
st.write("this app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="enter a todo",
              placeholder="add a new todo...."
              ,on_change=add_todo,
              key='new_todo')






import streamlit as st

st.title("To-Do List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input for new task
new_task = st.text_input("Enter a new task:")

# Add task button
if st.button("Add Task"):
    if new_task.strip():  # avoid empty input
        st.session_state.tasks.append(new_task)
        st.success(f"Added task: {new_task}")
    else:
        st.warning("Please enter a task!")

# Display tasks
st.subheader("Your Tasks:")

if st.session_state.tasks:
    # Loop through tasks
    for i, task in enumerate(st.session_state.tasks):
        col_task, col_button = st.columns([0.8, 0.2])
        col_task.write(f"{i+1}. {task}")
        remove = col_button.button("Remove", key=f"remove_{i}")
        if remove:
            st.session_state.tasks.pop(i)
            st.experimental_rerun = lambda: None  # safely ignore rerun
else:
    st.info("No tasks yet! Add one above.")

import streamlit as st
import sqlite3

DB_PATH = "procurement.db"

def get_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, role FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user_id = user[0]
            st.session_state.username = user[1]
            st.session_state.role = user[2]
            st.success(f"Welcome, {user[1]}!")
        else:
            st.error("Invalid username or password.")

def check_login():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        login()
        st.stop()

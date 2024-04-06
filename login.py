import streamlit as st
from pymongo import MongoClient
import hashlib
import dbtest

# Connect to MongoDB
client = MongoClient("mongodb+srv://josephpeterjece2021:AJ9Hg6xTtQBUCoGr@cluster1.xaacunv.mongodb.net/?retryWrites=true&w=majority")
db = client["Python"]
users_collection = db["users"]

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if username exists
def username_exists(username):
    return users_collection.find_one({"username": username}) is not None

# Function to register a new user
def register(username, password):
    hashed_password = hash_password(password)
    user_data = {"username": username, "password": hashed_password}
    users_collection.insert_one(user_data)
    st.success("Registration successful. Please log in.")

# Function to authenticate user
def authenticate(username, password):
    hashed_password = hash_password(password)
    user = users_collection.find_one({"username": username, "password": hashed_password})
    return user is not None

# Streamlit UI for login
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if authenticate(username, password):
            st.success("Logged in successfully!")
            
            # Set a session state flag to indicate successful login
            st.session_state.logged_in = True
            st.experimental_rerun()  # Reload the app to trigger redirection
        else:
            st.error("Invalid username or password. Please try again.")

# Function to register new user
def register_page():
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password == confirm_password:
            if not username_exists(username):
                register(username, password)
            else:
                st.error("Username already exists. Please choose a different username.")
        else:
            st.error("Passwords do not match. Please try again.")

# Function to hide login form and navigation
def hide_login_form():
    login_slot.empty()
    nav_slot.empty()

# Streamlit UI for main page
def main():
    st.sidebar.title("Navigation")
    global login_slot
    global nav_slot

    # Check if the user is not logged in before displaying "Go to" options
    if not st.session_state.get("logged_in"):
        page = st.sidebar.radio("Go to", ["Login", "Register"])

        if page == "Login":
            nav_slot = st.sidebar.empty()
            login_slot = st.empty()
            if not st.session_state.get("logged_in"):
                login_page()
        elif page == "Register":
            nav_slot = st.sidebar.empty()
            login_slot = st.empty()
            register_page()

    # Check if the user is logged in and redirect accordingly
    if st.session_state.get("logged_in"):
        dbtest.mains()

if __name__ == "__main__":
    main()

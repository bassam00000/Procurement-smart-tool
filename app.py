import streamlit as st
from login import check_login
from pages import home, purchase_requests, purchase_orders, rfqs, offers, admin

st.set_page_config(page_title="Smart Procurement Tool", layout="wide")
check_login()

PAGES = {
    "Home": home,
    "Purchase Requests": purchase_requests,
    "Purchase Orders": purchase_orders,
    "RFQs": rfqs,
    "Offers": offers,
    "Admin": admin
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
PAGES[selection].app()

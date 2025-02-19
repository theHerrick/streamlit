import streamlit as st
from streamlit_msal import Msal

client_id = "818de6b9-60ea-4c68-a1b5-e2ec5b0e9a66"
authority = "https://login.microsoftonline.com/2a3a7925-0941-4f65-a806-bbb581592374"

with st.sidebar:
    auth_data = Msal.initialize_ui(
        client_id=client_id,
        authority=authority,
        scopes=["User.Read"],
        connecting_label="Connecting",
        disconnected_label="Disconnected",
        sign_in_label="Sign in",
        sign_out_label="Sign out"
    )

if not auth_data:
    st.write("Authenticate to access protected content")
    st.stop()

st.write("Protected content available")
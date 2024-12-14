import streamlit as st
import re

def generate_download_link(share_url):
    """
    Generates a direct download link for a Google Drive sharing URL.
    
    Parameters:
        share_url (str): The Google Drive sharing URL.
    
    Returns:
        str: The direct download URL.
    """
    match = re.search(r'/d/([^/]+)/', share_url)
    if match:
        file_id = match.group(1)
        download_link = f"https://drive.google.com/uc?export=download&id={file_id}"
        return download_link
    else:
        return None

# Streamlit App
st.title("Google Drive Direct Download Link Generator")
st.write("Paste your Google Drive sharing URL below to generate a direct download link.")

# Input URL
share_url = st.text_input("Google Drive Sharing URL:", placeholder="e.g., https://drive.google.com/file/d/FILE_ID/view")

# Generate button
if st.button("Generate Link"):
    if share_url.strip():
        download_link = generate_download_link(share_url)
        if download_link:
            st.success("Direct Download Link:")
            st.write(download_link)
            st.markdown(f"[Download File]({download_link})", unsafe_allow_html=True)
        else:
            st.error("Invalid Google Drive sharing URL. Please check and try again.")
    else:
        st.warning("Please enter a Google Drive sharing URL.")

import streamlit as st
import os
import hmac
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Azure Key Vault details
KEY_VAULT_NAME = os.getenv('KEY_VAULT_NAME')
SECRET_NAME = os.getenv('SECRET_NAME')
KV_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net"


st.set_page_config(
    page_title="Acceuil",
    page_icon="👋",
)


# Authenticate and retrieve the password from Azure Key Vault
@st.cache_data
def get_password_from_keyvault():
    """Fetches the password securely from Azure Key Vault."""
    credential = DefaultAzureCredential()
    # credential = ManagedIdentityCredential()
    client = SecretClient(vault_url=KV_URI, credential=credential)
    retrieved_secret = client.get_secret(SECRET_NAME)
    return retrieved_secret.value

# Fetch the password once
STORED_PASSWORD = get_password_from_keyvault()

# STORED_PASSWORD = os.getenv('STORED_PASSWORD')
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], STORED_PASSWORD):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False



if not check_password():
    st.stop()  # Do not continue if check_password is not True.

st.success("🎉 You have access to the app!")


###### real app starts here



st.write("# Bienvenue sur votre outil de conversation AzureAI! 👋")

st.sidebar.success("Selectionnez un outils sur la barre de gauche")

st.markdown(
    """
    Cet outil utilise les capacitées de OpenAI à travers la plateforme Azure AI Studio pour le résumé de conversation et l'exploration du contenu de ces résumés
    **👈 Selectionnez un outil sur la barre de navigation à gauche**
    ### Plus d'information?
    - Explorez l'outil Microsoft Language Studio [Language Cognitive] https://language.cognitive.azure.com/home 
    - Interface Azure pour le résumé de conversation [Summarization](https://language.cognitive.azure.com/tryout/summarization)
    - Demander de nouvelles fonctionnalités [contact IT](mailto:remi.cazelles@carbon-waters.com)
    ### Autre informations
    - Vérifier coûts [Portail Azure](https://portal.azure.com/#home)
"""
)
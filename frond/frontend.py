import streamlit as st
import pandas as pd
import numpy as np
import requests

URL = "https://backendtama.herokuapp.com/predict/"

st.set_page_config(
    page_title = "BULLETIN (CYBERBULLYING CLASSIFICATION)",
    page_icon="👌",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/tamaarsy',
        'About': "# Cyberbullying Classification"
    }
)

st.image("bulletin.png")
st.title("STOP CYBERBULLYING, DIMULAI DARI ANDA!")
"\n"
st.title("Cyberbullying is NO NO NO")
st.image("cyberbullying.jpg")
"\n"
st.title("kenapa???")
st.image("cyberbullying_2.jpg")
"\n"
st.markdown("Cegah cyberbullying dengan ketik tweet yang ingin kamu ungkapkan dibawah ini:")
"\n"
out = st.text_area("Tweet kamu adalah : ")
"\n"


data = {
    'Out':out,
}

r = requests.post(URL, json=data)
#st.write(data)
res = r.json()
#st.write(res)
print(f'res : {res}')

st.write(f"Tulisan tweet kamu termasuk : {res['result_model']}")

st.subheader("DUNIA INDAH TANPA CYBERBULLYING, BULLETIN - 2022")
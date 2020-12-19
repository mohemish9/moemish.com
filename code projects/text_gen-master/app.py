import streamlit as st 
from markov_text_genrator import gen_from_model, markov_model, markov 

text = markov('as_you_like_it.txt',2,500)
st.write(text)

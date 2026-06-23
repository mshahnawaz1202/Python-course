import streamlit as st
import pandas as pd
import numpy as np



#----------- function for overview of data -------
def show_overview_cards(df):
    total_records = len(df)
    total_features = len(df.columns)
    avg_processing_cost = np.random.randint(1000, 4000)
    active_models = np.random.randint(1, 10)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Records", f"{total_records:,}")
    with c2:
        st.metric("Features", f"{total_features}")
    with c3:
        st.metric("Avg. Proc. Cost", f"${avg_processing_cost}")
    with c4:
        st.metric("Active Models", f"{active_models}")


# ------------------- setting page -------------
st.set_page_config('Data Analyst Dashboard')


# --------------- sidebar Navigation ---------------
if "page" not in st.session_state:
    st.session_state.page='Home'


st.sidebar.title('Navigation')

if st.sidebar.button('Home'):
    st.session_state.page='Home'

if st.sidebar.button('Summary'):
    st.session_state.page='Summary'

if st.sidebar.button('Visualize'):
    st.session_state.page='Visualize'

if st.sidebar.button('Statistics'):
    st.session_state.page='Statistics'

if st.sidebar.button('Top Performers'):
    st.session_state.page='Top Performers'


# ---------------- page views ---------------

if st.session_state.page=='Home':
    col1,col2,col3=st.columns([1,2,3])

    with col2:
        st.title('Data Analyst Dashboard')
        









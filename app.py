from src.extration import load_data
import numpy as np

#:import streamlit as st

#st.set_page_config(layout = wide)

def main():
    df_raw = load_data()

    #st.dataframe(df_raw)

if __name__ == '__main__':

   main()

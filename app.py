import streamlit as st
from io import BytesIO
import pandas as pd
import fonction_v2
import matplotlib.pyplot as plt
import io
from PIL import Image
import numpy as np

st.set_page_config(layout="wide")

def main():

    tab1 = st.tabs("Game Analysis Kicking")

    with tab1:
        
        st.title("Game Analysis Kicking 🔵⚪️")
        
        uploaded_file = st.file_uploader("Importer le fichier CSV", type=["csv"],key="file_uploader1")
        
        if uploaded_file is not None:
    
            st.write("File Uploaded Successfully!")

            check = st.checkbox("GameTime Graphics")
            
            df = pd.read_csv(uploaded_file)

            joueurs_racing = list(df[df.Row == "Jeu au pied Racing"].Joueurs.unique())

            player_inputs = {}
        
            for player in joueurs_racing:
    
                player_input = st.text_input(f"N° de {player} : ")
                player_inputs[player] = player_input
            
            st.write("Player Inputs:")
            st.write(player_inputs)
    
            if st.button("Process Images"):
    
                img = fonction_v2.kicking_plot(df,player_inputs)
                st.image(img)
    
                img = fonction_v2.kicking_plot_adv(df,opta=False)
                st.image(img)

                if check:

                    df1 = df.copy()
                    img = fonction_v2.gametime_graph3(df1)
                    st.image(img)


if __name__ == "__main__":
    main()

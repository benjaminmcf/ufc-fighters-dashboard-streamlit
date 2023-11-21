import streamlit as st 
import pandas as pd 
st.title('UFC Fighters dashboard')

df = pd.read_csv('ufc-fighters-statistics.csv')

fighter_select = st.sidebar.selectbox(
    "Select a fighter",
    df['name'].unique()
)


"""
name
nickname
wins
losses
draws
height_cm
weight_in_kg
reach_in_cm
stance
date_of_birth
significant_strikes_landed_per_minute
significant_striking_accuracy
significant_strikes_absorbed_per_minute
significant_strike_defence
average_takedowns_landed_per_15_minutes
takedown_accuracy
takedown_defence
average_submissions_attempted_per_15_minutes
"""

if fighter_select:
    st.write(fighter_select)
    df_fighter = df[df['name'] == fighter_select]
    # wins
    st.write('Wins: ', df_fighter['wins'].values[0])
    # losses
    st.write('Losses: ', df_fighter['losses'].values[0])
    # draws
    st.write('Draws: ', df_fighter['draws'].values[0])
    # height_cm
    st.write('Height: ', df_fighter['height_cm'].values[0])
    # weight_in_kg
    st.write('Weight: ', df_fighter['weight_in_kg'].values[0])
    # reach_in_cm
    st.write('Reach: ', df_fighter['reach_in_cm'].values[0])
    # stance
    st.write('Stance: ', df_fighter['stance'].values[0])
    # date_of_birth
    st.write('Date of birth: ', df_fighter['date_of_birth'].values[0])
    # significant_strikes_landed_per_minute
    st.write('Significant strikes landed per minute: ', df_fighter['significant_strikes_landed_per_minute'].values[0])
    



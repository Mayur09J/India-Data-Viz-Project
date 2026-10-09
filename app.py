import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def local_css(Appcss):
    with open ('Appcss.css') as f:
        st.markdown(f'<style>{f.read()}</styel>', unsafe_allow_html=True)

local_css('Appcss.css')


st.set_page_config(page_title='Indias Data Wise',layout='wide')

df=pd.read_csv('India.csv')

list_of_states=list(df['State'].unique())
list_of_states.insert(0,'Overall India')
df.drop(columns='Households',inplace=True)
sor=sorted(df.columns[53:])
sor.insert(13,'Population')


st.title('India census plot 2011')

st.sidebar.title('Indias Data Wise')

selected_state=st.sidebar.selectbox('Select State',list_of_states)

primary=st.sidebar.selectbox('Select Primary Parameter',sor)

secondary=st.sidebar.selectbox('Select Secondary Parameter',sor)

plot=st.sidebar.button('plot Graph',width=200)

if plot:
    if selected_state=='Overall India':
        india_center = {"lat": 20.5937, "lon": 78.9629}

        st.markdown('Size Represent Primary Parameter')
        st.markdown('Color Represents Secondary parameter')

        fig = px.scatter_map(df, lat='Latitude', lon='Longitude', zoom=4, map_style='carto-positron',size=primary,
                             color=secondary,size_max=35,width=1450,height=800,center=india_center,
                             hover_name='District'
                             )
        st.plotly_chart(fig,width="stretch")
    else:
        state_lat = df[df['State'] == selected_state]['Latitude'].head(1).values.item()
        state_lon = df[df['State'] == selected_state]['Longitude'].head(1).values.item()

        state_center = {"lat": state_lat, "lon": state_lon}

        st.markdown('Size Represent Primary Parameter')
        st.markdown('Color Represents Secondary parameter')

        state_df=df[df['State']==selected_state]


        fig = px.scatter_map(state_df, lat='Latitude', lon='Longitude', zoom=6, map_style='carto-positron',size=primary,color=secondary,
                             size_max=35,width=1450,height=800,center=state_center,hover_name='District',color_discrete_sequence=px.colors.qualitative.Vivid)
        st.plotly_chart(fig,width="stretch")



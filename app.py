import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')
car_data['model_year'] = car_data['model_year'].fillna(value=0)
car_data['model_year'] = car_data['model_year'].astype(str)
car_data['cylinders'] = car_data['cylinders'].fillna(value=0)
car_data['cylinders'] = car_data['cylinders'].astype(str)
car_data['odometer'] = car_data['odometer'].fillna(value=0)
car_data['paint_color'] = car_data['paint_color'].fillna(value='Unknown')
car_data['is_4wd']=car_data['is_4wd'].fillna(value=0)
car_data['is_4wd'] = car_data['is_4wd'].astype(str)
#print(car_data['is_4wd'].head(10))
#print(car_data.head(20))
#print(car_data.info())

hist_button = st.button('Criar histograma')
st.header("Histograma de Veiculos")

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

hist_button_2 = st.button('Criar Gráficos de dispersão') # criar um botão
        
if hist_button_2: 
    st.write('Criando um Gráficos de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig  =  px . scatter ( car_data,x="odometer", y="price") 
    st.plotly_chart(fig, use_container_width=True)     

build_histogram = st.checkbox('Criar um histograma')
if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('Criando um Gráficos de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig  =  px . scatter ( car_data,x="odometer", y="price") 
    st.plotly_chart(fig, use_container_width=True)



#streamlit run app.py
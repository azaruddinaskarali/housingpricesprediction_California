



import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

from sklearn.base import BaseEstimator, TransformerMixin






pickle_in = open( "fo_reg.pkl","rb")
fo_reg=pickle.load(pickle_in)


header=st.beta_container()
dataset=st.beta_container()
features=st.beta_container()



with header:
    st.title("Welcome to California Housing Prices Project!")

    st.text("◆ In this Project I have built a ML regression-models that learns from California Housing Prices data [derived from 1990 Census(USA)]which Predicts the median housing price in any district in California, when all the other metrics are given.")


with dataset:
    st.header("★ California Housing Prices Dataset")

    st.text("◆ I found the dataset in kaggle and used it for my predictions")

    housing_data=pd.read_csv(r"C:\Users\Lenovo\Desktop\California_streamlit_webapp\housing.csv")
    st.write(housing_data.head(5))

    st.subheader("★ Median Income Distribution in the Housing Prices Dataset")
    median_income_distribution=pd.DataFrame(housing_data['median_income'].value_counts())
    st.bar_chart(median_income_distribution.head(50))


with features:
    st.header('★ The New Features I have Created.')

    st.text("◆ I tried various attribute combinations. For example, the total number of rooms in a district is not very useful if we don’t know how many households there are. What we really want is the number of rooms per household.")

    st.text('◆ First Feature of Additional features Created  Rooms_per_household ')
    st.text('◆ Second Feature of Additional features Created Bedrooms_per_room')
    st.text('◆ Third Feature of Additional features Created Population_per_household ')






def welcome():
    return "Welcome All"


def predict_housePrices(longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,HOCEAN,INLAND,ISLAND,NEARBAY,NEAROCEAN):



    prediction=fo_reg.predict([[longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population	,households,median_income,HOCEAN,INLAND,ISLAND,NEARBAY,NEAROCEAN]])
    print(prediction)
    return prediction



def main():
    st.title("Lets dive into the Predictions!")
    html_temp = """
    <div style="background-color:#5f9ea0;padding:10px">
    <h2 style="color:white;text-align:center;">California Housing Prices Predictor ML app  </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)




    lon = st.slider("Longitude",-124.350000,-114.310000,key='1')
    st.write(f"Longitude: {lon}")
    longitude=lon

    lat = st.slider("Latitude",32.540000,41.950000,key='2')
    st.write(f"Latitude: {lat}")
    latitude=lat

    hma = st.slider("Housing_Median_Age", 1,52,key='3')
    st.write(f"Housing_Median_Age: {hma}")
    housing_median_age=hma


    totrooms = st.slider("totalrooms", 2,39320,key='4')
    st.write(f"Total_Rooms: {totrooms}")
    total_rooms=totrooms

    totbedrooms = st.slider("TotalBedrooms",1,6445,key='5')
    st.write(f"TotalBedrooms: {totbedrooms}")
    total_bedrooms=totbedrooms

    pop = st.slider("Population", 3,35682,key='6')
    st.write(f"Population: {pop}")
    population=pop

    hos= st.slider("households", 1,6092,key='7')
    st.write(f"households: {hos}")
    households=hos

    med_inc = st.slider("median_income", 0.499900,15.000100,key='8')
    st.write(f"median_income: {med_inc}")
    median_income=med_inc




    HOCEAN = st.text_input("<1H OCEAN","Type <1 H ocean Here")
    INLAND = st.text_input("INLAND","Type Inland Here")
    ISLAND = st.text_input("Island","Type Island Here")
    NEARBAY = st.text_input("Near_Bay","Type Nearbay Here")
    NEAROCEAN= st.text_input("Near_Ocean","Type Nearocean Here")




    result=""
    if st.button("Predict"):
        result=predict_housePrices(longitude,latitude,housing_median_age,total_rooms,total_bedrooms	,population	,households,median_income,HOCEAN,INLAND,ISLAND,NEARBAY,NEAROCEAN)
    st.success('The Median Housing Price in $ is  {}'.format(result))


    if st.button("About"):

        st.text("Built with Streamlit")
        st.text("Built By Azaruddin AskarAli")

if __name__=='__main__':
    main()

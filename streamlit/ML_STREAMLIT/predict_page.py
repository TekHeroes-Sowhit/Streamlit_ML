
import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("saved_steps.pkl",'wb') as file:
    data=pickle.dump(data,file)
    return data
data=load_model()
lb_country=data["lb_country"]
lb=data[""]

countries=[
    "United States",
    "India",
    "United Kingdom",
    "Germany",
    "Brazil",
    "France",
    "Spain",
    "Australia",
    "Netherlands",
    "Poland",
    "Italy",
    "Russian Federation",
    "Sweden
    
]

education=(
    "Less than a Bachelor",
    "Bachelor`s Degree",
    "Master`s Degree",
    "Post grad",
)

country=st.selectbox("Country",countries)
education=st.selectbox("education Leve",education)
experience=st.slider("Years of Experience",0,50,3)


def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write(""" ### We need more information to predict salary """)
    

ok=st.button("Calculate Salary")
if ok:
    x=np.array([["United States",'Master`s Degree']])
    x[:,0]=lb_country.transform(x[:0])
    x[:,1]=lb_country.transform(x[:,1])
    x=x.astype(float)
    salary=regressor.predict(x)
    st.subheader(f" the estimated salary is ${salary[0]:.2f}")
    

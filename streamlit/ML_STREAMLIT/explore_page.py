
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def clean_experience(x):
    if x=='More than 50 years':
        return 50
    if x=='Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor`s Degree':
        return 'Bachelor`s Degree'
    if 'Masters`s Degree':
        return 'Masters`s Degree'
    if 'Professional degree' in x or'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'
@st.cache
def load_data():
    df=pd.read_csv("C:/Users/00824732/Desktop/streamlit/survey_results_public.csv")
    df=df[["Country","YearsCodePro","Employment","ConvertedComp","EdLevel"]]
    df=df.rename({"ConvertedComp":"Salary"},axis=1)
    df=df.rename({"ConvertedComp":"Salary"},axis=1)
    df=df[df["ConvertedComp"].notnull()]
    df=df.dropna()
    df=df[df["Employment"]=="Employed full-time"]
    df=df.drop("Employment",axis=1)
    country_map=shorten_categories(df.Country.value_counts(),400)
    df["Country"]=df["Country"].map(country_map)
    df_full_time=df_full_time[df_full_time["Salary"]<=25000]
    df_full_time=df_full_time[df_full_time["Salary"]>=10000]
    df_full_time=df_full_time[df_full_time["Country"]!="Other"]
    
    df["YearCodePro"]=df["YearCodePro"].apply(clean_experience)
    df["EdLevel"]=df["EdLevel"].apply(clean_education)
    return df

df=load_data()


def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    st.write(""" ### Stack Overflow Developer Salary""")
    fig1,ax1=plt.subplots()
    ax1.pie(data,labels=data.index,autopct='%1.1f%%',shadow=True,startangle=90)
    ax1.axis("equal")
    st.write("""### Number of Data from different countries """)
    st.pyplot(fig1)
    st.write("""### Mean Salary Based on Country """)
    data=df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    st.write("""### Mean Salary Based on Experience """)
    data=df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
     

    
    
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Function to lower the countries in data & keep only countries which have more than threshold data available
def country_adjust(categories,threshold):
    categorial_map={}
    for i in range(len(categories)):
        if(categories.values[i] >= threshold):
            categorial_map[categories.index[i]]=categories.index[i]
        else:
            categorial_map[categories.index[i]]="Other"
    return categorial_map

#Function to clean the experience feature in the dataset
def clean_experience(x):
    if(x=="Less than 1 year"):
        return 0.5
    elif(x=="More than 50 years"):
        return 50
    else:
        return float(x)

#Function to clean the education feature in the dataset
def clean_education(x):
    if(x=="Bachelor’s degree (B.A., B.S., B.Eng., etc.)"):
        return "Bachelor’s degree"
    elif(x=="Master’s degree (M.A., M.S., M.Eng., MBA, etc.)"):
        return "Master’s degree"
    elif(x=="Professional degree (JD, MD, etc.)" or x=="Other doctoral degree (Ph.D., Ed.D., etc.)"):
        return "Post Graduation"
    else:
        return "Less than a Bachelor"


#Function to load the dataset and clean the dataset using above function calls
@st.cache
def load_data():
    df = pd.read_csv('survey_results_public.csv')
    df = df[["Country","EdLevel","YearsCodePro","Employment","ConvertedComp"]]
    df = df.rename({"ConvertedComp":"Salary"},axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment",axis=1)

    #Clean the country feature
    country_map = country_adjust(df["Country"].value_counts(),400)
    df["Country"] = df["Country"].map(country_map)

    #Removing the outliers
    df = df[df["Salary"] <=150000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]

    #Clean the experience feature
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)

    #Clean the education feature
    df["EdLevel"] = df["EdLevel"].apply(clean_education)

    return df



df = load_data()

def show_explore():
    st.title("Explore Software Engineer Salaries")

    st.write("""
    ### Stack Overflow Developer Survey 2020
    """)

    data = df["Country"].value_counts()
    
    fig1 , ax1 = plt.subplots()

    ax1.pie(data,labels=data.index,autopct="%1.1f%%",startangle=50)
    ax1.axis("equal")

    st.write("#### Number of records of Data from Different Countries")
    st.pyplot(fig1)

    st.write("""
    ### Mean Salary based on Country
    """)
    agree = st.button("Click to see Mean Salary based on Country")
    if agree:
        data_salmean = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=False)
        print(data_salmean)
        st.bar_chart(data_salmean)


    
    st.write("""
    ### Mean Years of Experience based on Country
    """)
    agree = st.button("Click to see Mean Years of Experience based on Country")
    if agree:
        data_expmean = df.groupby(["Country"])["YearsCodePro"].mean().sort_values(ascending=False)
        print(data_expmean)
        st.bar_chart(data_expmean)

    st.write("""
    ### Mean Salary based on Years of Experience
    """)
    agree = st.button("Click to see Mean Salary based on Years of Experience")
    if agree:
        data_expsal = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=False)
        print(data_expsal)
        st.line_chart(data_expsal)

    st.write("""
    ### All Data of Salaries
    """)
    agree = st.button("Click to see All Data of Salaries")
    if agree:
        chart_data = pd.DataFrame(df[:], columns=["Salary"])
        st.area_chart(chart_data)

    st.write("""
    ### Box Plot of Salaries to Identify Outliers
    """)
    agree = st.button("Click to see Box Plot of Salaries")
    if agree:
        fig , ax = plt.subplots(1,1, figsize=(12,7))
        df.boxplot('Salary' , 'Country' , ax=ax)
        plt.suptitle("Salary USD vs Country")
        plt.title("")
        plt.ylabel("Salary")
        plt.xticks(rotation=90)
        st.pyplot(fig)



    st.write("""
    ### Box Plot of Years of Experience to Identify Outliers
    """)
    agree = st.button("Click to see Box Plot of Years of Experience")
    if agree:
        fig , ax = plt.subplots(1,1, figsize=(12,7))
        df.boxplot('YearsCodePro' , 'Country' , ax=ax)
        plt.suptitle("Years of Experience vs Country")
        plt.title("")
        plt.ylabel("Experience")
        plt.xticks(rotation=90)
        st.pyplot(fig)
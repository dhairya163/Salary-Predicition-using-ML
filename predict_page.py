import streamlit as st
import pickle
import numpy as np

def model_dt():
    def load_model():
        with open("saved_steps.pkl","rb") as file:
            data = pickle.load(file)
        return data

    data = load_model()

    model = data["model_dt"]
    le_country = data["le_country"]
    le_education = data["le_education"]

    def show_predict_page():
        st.title("Software Dev. Salary Prediction")
        st.write("""#### The Salary is predicted from Stackoverflow developer survey 2020 data using Decision Tree Regressor with max depth = 8 to minimise the error.""")
        st.write("""#### We need some information to predict the salary""")
        countries = ('United States', 'United Kingdom', 'Spain', 'Netherlands',
        'Germany', 'Canada', 'Italy', 'Brazil', 'France',
        'Poland', 'India', 'Sweden', 'Australia', 'Russian Federation')
        education_options = ("Less than a Bachelor","Bachelor’s degree","Master’s degree","Post Graduation")
        country = st.selectbox("Country",countries)
        education = st.selectbox("Education Level",education_options)

        experience = st.slider("Years of Experience",0,50)

        post = st.button("Calculate Salary")

        if post:
            X = np.array([[country,education,experience]])

            X[:,0] = le_country.transform(X[:,0])
            X[:,1] = le_education.transform(X[:,1])
            X = X.astype(float)

            y_pred_input = model.predict(X)

            st.subheader("The estimated salary is {0:.2f} USD".format(y_pred_input[0]))
    show_predict_page()

def model_linear():
    def load_model():
        with open("saved_steps.pkl","rb") as file:
            data = pickle.load(file)
        return data

    data = load_model()

    model = data["model_linear"]
    le_country = data["le_country"]
    le_education = data["le_education"]

    def show_predict_page():
        st.title("Software Dev. Salary Prediction")
        st.write("""#### The Salary is predicted from Stackoverflow developer survey 2020 data using Linear Regressor""")
        st.write("""#### We need some information to predict the salary""")
        countries = ('United States', 'United Kingdom', 'Spain', 'Netherlands',
        'Germany', 'Canada', 'Italy', 'Brazil', 'France',
        'Poland', 'India', 'Sweden', 'Australia', 'Russian Federation')
        education_options = ("Less than a Bachelor","Bachelor’s degree","Master’s degree","Post Graduation")
        country = st.selectbox("Country",countries)
        education = st.selectbox("Education Level",education_options)

        experience = st.slider("Years of Experience",0,50)

        post = st.button("Calculate Salary")

        if post:
            X = np.array([[country,education,experience]])

            X[:,0] = le_country.transform(X[:,0])
            X[:,1] = le_education.transform(X[:,1])
            X = X.astype(float)

            y_pred_input = model.predict(X)

            st.subheader("The estimated salary is {0:.2f} USD".format(y_pred_input[0]))
            print("Predicted Salary using linear model sucessfully")
    show_predict_page()


def model_gradient():
    def load_model():
        with open("saved_steps.pkl","rb") as file:
            data = pickle.load(file)
        return data

    data = load_model()

    model = data["model_gradient"]
    le_country = data["le_country"]
    le_education = data["le_education"]

    def show_predict_page():
        st.title("Software Dev. Salary Prediction")
        st.write("""#### The Salary is predicted from Stackoverflow developer survey 2020 data using Stochastic Gradient Regressor""")
        st.write("""#### We need some information to predict the salary""")
        countries = ('United States', 'United Kingdom', 'Spain', 'Netherlands',
        'Germany', 'Canada', 'Italy', 'Brazil', 'France',
        'Poland', 'India', 'Sweden', 'Australia', 'Russian Federation')
        education_options = ("Less than a Bachelor","Bachelor’s degree","Master’s degree","Post Graduation")
        country = st.selectbox("Country",countries)
        education = st.selectbox("Education Level",education_options)

        experience = st.slider("Years of Experience",0,50)

        post = st.button("Calculate Salary")

        if post:
            X = np.array([[country,education,experience]])

            X[:,0] = le_country.transform(X[:,0])
            X[:,1] = le_education.transform(X[:,1])
            X = X.astype(float)

            y_pred_input = model.predict(X)

            st.subheader("The estimated salary is {0:.2f} USD".format(y_pred_input[0]))
            print("Predicted Salary using linear model sucessfully")
    show_predict_page()
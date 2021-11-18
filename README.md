# Salary-Predicition-using-ML
Created a WebApp where user can predict Software Developer salary by giving input various number of features such as Country , Level of Education and Work Experience. Salary is predicted using Machine Learning models such as Decision Trees , Linear Regressor and more.

The data is taken from Developer Survey result by StackOverflow 2020. The data is then cleaned and scaled before applying the regression model.

Streamlit library is used to render WebApp and link the model to a WebApp where user can input various fields in port of buttons and sliders and the python script calculates the salary based on the given input using the regression model selected.

# Prerequisites-

streamlit

numpy

pandas

pickle

scikit-learn (Need just to change something in model, not required for execution of webapp)

# Steps to run webapp -

Execute command in terminal to run WebApp -

streamlit run {destination_folder}\app.py  

# Some screenshots of the webapp

![image](https://user-images.githubusercontent.com/64198273/142244172-9b46af1e-d55a-40ad-80ce-33c193af8945.png)

![image](https://user-images.githubusercontent.com/64198273/142241726-8cca9d82-75a4-4266-8166-86c510956a27.png)

![image](https://user-images.githubusercontent.com/64198273/142241789-2af620c5-5070-4952-bedf-d7f564f33eaa.png)

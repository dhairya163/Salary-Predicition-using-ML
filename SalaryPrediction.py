# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('survey_results_public.csv')
df.head()

# %%
df = df[["Country","EdLevel","YearsCodePro","Employment","ConvertedComp"]]
df = df.rename({"ConvertedComp":"Salary"},axis=1)
df.head()

# %%
df = df[df["Salary"].notnull()]
df.head()

# %%
df.info()

# %%
df = df.dropna()

# %%
df.isnull().sum()

# %%
df = df[df["Employment"] == "Employed full-time"]

# %%
df = df.drop("Employment",axis=1)

# %%
df.info()

# %%
df["Country"].value_counts()

# %%
def country_adjust(categories,threshold):
    categorial_map={}
    for i in range(len(categories)):
        if(categories.values[i] >= threshold):
            categorial_map[categories.index[i]]=categories.index[i]
        else:
            categorial_map[categories.index[i]]="Other"
    return categorial_map


# %%
country_map = country_adjust(df["Country"].value_counts(),400)

# %%
df["Country"] = df["Country"].map(country_map)
df["Country"].value_counts()

# %%
fig , ax = plt.subplots(1,1, figsize=(12,7))
df.boxplot('Salary' , 'Country' , ax=ax)
plt.suptitle("Salary USD vs Country")
plt.title("")
plt.ylabel("Salary")
plt.xticks(rotation=90)
plt.show()

# %%
df = df[df["Salary"] <=150000]
df = df[df["Salary"] >= 10000]
df = df[df["Country"] != "Other"]

# %%
fig , ax = plt.subplots(1,1, figsize=(12,7))
df.boxplot('Salary' , 'Country' , ax=ax)
plt.suptitle("Salary USD vs Country")
plt.title("")
plt.ylabel("Salary")
plt.xticks(rotation=90)
plt.show()

# %%
df["YearsCodePro"].unique()

# %%
def clean_experience(x):
    if(x=="Less than 1 year"):
        return 0.5
    elif(x=="More than 50 years"):
        return 50
    else:
        return float(x)

# %%
df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)

# %%
df["YearsCodePro"].unique()

# %%
df["EdLevel"].unique()

# %%
def clean_education(x):
    if(x=="Bachelor’s degree (B.A., B.S., B.Eng., etc.)"):
        return "Bachelor’s degree"
    elif(x=="Master’s degree (M.A., M.S., M.Eng., MBA, etc.)"):
        return "Master’s degree"
    elif(x=="Professional degree (JD, MD, etc.)" or x=="Other doctoral degree (Ph.D., Ed.D., etc.)"):
        return "Post Graduation"
    else:
        return "Less than a Bachelor"

# %%
df["EdLevel"] = df["EdLevel"].apply(clean_education)

# %%
df["EdLevel"].value_counts()

# %%
#Label Encoding for Education and country

from sklearn.preprocessing import LabelEncoder

encoder_education = LabelEncoder()
df["EdLevel"] = encoder_education.fit_transform(df["EdLevel"])
df["EdLevel"].unique()

# %%
encoder_country = LabelEncoder()
df["Country"] = encoder_country.fit_transform(df["Country"])
df["Country"].unique()

# %%
#Training the model

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

# %%
from sklearn.linear_model import LinearRegression

linear_model = LinearRegression()
linear_model.fit(X,Y)

# %%
y_pred_linear = linear_model.predict(X)

# %%
from sklearn import metrics

error = np.sqrt(metrics.mean_squared_error(Y,y_pred_linear))
print(error)

# %%
#Let's try Decision Tree Model to reduce error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV

max_depth = [None,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
parameters = {"max_depth":max_depth}

regressor = DecisionTreeRegressor(random_state=0)

gs = GridSearchCV(regressor,parameters)
gs.fit(X,Y)


# %%
print(gs.best_estimator_)

y_pred_dtree = gs.predict(X)

error_dtree = np.sqrt(metrics.mean_squared_error(Y,y_pred_dtree))
print("${}".format(error_dtree))

# %%
#Trying Gradient Descent optimisation

from sklearn.linear_model import SGDRegressor

gradient_model = SGDRegressor()
gradient_model.fit(X,Y)

# %%
y_pred_gradient = gradient_model.predict(X)

# %%
error = np.sqrt(metrics.mean_squared_error(Y,y_pred_gradient))
print(error)

# %%
#So I will use decision tree with random_state=0 and max_depth=8

# %%
#Now I will setup my model for user input and predict the salary
X

# %%
X = np.array([["United States","Master’s degree",15]])
X

# %%
X[:,0] = encoder_country.transform(X[:,0])
X[:,1] = encoder_education.transform(X[:,1])
X = X.astype(float)
X

# %%
y_pred_input = gs.predict(X)
y_pred_input

# %%
#Saving the Models using pickle library

# %%
import pickle

# %%
data = {"model_dt":gs,"model_linear":linear_model,"model_gradient":gradient_model,"le_country":encoder_country,"le_education":encoder_education}
with open("saved_steps.pkl","wb") as file:
    pickle.dump(data,file)

# %%
with open("saved_steps.pkl","rb") as file:
    data = pickle.load(file)

model_loaded = data["model_dt"]

# %%
y_pred_loaded = model_loaded.predict(X)

# %%
print(y_pred_loaded)

# %%




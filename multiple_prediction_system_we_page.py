# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:06:19 2023

@author: 91920
"""

#importing dependencies
import pickle
import streamlit as st
from streamlit_option_menu import option_menu



#loading the models
diabetes_model=pickle.load(open("trained_model_for_diabetes_prediction.sav","rb"))

heart_model = pickle.load(open("trained_model_for_heart_disease.sav", "rb"))


#sidebar for navigation
with st.sidebar:
    selected=option_menu("Heart and Diabetes Prediction System",    #Name of the title 
                         
                         ["Diabetes Prediction","Heart Prediction"],    #Name of pagaes
                         
                         icons=["activity","heart"],                #icons for web page
                         default_index=0)   #default page
    
    
#Diabetes Prediction Page
if(selected=="Diabetes Prediction"):
    #page title
    st.title("Diabestes Prediction using ml")
   
    
   #getting the input from user
   
   #columns for input fields
    col1,col2,col3=st.columns(3)
   
    with col1:
       Pregnancies=st.text_input("Enter the number of pregnencies :")
       SkinThickness=st.text_input("Enter the SkinThickness :")
       DiabetesPedigreeFunction=st.text_input("Enter the DiabetesPedigreeFunction :")
    
    with col2:
       Glucose=st.text_input("Enter the glucose :")
       Insulin=st.text_input("Enter the Insulin :")
       Age=st.text_input("Enter the Age :")
    with col3:
       BloodPressure=st.text_input("Enter the BloodPressure :")
       BMI=st.text_input("Enter the BMI :")
 
       
    
    #code for prediction
    diabetes_diagnosis=''
    
    #creating a button for Prediction
    
    if st.button("Diabetes Test Result :"):
        diabetes_prediction=diabetes_model.predict([[float(Pregnancies),float(Glucose),float(BloodPressure),float(SkinThickness),float(Insulin),
                                                float(BMI),float(DiabetesPedigreeFunction),float(Age)]])
        if(diabetes_prediction[0]==1):
            diabetes_diagnosis="The person is Diabetic"
        
        else:
            diabetes_diagnosis="The Person is not Diabetic"
    
    st.success(diabetes_diagnosis)
        
    
    
    
  
#heart Prediction Page   
if(selected=="Heart Prediction"):
   
    #page title
    st.title("Heart Disease Prediction using ml")
    
    #getting the input from user
    
    #columns for page
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
        
       #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
        
    #code for prediction
    person_heart=""
    #creating a button for prediction
    
    if st.button("Person Heart Test Result"):
        
        heart_prediction=heart_model.predict([[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg),float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]])
        
        if(heart_prediction[0]==1):
            person_heart="Person has unhealthy heart"
        else:
            person_heart="Person has healthy heart"
        
    
    st.success(person_heart)
        
        
        
        
        
        
        
        
        
        
        
    
    
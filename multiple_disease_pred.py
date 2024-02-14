#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:37:36 2024

@author: choolwemudenda21
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_model.sav','rb'))

parkinson_model = pickle.load(open('parkinson_model.sav','rb'))

breast_cancer_model = pickle.load(open('breast_cancer_model.sav','rb'))

# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           
                           icons = ['prescription','heart-pulse','file-medical','hospital'],
                           
                           default_index = 0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
        
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
         
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'

        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
    st.success(diab_diagnosis)
    

#Heart Disease Prediction Page                
                            
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the Person')
        
    with col2:
        sex = st.text_input('Sex')
    
    with col3:
        cp = st.text_input('Chest Pain Type')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholesterol Level')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar Level ')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest')
        
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
        
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy')
        
    with col1:
        thal = st.text_input('Thalassemia')
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person does have Heart Disease'
        else:
            heart_diagnosis = 'The person does not have Heart Disease'
            
    st.success(heart_diagnosis)
    
#Breast Cancer Disease Prediction Page  
    
if (selected == 'Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
       radius_mean = st.text_input('radius')
        
    with col2:
       texture_mean  = st.text_input('texture')
        
    with col3:
       perimeter_mean  = st.text_input('perimeter')
    
    with col4:
       area_mean = st.text_input('area')
        
    with col5:
       smoothness_mean = st.text_input('smoothness') 
     
    with col1:
       compactness_mean = st.text_input('compactness')
        
    with col2:
       concavity_mean  = st.text_input('concavity')
        
    with col3:
       concave_points_mean  = st.text_input('concave')
    
    with col4:
       symmetry_mean = st.text_input('symmetry')
        
    with col5:
       fractal_dimension_mean = st.text_input('fractal dimension')  
     
    with col1:
        radius_se = st.text_input('radius (se)')
         
    with col2:
        texture_se  = st.text_input('texture (se)')
         
    with col3:
        perimeter_se  = st.text_input('perimeter (se)')
     
    with col4:
       area_se = st.text_input('area (se)')
         
    with col5:
      smoothness_se = st.text_input('smoothness (se)') 
      
    with col1:
        compactness_se = st.text_input('compactness (se)')
         
    with col2:
        concavity_se  = st.text_input('concavity (se)')
         
    with col3:
        concave_points_se  = st.text_input('concave (se)')
     
    with col4:
        symmetry_se = st.text_input('symmetry (se)')
         
    with col5:
        fractal_dimension_se = st.text_input('fractal dimension (se)')  
        
    with col1:
         radius_worst = st.text_input('radius (worst)')
          
    with col2:
         texture_worst  = st.text_input('texture (worst)')
          
    with col3:
         perimeter_worst  = st.text_input('perimeter (worst)')
      
    with col4:
        area_worst = st.text_input('area (worst)')
          
    with col5:
       smoothness_worst = st.text_input('smoothness (worst)') 
       
    with col1:
         compactness_worst = st.text_input('compactness (worst)')
          
    with col2:
         concavity_worst  = st.text_input('concavity (worst)')
          
    with col3:
         concave_points_worst  = st.text_input('concave (worst)')
      
    with col4:
         symmetry_worst = st.text_input('symmetry (worst)')
          
    with col5:
         fractal_dimension_worst = st.text_input('fractal dimension (worst)') 
         
         
    # code for Prediction
    breast_diagnosis = ''
      
    # creating a button for Prediction
      
    if st.button('Breast Cancer Test Result'):
       breast_prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])
      
       if (breast_prediction[0] == 1):
              breast_diagnosis = 'The person does have Breast Cancer'

       else:
              breast_diagnosis = 'The person does not have Breast Cancer'
              
    st.success(breast_diagnosis)
     
    
    
#Parkinsons Disease Prediction Page  
    
if (selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
       fo = st.text_input(' MDVP:Fo(Hz)')
                                    
    with col2:
       fhi  = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
       flo  = st.text_input('LMDVP:Flo(Hz)')
    
    with col4:
      jitter_percent = st.text_input('MDVP:Jitter(percentage)')
        
    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        MDVP_APQ = st.text_input('MDVP:APQ')
        
    with col4:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('Noise-to-harmonics ratio')
        
    with col1:
        HNR = st.text_input('Harmonics-to-noise ratio')
        
    with col2:
        RPDE = st.text_input('Recurrence period density entropy')
        
    with col3:
        DFA = st.text_input('Detrended fluctuation analysis')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('Correlation dimension')
        
    with col2:
        PPE = st.text_input('Pitch period entropy')
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Parkinsons Disease Test Result'):
        parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
    
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = 'The person does have Parkinsons'

        else:
            parkinsons_diagnosis = 'The person does not have Parkinsons'
            
    st.success(parkinsons_diagnosis)
    
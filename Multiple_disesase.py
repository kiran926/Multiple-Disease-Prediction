# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 10:30:16 2023

@author: kiran
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
diabetes_model = pickle.load(open('C:/Users/kiran/OneDrive/certificate/Desktop/disease/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/kiran/OneDrive/certificate/Desktop/disease/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/kiran/OneDrive/certificate/Desktop/disease/parkinsons_model.sav', 'rb'))

breast_cancer_model=pickle.load(open('C:/Users/kiran/OneDrive/certificate/Desktop/disease/breast_cancer_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction'],
                          icons=['activity','heart','person', 'person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
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
        Insulin = st.text_input('Insulin Level')
    
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
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
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
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    
    
    
    
    
    # Cancer's Prediction Page
    if (selected == 'Breast Cancer Prediction'):
        
        # page title
        st.title("Breast Cancer's Disease Prediction using ML")
        
        col1, col2, col3, col4, col5 = st.columns(5)  
        
        
            
        with col1:
            rad = st.text_input('Mean Radius')
            
        with col2:
            text = st.text_input('Mean Texture')
            
        with col3:
            peri = st.text_input('Mean Perimeter')
            
        with col4:
            area = st.text_input('Mean Area')
            
        with col5:
            smooth = st.text_input('Mean Smoothness')
            
        with col1:
            correct = st.text_input('Mean Compactness')
            
        with col2:
            conca = st.text_input('Mean Concavity')
            
        with col3:
            conp = st.text_input('Mean Concave Points')
            
        with col4:
            symm = st.text_input('Mean Symmetry')
            
        with col5:
            fd = st.text_input('Mean Fractal Dimension')
            
        with col1:
            rer = st.text_input('Radius Error')
            
        with col2:
            ter = st.text_input('Texture Error')
            
        with col3:
            perier = st.text_input('Perimeter Error')
            
        with col4:
            arer = st.text_input('Area Error')
            
        with col5:
            smooerr = st.text_input('Smoothness Error')
            
        with col1:
            comerr = st.text_input('Compactness Error')
            
        with col2:
            conerr = st.text_input('Concavity Error')
            
        with col3:
            cperr = st.text_input('Concave Points Error')
            
        with col4:
            syer = st.text_input('Symmetry Error')
            
        with col5:
            fde = st.text_input('Fractal Dimension Error')
            
        with col1:
            wr = st.text_input('Worst Radius')
            
        with col2:
                wt = st.text_input('Worst Texture')
                
        with col3:
                wp = st.text_input('Worst Perimeter')
                    
        with col4:
                 wa = st.text_input('Worst Area')
                        
        with col5:
                  ws = st.text_input('Worst Smoothness')
                            
        with col1:
                 wc = st.text_input('Worst Compactness')
                 
       
             
        with col2:
                 wco = st.text_input('Worst Concativity')
                 
        with col3:
                wcp = st.text_input('Worst Concave Points')
                     
        with col4:
                 wsy = st.text_input('Worst Symmetry')
                         
        with col5:
                   wfde = st.text_input('Worst Fractal Dimension')
                                      
            
        
        
        # code for Prediction
        cancer_diagnosis = ''
        
        # creating a button for Prediction    
        if st.button('Breast Cancer Test Result'):
            breast_cancer_prediction = breast_cancer_model.predict([[rad, text, peri, area, smooth, correct, conca, conp, symm, fd, rer, ter, perier, arer, smooerr, comerr, conerr, cperr, syer, fde, wr, wt, wp, wa, ws, wc, wco, wcp, wsy, wfde]])                          
            
            if (breast_cancer_prediction[0] == 1):
              cancer_diagnosis = "The Breast cancer is Malignant"
            else:
              cancer_diagnosis = "The Breast Cancer is Benign"
            
        st.success(cancer_diagnosis)
        
        



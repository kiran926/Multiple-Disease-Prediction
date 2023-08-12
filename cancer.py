# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:11:31 2023

@author: kiran
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/kiran/OneDrive/certificate/Desktop/disease/breast_cancer_model.sav', 'rb'))


# creating a function for Prediction

def cancer_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
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
            cancer_diagnosis = cancer_prediction.predict([[rad, text, peri, area, smooth, correct, conca, conp, symm, fd, rer, ter, perier, arer, smooerr, comerr, conerr, cperr, syer, fde, wr, wt, wp, wa, ws, wc, wco, wcp, wsy, wfde]])                          
            
           
            
st.success(cancer_diagnosis)
        
            
    
if __name__ == '__main__':
    main()

    
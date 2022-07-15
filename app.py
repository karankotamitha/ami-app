# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 18:59:10 2022

@author: amith
"""

import pickle
import streamlit as st
import numpy as np

data = pickle.load(open('Final1.pkl','rb'))
model = pickle.load(open('model1.pkl','rb'))

st.title("Medical Sample Collection Process Streamline")

#Test_Name
Test_Name = st.selectbox('Test_Name', data["Test_Name"].unique())
if Test_Name == "Acute kidney profile":
    Test_Name = 0
elif Test_Name == "HbA1c":
    Test_Name = 5
elif Test_Name == "Vitamin D-25Hydroxy":
    Test_Name = 9
elif Test_Name == "TSH":
    Test_Name = 8
elif Test_Name == "Lipid Profile":
    Test_Name = 6
elif Test_Name == "Complete Urinalysis":
    Test_Name = 2
elif Test_Name == "RTPCR":
    Test_Name = 7
elif Test_Name == "H1N1":
    Test_Name = 4
elif Test_Name == "Fasting blood sugar":
    Test_Name = 3
else:
    Test_Name = 1
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

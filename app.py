import streamlit as st
import pandas as pd
import pickle
#Make any change
with open(r"C:\Users\HP\Downloads\rf_loan_status_pipeline","rb")  as model_file:
    pipeline=pickle.load(model_file)

st.title('LoanApporal Prediction')

gender= st.selectbox("Gender",options=["male","Female"])
Married= st.selectbox("Married",options=["Married","Single"])
Dependents=st.selectbox("Dependants",options=["0","1","2","3+"])
Education=st.selectbox("Education",options=["Graduate","Not Graduate"])
Self_Employed=st.selectbox("Self_Employes",options=["Yes","No"])
ApplicantIncome=st.number.input("Applicant Income",min_value=0, value=3000)
CoapplicantIncome  =st.number.input("Coapplicant Income",min_value=0,value=0)
LoanAmount= st.number.input("Loan Amount(in thousands)",min_value=0.0,value=100.0)
Loan_Amount_Term=st.number.input("Loan Amount Term (in days)",min_value=0.0,value=365.0)
Credit_History =st.selectbox("credit history",options[1.0,0.0])
Property_Area=st.selectbox("Property Area",options["Urban", "Semiuban","Rural"])

input_dict={
    "Gender":[gender],
    "Married":[married],
    "Dependants":[dependants],
    "Education":[education],
    "Self_Employed":[self_employed],
    "ApplicantIncome":[applicanincome],
    "Coapplicantincome":[coaplicant_income],
    "LoanAmount":[loan_amount],
    "Loan_Amount_Term":[loan_amount_term],
    "Credit_History":[credit_history],
    "Property_Area":[property_area],
}

input_df= pd.DataFrame(input_dict)


if st.button("Predict Loan Status"):
    prediction=pipeline.predict(input_df)
    loan_status_map= {0:"Loan Denied", 1:"Loan Approved"}

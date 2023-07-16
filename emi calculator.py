import streamlit as st
def calculate_emi(p,n,r):
	emi = (p*(r/100)*((1+r/100)**n))/(((1+r/100)**n)-1)
	st.write("EMI calculated = ₹",emi)
st.title("EMI calculator.")
p=st.slider("Enter principal amount:",1,10000)
n=st.slider("Enter time borrowed for, in months:" 1,36)
r=st.slider("Enter rate of interest:",1,15)
n=n*12
r=r/12
if st.button("calculate"):
	calculate_emi(p,n,r)

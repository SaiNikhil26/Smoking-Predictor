import streamlit as st
import pickle
pickle_in = open("smoking.pkl","rb")
clf = pickle.load(pickle_in)


def prediction(gender,age,height,weight,waist,eyesight_left,eyesight_right,hearing_left,hearing_right,systolic,relaxation,sugar,cholestrol,triglyceride,HDL,LDL,Heamoglobin,Urine,serum,AST,ALT,GTP,dental_carries,tartar):
    predict = clf.predict([[gender,age,height,weight,waist,eyesight_left,eyesight_right,hearing_left,hearing_right,systolic,relaxation,sugar,cholestrol,triglyceride,HDL,LDL,Heamoglobin,Urine,serum,AST,ALT,GTP,dental_carries,tartar]])
    print(predict)
    return predict
def main():
    st.title("Smoking Preidctor")
    
    gender = st.number_input("Gender")
    age = st.number_input("Age")
    height = st.number_input("Height")
    weight = st.number_input("Weight")
    waist = st.number_input("Waist")
    eyesight_left = st.number_input("Eyesight-left")
    eyesight_right = st.number_input("Eyesight-right")
    hearing_left = st.number_input("Hearing-left")
    hearing_right = st.number_input("Hearing-right")
    systolic = st.number_input("Systolic")
    relaxation = st.number_input("Relaxation")
    sugar = st.number_input("Bloos-Sugar")
    cholestrol = st.number_input("Cholestrol")
    triglyceride = st.number_input("Triglyceride")
    HDL = st.number_input("HDL")
    LDL = st.number_input("LDL")
    Heamoglobin = st.number_input("Heamoglobin")
    Urine = st.number_input("Urine Protein")
    serum = st.number_input("Serum Creatinine")
    AST = st.number_input("AST")
    ALT = st.number_input("ALT")
    GTP = st.number_input("GTP")
    dental_carries = st.number_input("Dental Carries")
    tartar = st.number_input("Tartar")
    result = "";
    if st.button("Predict"):
        result = prediction(gender, age, height, weight, waist, eyesight_left, eyesight_right, hearing_left, hearing_right, systolic, relaxation, sugar, cholestrol, triglyceride, HDL, LDL, Heamoglobin, Urine, serum, AST, ALT, GTP, dental_carries, tartar)
    st.success("Smoking : {}".format(result))
    if st.button("About"):
        st.text("Learn about smoking")
        
if __name__=='__main__':
    main()
    
import streamlit as st
import numpy as np
#import pandas as pd
from SalaryFunction import process


st.title('Расчет зарплаты')
#title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)


if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
st.text("Введите данные из резюме.")
col1, col2, col3 = st.columns(3)

with col1:
    age_class = st.text_input("Возраст",value="18")
    age_class=int(age_class)
    if(age_class<18):
        age_class=0
    elif(age_class<23):
        age_class=1
    elif(age_class<28):
        age_class=2
    elif(age_class<33):
        age_class=3
    elif(age_class<38):
        age_class=4
    elif(age_class<43):
        age_class=5
    elif(age_class<48):
        age_class=6
    elif(age_class<53):
        age_class=7
    elif(age_class<58):
        age_class=8
    elif(age_class<63):
        age_class=9
    else:
        age_class=10
    sex_class = st.radio(
        "Пол",
        options=["Муж.", "Жен."],
    )
    if(sex_class=="Муж."):sex_class=0
    if(sex_class=="Жен."):sex_class=1
    # Список порогов опыта работы в месяцах
    experience_class = st.text_input("Опыт работы лет.",value="5")
    experience_class=float(experience_class)
    experience_class=experience_class*12
    if(experience_class<7):
        experience_class=0
    elif(experience_class<13):
        experience_class=1
    elif(experience_class<25):
        experience_class=2
    elif(experience_class<37):
        experience_class=3
    elif(experience_class<61):
        experience_class=4
    elif(experience_class<97):
        experience_class=5
    elif(experience_class<121):
        experience_class=6
    elif(experience_class<157):
        experience_class=7
    elif(experience_class<193):
        experience_class=8
    elif(experience_class<241):
        experience_class=9
    else:
        experience_class=10
    education_class = st.radio(
        "Образование",
        options=["высшее образование", "среднее специальное", "неоконченное высшее", "среднее образование"],
    )
    if(education_class=="высшее образование"):education_class=0
    if(education_class=="среднее специальное"):education_class=1
    if(education_class=="неоконченное высшее"):education_class=2
    if(education_class=="среднее образование"):education_class=3

with col2:
    employment_class = st.radio("Вид занятости",options=["стажировка", "частичная занятость", "проектная работа", "полная занятость"],)
    if(employment_class=="стажировка"):employment_class=0
    if(employment_class=="частичная занятость"):employment_class=1
    if(employment_class=="проектная работа"):employment_class=2
    if(employment_class=="полная занятость"):employment_class=3
    schedule_class = schedule_class = st.radio(
        "График работы",
        options=["гибкий график", "полный день", "сменный график", "удаленная работа"],
    )
    if(schedule_class=="гибкий график"):schedule_class=0
    if(schedule_class=="полный день"):schedule_class=1
    if(schedule_class=="сменный график"):schedule_class=2
    if(schedule_class=="удаленная работа"):schedule_class=3
with col3:

    city_class = st.radio(
        "Город",
        options=["Москва", "Санкт-петербург", "Города милионники", "прочие города"],
    )
    if(city_class=="Москва"):city_class=0
    if(city_class=="Санкт-петербург"):city_class=1
    if(city_class=="Города милионники"):city_class=2
    if(city_class=="прочие города"):city_class=3
city_ohe = np.eye(4)[city_class]
empl_multi=np.eye(4)[employment_class]
sсhed_multi=np.eye(4)[schedule_class]
edu_multi = np.eye(4)[education_class]
exp_ohe = np.eye(11)[experience_class]
sex_vec = np.array([sex_class])                               # Пол в виде вектора
age_ohe = np.eye(11)[age_class]
x_data = np.hstack([sex_vec,age_ohe,city_ohe,empl_multi,sсhed_multi,edu_multi,exp_ohe])
x_data = x_data[np.newaxis,...] 
print(x_data.shape)

col11 = st.columns(1)
job_description = st.text_input("Желаемая должность",value="грузчик")
st.text("Приблизительная зарплата на 2020 год.")
#st.text(x_data)
#st.text(str(city_ohe)+str(empl_multi)+str(sсhed_multi))
#st.text(str(edu_multi)+str(exp_ohe))
#st.text(str(sex_vec)+str(age_ohe))
prd=process(x_data,job_description)
st.text(str(int(prd[0]*1000))+"руб.")

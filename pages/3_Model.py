import streamlit as st
from PIL import Image
import pandas as pd

st.markdown("<div style='text-align: center;'><h2>Model Prediksi</h2></div>", unsafe_allow_html=True)
tab1,tab2, = st.tabs(['Sebelum Skew','Setelah Skew'])
with tab1:
    st.subheader('Linear Regression')
    linear = {'Metric': ['Mean Squared Error ln', 'R-squared ln', 'Mean Absolute Error ln'],
            'Value': [4.50089873042597e+18, 0.634080550137397, 1091250163.8639235]}
    st.table(linear)
    gambar1 = 'gambar/linear_sebelum_skew.png'
    Image1 = Image.open(gambar1)
    st.image(Image1,use_column_width=True)
    st.write('')
    st.write('')
    st.subheader('Random Forest Regressor')
    random = {'Metric': ['Mean Squared Error rf', 'R-squared rf', 'Mean Absolute Error rf'],
                'Value': [3.105875507823839e+18, 0.7474948170946577, 709595333.3977281]}
    st.table(random)
    gambar2 = ('gambar/random_forest_sebelum_skew.png')
    Image2 = Image.open(gambar2)
    st.image(Image2,use_column_width=True)
    st.write('')
    st.write('')
    st.subheader('Gradient Boosting Regressor')
    gradient = {'Metric': ['Mean Squared Error gb', 'R-squared gb', 'Mean Absolute Error gb'],
                'Value': [3.2093667243187067e+18, 0.7390810643591392, 783584729.4671302]}
    st.table(gradient)
    gambar3 = ('gambar/gradirnt_sebelum_skew.png')
    Image3 = Image.open(gambar3)
    st.image(Image3,use_column_width=True)
    st.write("""Mean squared Error jika semkain mendekati 0 maka model semakin baik dan 
             R square disebut juga sebagai koefisien determinasi yang menjelaskan seberapa jauh data dependen dapat dijelaskan oleh data independen. R square bernilai antar 0 - 1 dengan ketentuan semakin mendekati angka satu berarti semakin baik.
             semakin kecil nilai Mean Absolte Error, semakin baik model dalam melakukan prediksi""")    
    st.write("""Berhubung nilai mean squared error dan mean absolute extreme maka saya cari cara lainya untuk mengatasi nilai extreme""")
    st.write('')
    st.write('')
    st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")
with tab2:
    st.subheader('fitur sebelum dan sesudah di skew')
    gambar4 = ('gambar/harga_tans.png')
    image1 = Image.open(gambar4)
    st.image(image1,use_column_width=True)
    gambar5 = ('gambar/harga_box_trans.png')
    image2 = Image.open(gambar5)
    st.image(image2,use_column_width=True)
    gambar6 = ('gambar/kamar_mandi_setelah_skew.png')
    image3 = Image.open(gambar6)
    st.image(image3,use_column_width=True)
    gambar7 = ('gambar/kamar_mandi_box.png')
    image4 = Image.open(gambar7)
    st.image(image4,use_column_width=True)
    gambar8 = ('gambar/kamar_tidur_skew.png')
    image5 = Image.open(gambar8)
    st.image(image5,use_column_width=True)
    gambar9 = ('gambar/kamar_tidur_box.png')
    image6 = Image.open(gambar9)
    st.image(image6,use_column_width=True)
    gambar10 = ('gambar/bangunan_setelah_skew.png')
    image7 = Image.open(gambar10)
    st.image(image7,use_column_width=True)
    gambar11 = ('gambar/bangunan_box.png')
    image8 = Image.open(gambar11)
    st.image(image8,use_column_width=True)
    gambar12 = ('gambar/lahan_setelah_skew.png')
    image9 = Image.open(gambar12)
    st.image(image9,use_column_width=True)
    gambar13 = ('gambar/lahan_box.png')
    image10 = Image.open(gambar13)
    st.image(image10,use_column_width=True)
    st.write("""Skewness adalah derajat ketidaksimetrisan suatu distribusi. 
             Jika kurva frekuensi suatu distribusi memiliki ekor yang lebih memanjang ke kanan (dilihat dari meannya) maka dikatakan menceng kanan (positif) dan jika sebaliknya maka menceng kiri (negatif)""")
    st.write("""dalam kasus ini saya menggunakan skew 0.75 karena kemiringanya ke kanan yang berarti positif
             agar lebih simetris""")
    st.write('terlihat ada perubahan di visualisasi di atas')
    st.write('')
    st.write('')
    st.subheader('Linear Regression')
    ln = {'Metric': ['Mean Squared Error ln', 'R-squared ln', 'Mean Absolute Error ln'],
            'Value': [0.1859715810743271, 0.789036672196951, 0.3160616356220432]}
    st.table(ln)
    gambar14 = ('gambar/linear_setekah_skew.png')
    image11 = Image.open(gambar14)
    st.image(image11,use_column_width=True)
    st.write('')
    st.write('')
    st.subheader('Random Forest Regressor')
    rf = {'Metric': ['Mean Squared Error rf', 'R-squared rf', 'Mean Absolute Error rf'],
            'Value': [0.13269650123022314, 0.8494711109857108, 0.24430893204296192]}
    st.table(rf)
    gambar15 = ('gambar/random_forest_setelah_skew.png')
    image12 = Image.open(gambar15)
    st.image(image12,use_column_width=True)
    st.write('')
    st.write('')
    st.subheader('Gradient Boosting Regressor')
    gb = {'Metric': ['Mean Squared Error gb', 'R-squared gb', 'Mean Absolute Error gb'],
            'Value': [0.13921246620405128, 0.842079499607317, 0.2694133120359327]}
    st.table(gb)
    gambar16 = ('gambar/gradirnt_setelah_skew.png')
    image13 = Image.open(gambar16)
    st.image(image13,use_column_width=True)
    st.write("""setelah melakukan skewnees terlihat skor dari MAE,MSE dan R squared normal,
             berhubung nilai dari random forest paling bagus maka putuskan menggunakan random forest""")
    st.write('')
    st.write('')
    st.subheader('Tuning Random Forest Regressor')
    data_best_model = {'Model': ['Random Forest'],
                        'Mean Squared Error': [0.13027233630759524],
                        'R-squared': [0.8522210467353919],
                        'Mean Absolute Error': [0.24047288646915016],
                        'Best Parameters': [{'max_depth': None, 'max_features': 'auto', 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 150}]}
    st.table(data_best_model)
    gambar17 = ('gambar/random_forest_tuning.png')
    image14 = Image.open(gambar17)
    st.image(image14,use_column_width=True)
    st.write("""Tuning dilakuakan dengan mencari best_params dengan GridCV,
             nilai setelah tuning ada peningkatan""")
    st.write('')
    st.write('')
    st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")
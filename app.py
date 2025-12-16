import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.title("SISTEM DETEKSI STUNTING ANAK")
# st.write("Aplikasi Streamlit pertamaku 🚀")

st.markdown("""
           <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
        """, unsafe_allow_html=True)

with open("styles/style.css") as f:
    css = f"<style>{f.read()}</style>"

# layout
row1 = st.container()
row2 = st.container()

# ========================= start baris 1 =========================

col1,col2 = st.columns([1,4])
# ========================= kolom 1 baris 1 =========================
with col2:
    tile = st.container(height=1000)

    with tile :
        st.markdown("""
            <div class="header-title">
            Visualisasi Data
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div class="space">
               
            </div>
        """, unsafe_allow_html=True)
        
        con1 = st.container(height=80)
        # con2 = st.container(height=400)
        with con1 :
            st.caption("Model klasifikasi ini menggunakan algoritma K-Nearest Neighbors (KNN) dilatih menggunakan dataset yang berfokus pada deteksi stunting, bersumber dari pengukuran balita di Lombok Timur, Nusa Tenggara Barat (NTB), yang dikumpulkan pada Februari 2024.")
 
        st.subheader("Visualisasi Data Stunting")
        col11,col12 = st.columns(2)
        col23,col24 = st.columns(2)
        df = pd.read_csv('dataset/data_stunting.csv')
        df_after = pd.read_csv('dataset/after_tranform.csv')

        # merubah type data
        num_cols = ['Birth Weight', 'Birth Height', 'Weight', 'Height']
        cat_cols = ['BB/U','TB/U', 'BB/TB']
        # df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], errors='coerce')

        for i in df.columns :
            if i in num_cols :
                df[i] = df[i].astype('float')
            if i in cat_cols :
                df[i] = df[i].astype('category')
        
        df['Birth Height'] = df['Birth Height'].fillna(df['Birth Height'].mean())
        df['Birth Weight'] = df['Birth Weight'].fillna(df['Birth Weight'].mean())
 
        with col11:
            st.markdown(
                """
                <div style="
                    background-color:#264c8a;
                    padding:10px;
                    border-radius:10px 10px 0 0;
                    color:white;
                    font-weight:bold;
                    font-size:18px;">
                    Berat Lahir
                </div>
                """,
                unsafe_allow_html=True
            )
            fig, ax = plt.subplots(figsize=(4,2))
            ax.hist(df['Birth Weight'])
            ax.set_title("Distribusi Berat Lahir")
            ax.set_xlabel("Berat Lahir")
            ax.set_ylabel("Frekuensi")
            st.pyplot(fig)

        with col12:
            st.markdown(
                """
                <div style="
                    background-color:#264c8a;
                    padding:10px;
                    border-radius:10px 10px 0 0;
                    color:white;
                    font-weight:bold;
                    font-size:18px;">
                    Tinggi Lahir
                </div>
                """,
                unsafe_allow_html=True
            )
            fig, ax = plt.subplots(figsize=(4,2))
            ax.hist(df['Birth Height'])
            ax.set_title("Distribusi Tinggi Lahir")
            ax.set_xlabel("Tinggi Lahir")
            ax.set_ylabel("Frekuensi")
            st.pyplot(fig)

    
        with col23:
            st.markdown(
                """
                <div style="
                    background-color:#264c8a;
                    padding:10px;
                    border-radius:10px 10px 0 0;
                    color:white;
                    font-weight:bold;
                    font-size:18px;">
                    Berat
                </div>
                """,
                unsafe_allow_html=True
            )
            fig, ax = plt.subplots(figsize=(4,2))
            ax.hist(df['Weight'])
            ax.set_title("Distribusi Berat")
            ax.set_xlabel("Berat")
            ax.set_ylabel("Frekuensi")
            st.pyplot(fig)

        with col24:
            st.markdown(
                """
                <div style="
                    background-color:#264c8a;
                    padding:10px;
                    border-radius:10px 10px 0 0;
                    color:white;
                    font-weight:bold;
                    font-size:18px;">
                    Tinggi
                </div>
                """,
                unsafe_allow_html=True
            )
            fig, ax = plt.subplots(figsize=(4,2))
            ax.hist(df['Height'])
            ax.set_title("Distribusi Tinggi")
            ax.set_xlabel("Tinggi")
            ax.set_ylabel("Frekuensi")
            st.pyplot(fig)
        
        st.subheader("Heat Map")
    

        conHeatMap = st.container()
        with conHeatMap :
        
            colHeat, colHeat2 = st.columns(2)
            with colHeat :
                st.markdown(
                    """
                    <div style="
                        background-color:#264c8a;
                        padding:10px;
                        border-radius:10px 10px 0 0;
                        color:white;
                        font-weight:bold;
                        font-size:18px;">
                        Tinggi
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                fig, ax = plt.subplots(figsize=(4, 3))

                corr = df[['Birth Height', 'Birth Weight','Weight', 'Height']].corr()

                sns.heatmap(
                    corr,
                    annot=True,
                    cmap="Blues",
                    fmt=".2f",
                    ax=ax
                )

                ax.set_title("Heatmap Korelasi")

                st.pyplot(fig)
        
        st.subheader("Distribusi Status Stunting Berdasarkan Jumlah anak")
        
        conComp = st.container()
        with conComp :
        
            colComp, colComp2 = st.columns(2)
            with colComp :
                st.markdown(
                    """
                    <div style="
                        background-color:#264c8a;
                        padding:10px;
                        border-radius:10px 10px 0 0;
                        color:white;
                        font-weight:bold;
                        font-size:18px;">
                        Tinggi
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                fig, ax = plt.subplots(figsize=(4, 2))

                sns.countplot(
                    data=df,
                    x="TB/U",
                    order=df["TB/U"].value_counts().index,
                    ax=ax
                )

                ax.set_title("Distribusi TB/U")
                ax.set_xlabel("Kategori TB/U")
                ax.set_ylabel("Frekuensi")

                st.pyplot(fig)

        st.subheader("Boxplot Data Stunting Sebelum dan Sesudah Normalisasi Box Cox")

        conBoxPlot = st.container()
        with conBoxPlot :
        
            colBoxPlot, colBoxPlot2 = st.columns(2)
            with colBoxPlot :
                st.markdown(
                    """
                    <div style="
                        background-color:#264c8a;
                        padding:10px;
                        border-radius:10px 10px 0 0;
                        color:white;
                        font-weight:bold;
                        font-size:18px;">
                        Before
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                fig, ax = plt.subplots(figsize=(4,2))
                ax.boxplot(df[['Birth Height', 'Birth Weight','Weight', 'Height']])
                ax.set_title("Distribusi Tinggi")
                ax.set_xlabel("Tinggi")
                ax.set_ylabel("Frekuensi")
                st.pyplot(fig)

            with colBoxPlot2 :
                st.markdown(
                    """
                    <div style="
                        background-color:#264c8a;
                        padding:10px;
                        border-radius:10px 10px 0 0;
                        color:white;
                        font-weight:bold;
                        font-size:18px;">
                        After
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                fig, ax = plt.subplots(figsize=(4,2))
                ax.boxplot(df_after[['Birth Height', 'Birth Weight','Weight', 'Height']])
                ax.set_title("Distribusi Tinggi")
                ax.set_xlabel("Tinggi")
                ax.set_ylabel("Frekuensi")
                st.pyplot(fig)
        
        
        st.subheader("Hasil Klasifikasi dan Evaluasi")

        conEval = st.container()
        with conEval :
        
            colEval, colEval2 = st.columns(2)
            with colEval :
                metrics_df = pd.DataFrame({
                    "Metrik Kinerja": ["Accuracy", "Precision", "Recall", "F1-score"],
                    "Nilai Model": ["75,76%", "81,82%", "75,76%", "67,79%"]
                })

                st.table(metrics_df)


        
# ========================= kolom 2 baris 1 =========================
with col1:
    tile = st.container(height=1000)

    with tile :
        st.markdown("""
            <div class="header-title">
            Input Dataa
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="space">
               
            </div>
        """, unsafe_allow_html=True)

        tanggal = st.date_input("Tanggal Lahir")
        BeratLahir = st.number_input("Berat Lahir (Kg)")
        TinggiLahir = st.number_input("Tinggi Lahir (Kg)")
        BeratSekarang = st.number_input("Berat Sekarang (Kg)")
        TinggiSekarang = st.number_input("Tinggi Sekarang (Kg)")

        if st.button("Prediksi"):
            st.write("Button diklik!")
    


        

st.markdown(css, unsafe_allow_html=True)

# suntikkan ke streamlit
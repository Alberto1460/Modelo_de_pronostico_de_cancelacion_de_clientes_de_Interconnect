import streamlit as st
import pandas as pd
import pickle
import xgboost 

st.set_page_config(
    page_title='Mi App-Cancelación de Clientes',
    page_icon='🔮'
)

# Titulo de la aplicación
st.title("Predicción de Cancelación de Clientes en Interconnect 🌐")

st.write('Ingresa los siguientes datos para saber si un cliente abandonará o no la empresa Interconnect')

# Usar la barra lateral para agrupar las entradas
st.sidebar.header('Datos del cliente')

# 1. Entradas para variables binarias (LabelEncoder)
paperlessbilling = st.sidebar.selectbox("Paperless Billing", ['Yes', 'No'])
onlinesecurity = st.sidebar.selectbox('Online Security', ['Yes', 'No'])
onlinebackup = st.sidebar.selectbox('Online Backup', ['Yes', 'No'])
deviceprotection = st.sidebar.selectbox('Device Protection', ['Yes', 'No'])
techsupport = st.sidebar.selectbox('Tech Support', ['Yes', 'No'])
streamingtv = st.sidebar.selectbox('Streaming Tv', ['Yes', 'No'])
streamingmovies = st.sidebar.selectbox('Streaming Movies', ['Yes', 'No'])
partner = st.sidebar.selectbox('Partner', ['Yes', 'No'])
dependents = st.sidebar.selectbox('Dependents', ['Yes', 'No'])
multiplelines = st.sidebar.selectbox('Multiple Lines', ['Yes', 'No'])

# 2. Entradas para variables numéricas
monthlycharges = st.sidebar.number_input('Monthly Charges', min_value=0.0, value=50.0)
totalcharges = st.sidebar.number_input('Total Charges', min_value=0.0, value=1000.00)
total_days = st.sidebar.number_input('Total Days', min_value=0.0, value=365.0)
total_months = st.sidebar.number_input('Total Month', min_value=0.0, value=12.0)
seniorcitizen = st.sidebar.number_input('Senior Citizen 0 = No, 1 = Si', min_value=0.0, max_value=1.0, value=0.0)

# 3. Entradas para variables categóricas que luego se codificarán con OneHotEncoder
# (Estas son las variables originales: 'type', 'paymentmethod', 'internetservice', 'gender')
type = st.sidebar.selectbox('Type Option', ['one_year', 'two_year'])
paymentmethod = st.sidebar.selectbox('Payment Method', ['credit card (automatic)', 'electronic check', 'mailed check'])
internetservice = st.sidebar.selectbox('Internet Option', ['fiber optic', 'dsl', 'no'])
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])

# Botón para procesar (usando st.form para agrupar entradas)
with st.form(key='form_input'):
    st.subheader('Revisa los datos ingresados')
    st.write({"paperlessbilling": paperlessbilling,
        "onlinesecurity": onlinesecurity,
        "onlinebackup": onlinebackup,
        "deviceprotection": deviceprotection,
        "techsupport": techsupport,
        "streamingtv": streamingtv,
        "streamingmovies": streamingmovies,
        "partner": partner,
        "dependents": dependents,
        "multiplelines": multiplelines,
        "seniorcitizen": seniorcitizen,
        "monthlycharges": monthlycharges,
        "totalcharges": totalcharges,
        "total_days": total_days,
        "total_months": total_months,
        "type": type,
        "paymentmethod": paymentmethod,
        "internetservice": internetservice,
        "gender": gender})
    susbmit_button = st.form_submit_button(label='Predecir')

if susbmit_button:
# 4. Crear un diccionario con los datos ingresados (en el formato original)
    input_data = {
        "paperlessbilling": paperlessbilling,
        "onlinesecurity": onlinesecurity,
        "onlinebackup": onlinebackup,
        "deviceprotection": deviceprotection,
        "techsupport": techsupport,
        "streamingtv": streamingtv,
        "streamingmovies": streamingmovies,
        "partner": partner,
        "dependents": dependents,
        "multiplelines": multiplelines,
        "seniorcitizen": seniorcitizen,
        "monthlycharges": monthlycharges,
        "totalcharges": totalcharges,
        "total_days": total_days,
        "total_months": total_months,
        "type": type,
        "paymentmethod": paymentmethod,
        "internetservice": internetservice,
        "gender": gender
}

    # Convertir la respuesta a minúsculas
    for key in input_data:
        if isinstance(input_data[key], str):
            input_data[key] = input_data[key].lower()
        
    # Mostrar los datos ingresados en formato JSON (más limpio)
    st.subheader('Datos ingresados')
    st.json(input_data)

    # Convertir el diccionario en un DataFrame (una sola fila)
    df_input = pd.DataFrame([input_data])

    # 5. Cargar el preprocesador y el modelo
    with open("app/preprocesador.pkl", "rb") as file:
        preprocesador = pickle.load(file)

    # Código para cargar el Modelo
    with open("app/model.pkl", "rb") as file:
        model = pickle.load(file)

    # Paso 6: Aplicar el Preprocesamiento
    # 6a. Aplicar LabelEncoder a las columnas correspondientes
    for columna, encoder in preprocesador['label_encoders'].items():
        if columna in df_input.columns:
            df_input[columna] = encoder.transform(df_input[columna])


    # 6b. Aplicar OneHotEncoder a las variables categóricas
    columnas_onehot = ['type', 'paymentmethod', 'internetservice', 'gender']
    if preprocesador['onehot_encoder'] is not None:
        onehot_encoder = preprocesador['onehot_encoder']
        # Transformar y convertir a DataFrame
        df_onehot = onehot_encoder.transform(df_input[columnas_onehot])
        df_onehot = pd.DataFrame(df_onehot, columns=onehot_encoder.get_feature_names_out(columnas_onehot))
        df_input = df_input.drop(columns=columnas_onehot).reset_index(drop=True)
        df_input = pd.concat([df_input, df_onehot], axis=1)

    # Reordenar las columnas de la Aplicación con las del modelo

    # Obtener el nombre de las columnas del modelo
    columnas_modelo = model.get_booster().feature_names

    # Asegurar que input tenga las mismas columnas y ordenadas que cuando se entrenó el modelo
    df_input = df_input.reindex(columns=columnas_modelo)


    # 7. Ejecutar la predicción
    prediction = model.predict(df_input)
    if prediction == 1:
        st.error('❌ El modelo predice cancelación del cliente')
    else:
        st.success('✅ El modelo predice que el cliente no abandonará la empresa')
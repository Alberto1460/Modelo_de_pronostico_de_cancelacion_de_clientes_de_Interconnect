# 📌 Predicción de Cancelación de Clientes en Interconnect 🌐

Este proyecto es una aplicación desarrollada con **Streamlit** que permite predecir si un cliente de la empresa **Interconnect** cancelará su servicio. Utiliza un modelo de **XGBoost** entrenado con datos de clientes.

🔗 **Prueba la aplicación en vivo aquí:** [Predicción de Cancelación de Clientes](https://modelodepronosticodecancelaciondeclientesdeinterconnect.streamlit.app/)

---

## 🚀 Tecnologías utilizadas
- **Python** 🐍
- **Streamlit** 🖥️
- **Pandas** 📊
- **XGBoost** 📈
- **Pickle** (para cargar el modelo y preprocesador) 📦

---

## 📂 Estructura del Proyecto
```
Modelo_de_pronostico_de_cancelacion_de_clientes_de_Interconnect/
│── aplicación/
│   ├── app.py  # Código de la aplicación en Streamlit
│   ├── modelo.pkl  # Modelo entrenado en XGBoost
│   ├── preprocesador.pkl  # Preprocesador (LabelEncoder y OneHotEncoder)
│── datos/  # Datos utilizados en el entrenamiento
│── cuaderno/  # Notebook con el entrenamiento del modelo
│── requirements.txt  # Librerías necesarias para ejecutar la aplicación
│── README.md  # Este archivo
```

---

## 📥 Instalación y Ejecución
Si deseas ejecutar la aplicación en tu equipo local, sigue estos pasos:

1. **Clonar el repositorio:**
```sh
    git clone https://github.com/Alberto1460/Modelo_de_pronostico_de_cancelacion_de_clientes_de_Interconnect.git
    cd Modelo_de_pronostico_de_cancelacion_de_clientes_de_Interconnect
```

2. **Crear un entorno virtual (opcional pero recomendado):**
```sh
    python -m venv env
    source env/bin/activate  # En Mac/Linux
    env\Scripts\activate  # En Windows
```

3. **Instalar las dependencias:**
```sh
    pip install -r requirements.txt
```

4. **Ejecutar la aplicación:**
```sh
    streamlit run aplicación/app.py
```

---

## 🎯 Uso de la Aplicación
1. Introduce los datos del cliente en la barra lateral.
2. Haz clic en **"Predecir"**.
3. La aplicación mostrará si el cliente **cancelará** o **no cancelará** el servicio.

---

## 📷 Vista Previa
Se adjutan 3 imágenes de las vistas previas de la Aplicación!
![cv1](https://github.com/user-attachments/assets/82378012-b795-484d-a88f-abb6cce425ab)
![cv2](https://github.com/user-attachments/assets/e1c9db9e-5598-42c8-8fe9-46d82dc85e23)
![cv3](https://github.com/user-attachments/assets/6b207ae9-cd7d-47c0-8a0e-bdf35c2562d3)



---

## ✨ Autor
- **Alberto1460** 👨‍💻
- 📧 Contacto: *(albertoabl_010@hotmail.com)*

¡Espero que este proyecto te sea útil! No dudes en dar ⭐ al repositorio si te gusta.

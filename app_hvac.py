import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="App HVAC", page_icon="❄️", layout="centered")

# --- Encabezado ---
st.markdown("""
    <h1 style='text-align: center; color: #0e7490;'>❄️ App Básica HVAC</h1>
    <p style='text-align: center; font-size: 16px; color: #555;'>
    Herramienta rápida para conversiones y cálculos de carga térmica y ventilación.
    </p>
    <hr>
""", unsafe_allow_html=True)

# ==============================
# Conversión de Temperatura
# ==============================
st.subheader("🌡 Conversión de Temperatura")
with st.container():
    temp = st.number_input("Introduce la temperatura:", value=0.0, step=0.1)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("°C ➡ °F"):
            fahrenheit = (temp * 9/5) + 32
            st.success(f"**{fahrenheit:.2f} °F**")
    with col2:
        if st.button("°F ➡ °C"):
            celsius = (temp - 32) * 5/9
            st.success(f"**{celsius:.2f} °C**")

st.markdown("---")

# ==============================
# Cálculo Carga Térmica
# ==============================
st.subheader("🔥 Cálculo Carga Térmica (BTU/h)")
with st.container():
    area = st.number_input("Área (m²):", value=0.0, step=0.1)
    altura = st.number_input("Altura (m):", value=0.0, step=0.1)
    delta_t = st.number_input("ΔT (°C):", value=0.0, step=0.1)

    if st.button("Calcular Carga Térmica"):
        carga = area * altura * delta_t * 1.2
        st.success(f"**Carga Térmica: {carga:.2f} BTU/h**")

st.markdown("---")

# ==============================
# Cálculo de CFM
# ==============================
st.subheader("💨 Cálculo de CFM")
with st.container():
    volumen = st.number_input("Volumen (m³):", value=0.0, step=0.1)
    ach = st.number_input("Renovaciones por hora (ACH):", value=0.0, step=0.1)

    if st.button("Calcular CFM"):
        cfm = (volumen * ach) / 60
        st.success(f"**CFM: {cfm:.2f}**")

# ==============================
# Pie de página
# ==============================
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray; font-size: 12px;'>
    🛠 Desarrollado para cálculos rápidos en campo HVAC
    </p>
""", unsafe_allow_html=True)
📌 Instrucciones para ejecutarlo
Instala Streamlit si no lo tienes:

bash
Copiar
Editar
pip install streamlit
Guarda el código como:

Copiar
Editar
app_hvac.py
En la terminal, ejecuta:

bash
Copiar
Editar
streamlit run app_hvac.py
Se abrirá en tu navegador con un diseño más moderno y ordenado.

Si quieres, puedo añadirle funciones extra como:

Cálculo de toneladas de refrigeración a partir de BTU/h.

Historial de cálculos para no perder los resultados.

Opción para exportar los cálculos a PDF.

¿Quieres que te lo prepare ya con esas funciones extra?








Dijiste:
si agregalo


ChatGPT dijo:
Listo 🚀, te voy a dejar tu App HVAC Web en Streamlit con:

Conversión de temperatura (°C ↔ °F)

Cálculo de carga térmica (BTU/h)

Conversión de BTU/h a Toneladas de refrigeración

Cálculo de CFM

Historial de cálculos guardado mientras uses la app

Exportación a PDF con los resultados

Aquí tienes el código completo:

python
Copiar
Editar
import streamlit as st
from fpdf import FPDF

# =========================
# CONFIGURACIÓN DE LA PÁGINA
# =========================
st.set_page_config(page_title="App HVAC", page_icon="❄️", layout="centered")

# Variable para historial
if "historial" not in st.session_state:
    st.session_state.historial = []

# =========================
# FUNCIÓN PARA EXPORTAR PDF
# =========================
def exportar_pdf(historial):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Reporte de Cálculos HVAC", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(10)

    for item in historial:
        pdf.multi_cell(0, 8, f"- {item}")

    nombre_archivo = "reporte_hvac.pdf"
    pdf.output(nombre_archivo)
    return nombre_archivo

# =========================
# ENCABEZADO
# =========================
st.markdown("""
    <h1 style='text-align: center; color: #0e7490;'>❄️ App Profesional HVAC</h1>
    <p style='text-align: center; font-size: 16px; color: #555;'>
    Herramienta para conversiones y cálculos de HVAC con historial y exportación a PDF.
    </p>
    <hr>
""", unsafe_allow_html=True)

# =========================
# CONVERSIÓN DE TEMPERATURA
# =========================
st.subheader("🌡 Conversión de Temperatura")
temp = st.number_input("Introduce la temperatura:", value=0.0, step=0.1)

col1, col2 = st.columns(2)
with col1:
    if st.button("°C ➡ °F"):
        fahrenheit = (temp * 9/5) + 32
        resultado = f"{temp:.2f} °C = {fahrenheit:.2f} °F"
        st.success(resultado)
        st.session_state.historial.append(resultado)
with col2:
    if st.button("°F ➡ °C"):
        celsius = (temp - 32) * 5/9
        resultado = f"{temp:.2f} °F = {celsius:.2f} °C"
        st.success(resultado)
        st.session_state.historial.append(resultado)

st.markdown("---")

# =========================
# CÁLCULO DE CARGA TÉRMICA
# =========================
st.subheader("🔥 Cálculo Carga Térmica (BTU/h)")
area = st.number_input("Área (m²):", value=0.0, step=0.1)
altura = st.number_input("Altura (m):", value=0.0, step=0.1)
delta_t = st.number_input("ΔT (°C):", value=0.0, step=0.1)

if st.button("Calcular Carga Térmica"):
    carga = area * altura * delta_t * 1.2
    toneladas = carga / 12000  # Conversión a toneladas de refrigeración
    resultado = f"Carga Térmica: {carga:.2f} BTU/h ({toneladas:.2f} TR)"
    st.success(resultado)
    st.session_state.historial.append(resultado)

st.markdown("---")

# =========================
# CÁLCULO DE CFM
# =========================
st.subheader("💨 Cálculo de CFM")
volumen = st.number_input("Volumen (m³):", value=0.0, step=0.1)
ach = st.number_input("Renovaciones por hora (ACH):", value=0.0, step=0.1)

if st.button("Calcular CFM"):
    cfm = (volumen * ach) / 60
    resultado = f"CFM: {cfm:.2f}"
    st.success(resultado)
    st.session_state.historial.append(resultado)

st.markdown("---")

# =========================
# HISTORIAL Y EXPORTACIÓN
# =========================
st.subheader("📜 Historial de Cálculos")
if st.session_state.historial:
    for i, item in enumerate(st.session_state.historial, start=1):
        st.write(f"{i}. {item}")

    if st.button("📄 Exportar a PDF"):
        archivo = exportar_pdf(st.session_state.historial)
        with open(archivo, "rb") as file:
            st.download_button("Descargar PDF", file, file_name=archivo, mime="application/pdf")
else:
    st.info("Aún no has realizado cálculos.")

# =========================
# PIE DE PÁGINA
# =========================
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray; font-size: 12px;'>
    🛠 Desarrollado para cálculos rápidos y precisos en campo HVAC
    </p>
""", unsafe_allow_html=True)
import streamlit as st

st.title("Sistema de Asistencia")

# 1. Lista de estudiantes
estudiantes = ["Ana", "Carlos", "Laura", "Miguel"]

# 2. Inicializar la memoria (asistencias y total de clases)
if "asistencia" not in st.session_state:
    st.session_state.asistencia = {est: [] for est in estudiantes}
if "total_clases" not in st.session_state:
    st.session_state.total_clases = 0

# 3. Mostrar cuántas clases se llevan registradas
st.write(f"📌 **Clases registradas hasta ahora:** {st.session_state.total_clases}")

# 4. Formulario con limpieza automática al enviar
with st.form("form_asistencia", clear_on_submit=True):
    st.subheader("Registrar Nueva Clase")
    
    asistencias_clase = {}
    for estudiante in estudiantes:
        opcion = st.radio(
            f"¿Asistió {estudiante}?", 
            ["Sí", "No"], 
            key=f"radio_{estudiante}", 
            horizontal=True
        )
        asistencias_clase[estudiante] = 1 if "Sí" in opcion else 0
        
    enviar = st.form_submit_button("Guardar esta clase", key="btn_guardar")

# 5. Procesar los datos al presionar guardar
if enviar:
    st.session_state.total_clases += 1  # Sumamos 1 al contador de clases
    for estudiante in estudiantes:
        st.session_state.asistencia[estudiante].append(asistencias_clase[estudiante])
    st.success("¡Clase guardada con éxito!")

# 6. Sección de resultados acumulados
st.markdown("---")
st.subheader("📊 Resultados Acumulados")

for estudiante in estudiantes:
    datos = st.session_state.asistencia[estudiante]
    asistencias = datos.count(1)
    faltas = datos.count(0)
    total = asistencias + faltas
    
    porcentaje = (asistencias / total * 100) if total > 0 else 0
    
    st.write(f"**{estudiante}** ➔ Asistencias: {asistencias} | Faltas: {faltas} | Porcentaje: {porcentaje:.1f}%")
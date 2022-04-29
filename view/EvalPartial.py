from model.EvalAnteproy import EvaluacionAnteproyecto
from reportlab.pdfgen import canvas

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def crear_pdf(evaluacion_obj):
    archivo = canvas.Canvas("Informacion_estudiante.pdf")
    archivo.drawString(100, 700, evaluacion_obj.id_estudiante)
    archivo.drawString(100, 750, evaluacion_obj.nombre)
    archivo.drawString(100, 800, evaluacion_obj.tema_proyecto)
    archivo.save()

def agregar_evaluacion(st, controller):
    # Objecto que modelará el formulario
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.nombre = st.text_input("Nombre estudiante")
    evaluacion_obj.id_estudiante = st.text_input("Id estudiante")
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    evaluacion_obj.tema_proyecto = st.text_input("Tema del proyecto")
    evaluacion_obj.version_doc = st.number_input("Version del documento")
    col1, col2 = st.columns(2)
    with col1:
        enviado_btn = st.button("Submit")
    with col2:
        creado_pdf = st.button("Descargar Datos PDF")

    # Cuando se oprime el boton se agrega a la lista
    if creado_pdf:
        crear_pdf(evaluacion_obj)
        st.success("El archvo se ha creado exitosamente")

    if enviado_btn:
        controller.agregar_evaluacion(evaluacion_obj)
        st.write("Evaluacion agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def listar_evaluacion(st, controller):
    """Itera los elementos de evaluacion agregados y los muestra"""
    st.title("Datos guardados:")
    for evaluacion in controller.evaluaciones:
        with st.container():
            st.write(evaluacion.id_estudiante)
            st.write(evaluacion.nombre)
            st.write(evaluacion.tema_proyecto)
            st.write(evaluacion.version_doc)

from model.EvalAnteproy import EvaluacionAnteproyecto


""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""

def crear_pdf(evaluacion_obj):
    """
    archivo = canvas.Canvas("Informacion_estudiante.pdf")
    text = archivo.beginText(50, h - 50)
    for dato in evaluacion_obj:
        text.textLine(dato)
    archivo.drawText(text)
    archivo.save()
    return archivo
    """
    pass

def agregar_evaluacion(st, controller):
    # Objecto que modelará el formulario
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.nombre = st.text_input("Nombre estudiante")
    evaluacion_obj.id_estudiante = st.text_input("Id estudiante")
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    evaluacion_obj.tema_proyecto = st.text_input("Tema del proyecto")
    evaluacion_obj.version_doc = st.number_input("Version del documento")
    enviado_btn = st.button("Submit")
    creado_pdf = st.dowloand_button(
     label="Download data as CSV",
     data=crear_pdf(evaluacion_obj),
     file_name='large_df.csv',
     mime='text/csv',
    )

    # Cuando se oprime el boton se agrega a la lista
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

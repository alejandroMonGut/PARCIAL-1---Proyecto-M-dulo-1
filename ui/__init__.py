from tabulate import tabulate

#solo admite bibliotecas
def impresion_datos_extraidos (results_df):

    lista_datos_requeridos = ["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado", "edad"]

    print(tabulate(results_df[lista_datos_requeridos], tablefmt="github", headers=["Número de registro", "Ciudad de ubicación","Departamento", "Edad", "Tipo", "Estado", "País de procedencia"]))
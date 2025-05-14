
# # # Presupuesto
# importar biblioteca de pdf
from fpdf import FPDF
# solicitud de ingreso de valores

proyecto = input("Digita el nombre del proyecto: ")

while True:
    try:
        horas_estimadas = int(input("Digita el número de horas estimadas: "))
        break
    except ValueError:
        print("Por favor, ingresa solo números para las horas.")
        
while True:
    try:
        valor_hora = int(input("Digita el valor de la hora: "))
        break
    except ValueError:
        print("Por favor, ingresa solo números para el valor de la hora.")

    
termino = input("Digita el término del proyecto: ")

# cálculo de valor de horas

valor_total = int(horas_estimadas) * int(valor_hora)

# armado pdf a generar. Se maneja por eje cartesiano para ubicar posición de los textos o imágenes a usar en el pdf generado

# primero se añade una pagina en blanco con add_page, luego se le asigna la fuente a usar con set_font

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12, style= "B")

# para añadir el template del ejemplo se debe asignar con 

pdf.image("Template.png", 0, 0)

# se añaden las variables con .text(coord x, coord y, variable)

pdf.text(115, 145, proyecto)
pdf.text(115, 160, str(horas_estimadas))
pdf.text(115, 175, str(valor_hora))
pdf.text(115, 190, termino)
pdf.text (115, 205, str(valor_total))

nombre_archivo = proyecto.replace(" ", "_") + ".pdf"
pdf.output(nombre_archivo)
print ("¡¡¡Presupuesto generado con Éxito!!!")



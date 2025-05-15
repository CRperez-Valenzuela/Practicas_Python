
# # Automatizador de Webscraping y Envío por Correo

# Librerías necesarias:
# - yfinance: obtención de datos financieros
# - matplotlib: gráficos
# - pyautogui: automatización de acciones del mouse/teclado
# - pyperclip: manejo del portapapeles
# - webbrowser: abrir sitios web
# 
# Instalación (ejecutar solo si no están instaladas):
# !pip install yfinance matplotlib pyautogui pyperclip


# ## 1. Obtención de datos del usuario y descarga de histórico desde Yahoo Finance

import yfinance as yf

ticker = input("Digite el código de la acción: ")
fecha_inicio = input("Digite la fecha de inicio (aaaa-mm-dd): ")
fecha_cierre = input("Digite la fecha de cierre (aaaa-mm-dd): ")

datos_yfinance = yf.Ticker(ticker)
datos_historicos = datos_yfinance.history(start=fecha_inicio, end=fecha_cierre)

# ## 2. Gráfico del cierre usando matplotlib

import matplotlib.pyplot as plt

cierre = datos_historicos.Close
cierre.plot(title=f"Cierre de {ticker}")
plt.xlabel("Fecha")
plt.ylabel("Precio de Cierre (USD)")
plt.grid(True)
plt.show()


# ## 3. Análisis estadístico simple

minima = round(cierre.min(), 2)
maxima = round(cierre.max(), 2)
promedio = round(cierre.mean(), 2)

# ## 4. Automatización de envío por correo con Gmail

# Usamos pyautogui para automatizar clicks y escritura
# IMPORTANTE: Las coordenadas dependen de la resolución de tu pantalla

import time
import pyautogui
import pyperclip
import webbrowser

# Tiempo para preparar el entorno
pyautogui.PAUSE = 3

# Datos del correo
destinatario = "theteachercirope@gmail.com"
asunto = "Proyecto de análisis 2025"
mensaje = f"""
Buen día,

A continuación se presenta el análisis de la acción {ticker} del periodo
solicitado: {fecha_inicio} a {fecha_cierre}:

Cotización máxima: USD {maxima}
Cotización mínima: USD {minima}
Valor medio: USD {promedio}

Saludos. 
"""

# Abrir Gmail
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(5)

# Coordenadas personalizadas (ajustar según pantalla)
COORD_REDACTAR = (87, 217)
COORD_ENVIAR = (1254, 1006)

# Redactar nuevo correo
pyautogui.click(*COORD_REDACTAR)

# Pegar destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")

# Asunto
pyautogui.hotkey("tab")
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")

# Cuerpo del mensaje
pyautogui.hotkey("tab")
pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")

# Enviar
pyautogui.click(*COORD_ENVIAR)

# Cerrar pestaña y confirmar envío
pyautogui.hotkey("ctrl", "w")
print("¡¡¡Mensaje enviado con éxito!!!")

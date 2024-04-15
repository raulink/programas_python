import pywhatkit

numero_telefono = "+59177703963"
mensaje = "https://docs.google.com/document/d/1QM4rvNJoQH_Y5cBP_BHwnRWjpvS_h7MvEEVm6yXlFgU/edit#heading=h.jnpw7tz7hbae"
fecha_hora = "2024-02-25 11:50"

pywhatkit.sendwhatmsg(numero_telefono, mensaje,11,52)


print("Mensaje enviado exitosamente!")

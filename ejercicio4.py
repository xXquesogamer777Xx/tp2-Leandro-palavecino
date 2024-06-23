
objeto = input("Describe el objeto encontrado: ").lower()


palabra_clav_tesoro = ["oro", "joya", "diamante", "antiguo", "reliquia"]

es_tesoro = any(palabra in objeto for palabra in palabra_clav_tesoro)

if es_tesoro:
    print("El objeto encontrado es un tesoro oculto.")
else:
    print("El objeto encontrado es solo un adorno decorativo.")


intermedio



mensaje = input("Ingrese el mensaje enigmático tallado en la estatua: ").lower()


palabras_clave_pista = ["tesoro", mapa", "guía", "clave", "encontrar"]

es_pista = any(palabra in mensaje for palabra in palabras_clave_pista)

if es_pista:
    print("El mensaje es una pista útil para encontrar el tesoro.")
else:
    print("El mensaje es una distracción peligrosa.")


difícil 



    {"pregunta": "Soy algo que siempre está delante de ti, pero no puedes ver. ¿Qué soy?", "respuesta": "el futuro"},
    {"pregunta": "Cuanto más me quitas, más grande me hago. ¿Qué soy?", "respuesta": "un agujero"},
    {"pregunta": "Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo agua, pero no peces. ¿Qué soy?", "respuesta": "un mapa"}
]


adivinanza = random.choice(adivinanzas)


print("Para abrir la puerta mágica, debes responder correctamente a la siguiente adivinanza:")
print(adivinanza["pregunta"])


respuesta_usuario = input("Tu respuesta: ").lower()


if respuesta_usuario == adivinanza["respuesta"]:
    print("¡Correcto! La puerta mágica se abre.")
else:
    print("Incorrecto. La puerta mágica permanece cerrada.")
🐱 AI Cat Detector - Discord Bot

🤖 Sobre el Bot

AI Cat Detector es un bot de Discord que analiza imágenes enviadas en un canal y determina si la imagen contiene:

Un gato generado por inteligencia artificial.

Un gato real.

Otra cosa que no es un gato.

Utiliza modelos de visión por computadora para hacer la clasificación y proporciona una respuesta clara basada en el análisis de la imagen.

🚀 Instalación

1️⃣ Clonar el repositorio

git clone https://github.com/tu-usuario/ai-cat-detector.git
cd ai-cat-detector

2️⃣ Instalar dependencias

Asegúrate de tener Python 3.8 o superior instalado.

pip install -r requirements.txt

3️⃣ Configurar variables de entorno

Crea un archivo .env con el siguiente contenido y reemplaza TU_TOKEN_DISCORD con tu token real:

DISCORD_TOKEN=TU_TOKEN_DISCORD

Si el bot usa una API externa para clasificar imágenes, agrega la clave de la API en este archivo también.

4️⃣ Ejecutar el bot

python bot.py

📌 Uso

Sube una imagen en un canal donde el bot esté presente.

El bot analizará la imagen y responderá con uno de los siguientes mensajes:

✅ "Este es un gato real. 🐱"

🤖 "Este parece ser un gato generado por IA."

❌ "Esto no es un gato. 🙃"

🛠️ Tecnologías utilizadas

Python 🐍

Discord.py 🤖

OpenCV y/o modelos de clasificación de imágenes 🖼️

API de detección de IA (opcional)

📜 Licencia

Este proyecto está bajo la licencia MIT. ¡Siéntete libre de contribuir y mejorarlo!

📩 Para sugerencias o mejoras, abre un issue o un pull request en el repositorio. 😺


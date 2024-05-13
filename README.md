# challenge-ai-engineer

Agregar un archivo .env con una key de la API de OpenAI

Ejecutar con devcontainer o con venv
```
uvicorn main:app --reload
```
O construir localmente
```
docker buildx build -t rag_image .
```
y ejecutar pasandole un .env
```
docker run --env-file .env --name rag_container -p 8080:8000 rag_image
```
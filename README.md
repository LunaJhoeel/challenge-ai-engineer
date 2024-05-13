# challenge-ai-engineer

Run in devcontainer and with an .env
```
uvicorn main:app --reload
```
Or build local image
```
docker buildx build -t rag_image .
```
and run local container
```
docker run --env-file .env --name rag_container -p 8080:8000 rag_image
```
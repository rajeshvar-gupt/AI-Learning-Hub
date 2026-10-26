FROM python:3.12-slim
WORKDIR /app
ENV OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
COPY requirements-ml.txt .
RUN python -m pip install --no-cache-dir -r requirements-ml.txt
COPY ai_hub ai_hub
RUN python -m ai_hub.iris_api train --model /app/outputs/iris/model.json
RUN useradd --create-home learner
USER learner
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health',timeout=3)"]
CMD ["python","-m","ai_hub.iris_api","serve","--host","0.0.0.0","--port","8000"]

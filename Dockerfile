FROM python:slim
ENV TOKEN=5942671360:AAEuUAtIt1i0IaMiMlOpzOuNyBWSgpzHVXk
COPY bot_new.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "bot_new.py"]

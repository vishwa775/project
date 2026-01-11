FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "student.py", "Vishwa", "BCA", "3", "85", "78", "92"]

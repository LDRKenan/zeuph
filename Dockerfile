# Python 3.9 tabanlı bir Docker imajı kullan
FROM python:3.9

# Çalışma dizinini belirle
WORKDIR /app

# Pip’i güncelle
RUN pip install --upgrade pip

# Gerekli bağımlılıkları yükle
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# API'yi başlat
CMD ["python", "main.py"]
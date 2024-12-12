# ZeroLingoMate - API

## Description

Zerolingomate is a translation app that translates text from **Portuguese (pt-BR)** to **English (en)** and then to **Korean (ko)**, and vice versa. This API uses  `deep-translator` library to perform translations and Flask framework for web server.

## Why?
The idea of implementing a chain translation system, instead of directly translating from Portuguese to Korean, comes from the fact that translations between these two languages often have flaws. Since English to Korean translation tends to be more accurate, English is used as an intermediary language, ensuring a more accurate and high-quality translation.

<sub>
it was also motivated by my frustration with having to switch between two different apps to translate everything during my studies. The goal is to simplify the process and make translations more efficient in one place. So it's for my personal use :shipit: also for studies.
</sub>


## Features


- Translates from **Portuguese (pt-BR)** to **English (en)**, then from **English (en)** to **Korean (ko)**.

<sub>more work in progress...</sub>

## Technologies Used

- **Flask**: Web framework for the backend.
- **deep-translator**: Library for translating text using various translation engines, such as Google Translator.


## How to Use

### Prerequisites

- **Python 3.x** installed on your machine.
- **Flask** and **deep-translator** installed in your Python environment.

### Installation

1. Clone the repository:

```
git clone https://github.com/MaduSilva/ZeroLingoMateBackend.git

cd ZeroLingoMateBackend
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Run the Flask application:

```
python app.py
```
The server will be running on port 8081 by default.

## Endpoints

### 1. **POST** `/translate`


**Request**
```
{
  "text": "Eu quero comer sushi"
}
```

**Response**

```
{
    "english_translation": "I want to eat sushi",
    "korean_translation": "나는 초밥을 먹고 싶다",
    "original": "Quero comer sushi"
}
```



**Generic BMI Template API (Django, Django REST Framework, PostgreSQL)**

## Overview

This API utilizes the robust Django framework and the versatile Django REST Framework to provide a well-structured and documented template for calculating Body Mass Index (BMI) and managing person data. It's meticulously designed to be adaptable to your specific requirements and integration needs, offering a solid foundation for further development.

**Prerequisites:**

- Python 3.6 or later ([https://www.python.org/downloads/](https://www.python.org/downloads/): [https://www.python.org/downloads/](https://www.python.org/downloads/))
- Django ([https://www.djangoproject.com/](https://www.djangoproject.com/): [https://www.djangoproject.com/](https://www.djangoproject.com/))
- Django REST Framework ([https://www.django-rest-framework.org/](https://www.django-rest-framework.org/): [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/))

**Dependencies:**

- You'll need to install the required dependencies in your virtual environment (`venv`):

  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install django djangorestframework
  ```

**Endpoints:**

| Path                       | HTTP Method | Description                                              |
|--------------------------|------------|-----------------------------------------------------------|
| `/admin/`                 | GET        | Access to Django admin site (requires authentication)    |
| `/healthcheck/`           | GET       | Returns a simple response to verify API health and uptime |
| `/person/`                | GET/POST        | Retrieves a list of persons with basic information / Create a person in Database      |
| `/person/<int:id>/`       | GET/PUT/DELETE       | Retrieves detailed information for a specific person by ID / Updates a person / Deletes a person |
| `/person/peso-ideal/<int:id>/` | GET        | Calculates and returns the ideal weight for a person by ID |

**Authentication:**

- The `/admin/` endpoint necessitates Django authentication and authorization for access.
- Other endpoints are currently public but could be secured with appropriate mechanisms as needed.

**Request and Response Formats:**

- Requests and responses adhere to the JSON (JavaScript Object Notation) format for clear and consistent data exchange.
- Dates and times should be sent in a standard format like ISO 8601 (e.g., `2024-02-10T00:32:00Z`) for global understandability.
- Request bodies must comply with the expected schema for each endpoint to ensure correct data interpretation.
- Response bodies will contain an HTTP status code and relevant data in JSON format for easy handling.

**Fields:**

| Field          | Type     | Description                                                                                   |
|----------------|----------|---------------------------------------------------------------------------------------------------|
| id              | integer  | Unique identifier for the person                                                                   |
| nome           | string   | Person's full name                                                                                |
| data_nasc      | date     | Person's date of birth                                                                              |
| cpf            | string   | Person's CPF (Cadastro de Pessoas Físicas) number (Brazil-specific)                                  |
| sexo           | string   | Person's gender (e.g., 'M', 'F')                                                               |
| altura         | float    | Person's height in meters                                                                           |
| peso           | float    | Person's weight in kilograms                                                                        |

**BMI Calculation:**

- The `/person/peso-ideal/<int:id>/` endpoint utilizes the standard BMI formula: `BMI = peso / (altura * altura)`.
- BMI provides a general indication of weight-for-height status, but it's not a definitive measure of health. Consult a healthcare professional for personalized guidance.

**Example Usage (Python):**

```python
import requests

# Ensure you're in the activated virtual environment

response = requests.get('http://localhost:8000/person/')
data = response.json()

print(data)  # Outputs a list of person objects

person_id = 123
response = requests.get(f'http://localhost:8000/person/{person_id}/')
data = response.json()

print(data)  # Outputs details of the person with ID 123

response = requests.get(f'http://localhost:8000/person/peso-ideal/{person_id}/')
data = response.json()

print(data)  # Outputs the calculated ideal weight for the person
```

**Additional Notes:**

- This template serves as a foundation, and you may need to customize it based on your specific requirements.

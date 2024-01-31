import os
from flask import Flask, jsonify

app = Flask(__name__)

sample_data = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "birthdate": "1980-01-01",
        "homeaddress": "123 Main Street",
        "country": "US",
        "work_email": "john.doe@example.com",
        "employee_id": "123456",
        "role": "Software Engineer"
    },
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "birthdate": "1985-02-02",
        "homeaddress": "456 Elm Street",
        "country": "US",
        "work_email": "jane.doe@example.com",
        "employee_id": "654321",
        "role": "Manager"
    },
    {
        "first_name": "Bob",
        "last_name": "Smith",
        "birthdate": "1990-03-03",
        "homeaddress": "789 Oak Street",
        "country": "UK",
        "work_email": "bob.smith@example.com",
        "employee_id": "987654",
        "role": "Intern"
    }
]

@app.route('/', methods=['GET'])
def get_employees():
    return jsonify(sample_data)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

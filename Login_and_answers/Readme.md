Run the command : 
1.  pip install -r req.txt
2.  python manage.py makemigrations 
3.  python manage.py migrate
4.  python manage.py runserver

There are two api endpoints.
1. http://127.0.0.1:8000/Registration/
    Get request returns all the data stored in the DB
    Post request in containing the data in the following format :
     {
        "Email": "abc@gmail.com",
        "First_Name": "aaaa",
        "Last_Name": "aaaa",
        "DOB": "2023-02-01",
        "Gender": "M",
        "password": "AaBC100330%"
    }
    Creates a user with the above credentials
2. http://127.0.0.1:8000/Submit_Answer/
    Get request returns all the data stored in the DB
    Post request in containing the data in the following format :
    {
        "submission_id": "aaa",
        "user_id": "aaaa",
        "question_id": "aaaaa",
        "option_choice": "B"
    }
    Stores the details of the answer.


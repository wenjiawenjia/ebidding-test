# README #

__Note:__ This project is created only for test purposes! Production behaviour and configuration will be different.

Tested on Ubuntu 16.04

### Installation ###

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* Python >= 3.4
* pip - https://pip.pypa.io/en/stable/
* virtualenv - https://virtualenv.pypa.io/en/stable/

Create and activate a new virtual environment:

```
    $ virtualenv venv
    $ source venv/bin/activate
```

Install the required packages

```
    $ pip install -r requirements.txt
```

Create the migrations for the application

```
    $ python jtc_rest_demo/manage.py migrate
```

### Running the application ###

For local testing, use the following command:

```
    $ python jtc_rest_demo/manage.py runserver
```

By default, it will listen at http://localhost:8000 (you can change this by adding <your_ip_address>:<your_port> argument to the command)

You can test the upload url API at:

```
http://localhost:8000/api/jtc/listings/<listing_id>/attachments/get-signed-url/
```

__Note:__ This will only return some mock-up data

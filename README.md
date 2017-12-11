# carpool
Application that helps you get a ride

## Prerequisites
     * Babel==2.5.1
     * confusable-homoglyphs==2.0.2
     * Django==1.11.7
     * django-bootstrap3==9.1.0
     * django-phonenumber-field==1.3.0
     * django-registration==2.3
     * olefile==0.44
     * phonenumberslite==8.8.7
     * Pillow==4.3.0
     * psycopg2==2.7.3.2
     * pytz==2017.3
  
 ## Installation

* `git clone <repository-url>` this repository
* `cd carpool` 
* 

## Project Specifications

    Features
     As a Driver, i should be able to:
        Create an account with carpool
        Create a Profile - vehicle info
        Login to carpool as a driver
        Create a travel plan
            * name
            * pickup points - Roads
            * current_location
            * destination endpoint
            * capacity available
            * pub_date
        Update a travel plan
        View travel plans
        Review a rider
       
     As a Rider, I should be able to:
        Create an account with carpool
        Create a Profile - Rider info
        Login to carpool as a rider
        View a map with pickup points
        Find Drivers Near Me
        Select a driver and view details of his current travel plan
        Create a travel request
            * name
            * pickup points - Desired Pickup Point
            * current_location
            * destination endpoint
            * capacity request
            * pub_date
        Update a travel request
        View travel history
        Review a driver
        
  
## Running / Development

python manage.py runserver

Running on http://127.0.0.1:8000/

## Hosting / Production

      ### requirements
            gunicorn==19.7.1
            python-decouple==3.1
            whitenoise==3.3.1
            dj-database-url==0.4.2


### Running Tests

      python3.6 manage.py test

## Technologies Used
       Python3.6
       django
       Postgres Database
       Bootstrap
       CSS
       HTML
       Google Maps API
       Javascript

    Deployment:
       Heroku


Copyright (c) 2017 Virginia Ndung'u      
        
        

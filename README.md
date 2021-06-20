
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# imdbproject

## Project setup
To get a local copy up and running follow these simple steps.

### Prerequisites

You must have python 3.0 or higher and pip installed


### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/Howsly/tommbo.git
   ```
2. Move to project folder
   ```sh
   cd imdbproject
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
4. Move to project manage.py (imdbproject/manage.py)
   Keep sqlite default setting for local database connection,
   comment out postgresql connection
5.Test project
   ```
   python manage.py test imdbapp
   ```
6. Run migrate
   ```
   python manage.py migrate
   ```
7. Create superuser
   ```
   python manage.py createsuperuser
   user:admin
   password:admin
   ```
8. Compile and run for local environment
   ```
   python manage.py runserver
   ```
9. For IMDB user, register imdb user through admin.
   It has read only rights.
   For example, on heroku server
   For normal user, who is not superuser, can only view data,
   and have access to only Get method
   ```
   https://imdb-demo-project.herokuapp.com/docs/
   user:imdb_user
   password:api@imdb21
   ```
   
10. Access this web app online
   ```
   Swagger Documentation:
   https://imdb-demo-project.herokuapp.com/docs
   Djano admin:
   https://imdb-demo-project.herokuapp.com/admin
   ```
11. Created a command load_initial_data to load
    information of movies from json file. 
    Through heroku CLI,use command load_initial_data.
    It will create movie table with genre information
   ```
   heroku run python manage.py load_initial_data
   ```
12. Movie data can be added manually through django admin or API 
    endpoints

## Authors

* **Vishal** - *Initial work*
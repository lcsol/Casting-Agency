# Casting Agency

Casting Agency is a website that allows agencies to view and manage the information of movies and actors in their company. 

Main function of the application:
1. Display detailed information of movies and acotrs.
2. Add new movies and acotrs.
3. Update the information of movies and actors.
4. Delete movies and actors.

There are three types of users with different permissions:
- Casting Assistant
    - Can view actors and movies
- Casting Director
    - All permissions a Casting Assistant has
    - Add or delete an actor from the database
    - Modify actors or movies
- Executive Producer
    - All permissions a Casting Director has
    - Add or delete a movie from the database

## Getting Started
* Base URL: The backend is hosted via Heroku. The base URL: is: https://casting-agency-cl.herokuapp.com/
* Authentication: Third-party authentication and roles-based access control (RBAC) are implemented through Auth0. 
Temporary JWT for three different users:
  * Casting Assistant: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2NzliYzFlMjcxZDBiZThjNmQ5NWEiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0NTI2NywiZXhwIjoxNTkxNjMxNjY3LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.oYu-BMojfhhJwgYX8LtUd2CYk37id6lSDY_9z1zTI84-z8AtBLo5nGEgEMrHDxxUco11gMKTSSvAewjihURxaaTkPyUgwAp2JpN8_2bCmwa1GDToByFbiypsYdaXfQYBWIYMadkVrLo4fyt5tXnSfoDK-r7BvVymSQ9NfP0qYVFBuRj-Rhu3_cbmCs2g3Py9Ot12cG1UWwDJrfy2garX_ayRlBsO4fg2_gGulJheCcZk0EB1WsAYUSY-JhccqiT3Ju0qLS2CgGDcO1eYG7Cl5sJtcVaYut66o_1hfTybL_7GJ4aQJZQZ3xVu015F3xwIlMaVUMFojp6KrE1JCHRODA
  * Casting Director: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E1NjFlMjcxZDBiZThjNmRiNjIiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0NTM4NywiZXhwIjoxNTkxNjMxNzg3LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.M8paX-EhvihbBLVZvbd7oJlSyrPZugBw_QYmkSYTwwZiWYEjeWRUmH_GcccQTD-WBVHAsqnLOHlecqmCAdYwm-Nm0m_uEQ23lflsYqE9BL_yY8XbPJ3ZYUC4hqsEDfA56hXo12ZTKSxObBxY_JDgxpnRTnaVu3pUVJaATZmxkbVamaMw24FJ2SL_q8pHpz9-qXbKgGI_HCaLtAfpCVizD1bJmduYWD1DvDa3O3lppCfoU7SZJpzC48AmFmNxQl_Ol6zpzEBmOPuRrXw5_FViXXYAyGAnJVFBP0XnVR_950xYJp4EixfvXQN09XnViC1SYpHCi-HynSTeEwLFEew87g
  * Executive Producer: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E4OGQ3MzBjOTBiZWZhYjE1YmQiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0MDk5OCwiZXhwIjoxNTkxNjI3Mzk4LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.UpkRQ9QoAIDUTcf0PrPUUPShZXUSi7zRr69snJn96dcErb8a_uetco6rHysfV0iiS2VIRVozXuTovU9CjQZ8VEQDf8AL-OlkwTkjRgleYh7FZ4GdMARoc4U12sNwsAW-RqreUiCzYJ_gum0zBf8qr6nGbkJzSrkKR7PNxj_HSHF48IvptOJ3uHnbSHsrL4pOk3dt9YEK5WuaDooqJq8_sZfD7GrWBmKbzNwalgwytl9-fgApOqV56jtZi0prXf0f-zbh7CSoDzOlieXcanUXgMbhBnLP9NGW_gRlo2JOL8x9Ccr6a7BGw2Q1VHzzdmLV1pHkVbZd8FdKS_cETR4_fg


## Local hosting
The backend app can be hosted locally at the default http://0.0.0.0:8080/.

### Backend
#### Installing Dependencies
##### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
##### Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
##### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:
``` pip install -r requirements.txt ```
This will install all of the required packages we selected within the ``` requirements.txt ```file.
###### Key Dependencies
- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM used to handle the lightweight sqlite database. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension used to handle cross origin requests from our frontend server. 
#### Database Setup
With Postgres running, restore a database using the agency_test.psql file provided. From the backend folder in terminal run:
```bash
dropdb casting_agency
createdb casting_agency
psql casting_agency < agency_test.psql
```

#### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
python app.py
```

## Error Handling
Errors are returned as JSON objects in the following format:

```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
AuthError Exception with a JSON object representing authentication errors and a status code is defined to hanlde authentication errors. It returned in the following format:
```
{
    'code': 'authorization_header_missing',
    'description': 'Authorization header is expected.'
}
```

The API will return the following error types when requests fail:
* 400: Bad Request
* 404: Resource Not Found
* 405: Method Not Allowed
* 422: Not Processable
* AuthErrors include 400, 401, 403

## API Endpoints
* ```<host>``` can be either local host http://0.0.0.0:8080 or https://casting-agency-cl.herokuapp.com
* Use the temporary JWT for Executive Producer
### GET /movies
* General
    - Fetches a list of all movie objects
    - Request Arguments: None.
    - Returns: a list of movies, success value, and total number of movies
* Sample
```bash 
curl <host>/movies -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E4OGQ3MzBjOTBiZWZhYjE1YmQiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0MDk5OCwiZXhwIjoxNTkxNjI3Mzk4LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.UpkRQ9QoAIDUTcf0PrPUUPShZXUSi7zRr69snJn96dcErb8a_uetco6rHysfV0iiS2VIRVozXuTovU9CjQZ8VEQDf8AL-OlkwTkjRgleYh7FZ4GdMARoc4U12sNwsAW-RqreUiCzYJ_gum0zBf8qr6nGbkJzSrkKR7PNxj_HSHF48IvptOJ3uHnbSHsrL4pOk3dt9YEK5WuaDooqJq8_sZfD7GrWBmKbzNwalgwytl9-fgApOqV56jtZi0prXf0f-zbh7CSoDzOlieXcanUXgMbhBnLP9NGW_gRlo2JOL8x9Ccr6a7BGw2Q1VHzzdmLV1pHkVbZd8FdKS_cETR4_fg'
```

```
{
  "movies": [
    {
      "id": 1, 
      "release_date": "Wed, 03 Jun 2020 11:28:45 GMT", 
      "title": "New movie test"
    }, 
    {
      "id": 2, 
      "release_date": "Mon, 10 Aug 2020 00:00:00 GMT", 
      "title": "movie_1"
    }, 
    {
      "id": 3, 
      "release_date": "Tue, 15 Sep 2020 00:00:00 GMT", 
      "title": "movie_2"
    }, 
    {
      "id": 4, 
      "release_date": "Sat, 25 Jul 2020 00:00:00 GMT", 
      "title": "movie_3"
    }, 
    {
      "id": 5, 
      "release_date": "Thu, 05 Nov 2020 00:00:00 GMT", 
      "title": "movie_4"
    }, 
    {
      "id": 6, 
      "release_date": "Wed, 30 Dec 2020 00:00:00 GMT", 
      "title": "movie_5"
    }
  ], 
  "success": true, 
  "total_movies": 6
}
```

### POST /movies
* General
    - Create a new movie
    - Request Arguments: title, release date.
    - Returns: the id of created movie, a list of paginated movies, and success value
* Smaple
```bash
curl http://0.0.0.0:8080/movies -X POST -H "Content-Type: application/json" -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E4OGQ3MzBjOTBiZWZhYjE1YmQiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0MDk5OCwiZXhwIjoxNTkxNjI3Mzk4LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.UpkRQ9QoAIDUTcf0PrPUUPShZXUSi7zRr69snJn96dcErb8a_uetco6rHysfV0iiS2VIRVozXuTovU9CjQZ8VEQDf8AL-OlkwTkjRgleYh7FZ4GdMARoc4U12sNwsAW-RqreUiCzYJ_gum0zBf8qr6nGbkJzSrkKR7PNxj_HSHF48IvptOJ3uHnbSHsrL4pOk3dt9YEK5WuaDooqJq8_sZfD7GrWBmKbzNwalgwytl9-fgApOqV56jtZi0prXf0f-zbh7CSoDzOlieXcanUXgMbhBnLP9NGW_gRlo2JOL8x9Ccr6a7BGw2Q1VHzzdmLV1pHkVbZd8FdKS_cETR4_fg' -d '{"title":"myMovie", "release_date":"5-20-2022"}'
```
```
{
  "created": 7, 
  "movies": [
    {
      "id": 1, 
      "release_date": "Wed, 03 Jun 2020 11:28:45 GMT", 
      "title": "New movie test"
    }, 
    {
      "id": 2, 
      "release_date": "Mon, 10 Aug 2020 00:00:00 GMT", 
      "title": "movie_1"
    }, 
    {
      "id": 3, 
      "release_date": "Tue, 15 Sep 2020 00:00:00 GMT", 
      "title": "movie_2"
    }, 
    {
      "id": 4, 
      "release_date": "Sat, 25 Jul 2020 00:00:00 GMT", 
      "title": "movie_3"
    }, 
    {
      "id": 5, 
      "release_date": "Thu, 05 Nov 2020 00:00:00 GMT", 
      "title": "movie_4"
    }, 
    {
      "id": 6, 
      "release_date": "Wed, 30 Dec 2020 00:00:00 GMT", 
      "title": "movie_5"
    }, 
    {
      "id": 7, 
      "release_date": "Fri, 20 May 2022 00:00:00 GMT", 
      "title": "myMovie"
    }
  ], 
  "success": true
}
```
### PATCH /movies/<int:movie_id>
* General
    - Update a specific movie
    - Request Arguments: movie id, title or release date.
    - Returns: the updated movie and the success value
* Smaple
```bash
curl http://0.0.0.0:8080/movies/1 -X PATCH -H "Content-Type: application/json" -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E4OGQ3MzBjOTBiZWZhYjE1YmQiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0MDk5OCwiZXhwIjoxNTkxNjI3Mzk4LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.UpkRQ9QoAIDUTcf0PrPUUPShZXUSi7zRr69snJn96dcErb8a_uetco6rHysfV0iiS2VIRVozXuTovU9CjQZ8VEQDf8AL-OlkwTkjRgleYh7FZ4GdMARoc4U12sNwsAW-RqreUiCzYJ_gum0zBf8qr6nGbkJzSrkKR7PNxj_HSHF48IvptOJ3uHnbSHsrL4pOk3dt9YEK5WuaDooqJq8_sZfD7GrWBmKbzNwalgwytl9-fgApOqV56jtZi0prXf0f-zbh7CSoDzOlieXcanUXgMbhBnLP9NGW_gRlo2JOL8x9Ccr6a7BGw2Q1VHzzdmLV1pHkVbZd8FdKS_cETR4_fg' -d '{"title":"updated movie"}'
```
```
{
  "movie": {
    "id": 1, 
    "release_date": "Wed, 03 Jun 2020 11:28:45 GMT", 
    "title": "updated movie"
  }, 
  "success": true
}
```
### DELETE /movies/<int:movie_id>
* General
    - Delete a movie
    - Request Arguments: movie id.
    - Returns: the id of deleted movie, a list of paginated movies, success value, and total number of existing movies
* Smaple
```bash
curl -X DELETE http://0.0.0.0:8080/movies/1 -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E4OGQ3MzBjOTBiZWZhYjE1YmQiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0MDk5OCwiZXhwIjoxNTkxNjI3Mzk4LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.UpkRQ9QoAIDUTcf0PrPUUPShZXUSi7zRr69snJn96dcErb8a_uetco6rHysfV0iiS2VIRVozXuTovU9CjQZ8VEQDf8AL-OlkwTkjRgleYh7FZ4GdMARoc4U12sNwsAW-RqreUiCzYJ_gum0zBf8qr6nGbkJzSrkKR7PNxj_HSHF48IvptOJ3uHnbSHsrL4pOk3dt9YEK5WuaDooqJq8_sZfD7GrWBmKbzNwalgwytl9-fgApOqV56jtZi0prXf0f-zbh7CSoDzOlieXcanUXgMbhBnLP9NGW_gRlo2JOL8x9Ccr6a7BGw2Q1VHzzdmLV1pHkVbZd8FdKS_cETR4_fg'
```
```
{
  "deleted": 1, 
  "movies": [
    {
      "id": 2, 
      "release_date": "Mon, 10 Aug 2020 00:00:00 GMT", 
      "title": "movie_1"
    }, 
    {
      "id": 3, 
      "release_date": "Tue, 15 Sep 2020 00:00:00 GMT", 
      "title": "movie_2"
    }, 
    {
      "id": 4, 
      "release_date": "Sat, 25 Jul 2020 00:00:00 GMT", 
      "title": "movie_3"
    }, 
    {
      "id": 5, 
      "release_date": "Thu, 05 Nov 2020 00:00:00 GMT", 
      "title": "movie_4"
    }, 
    {
      "id": 6, 
      "release_date": "Wed, 30 Dec 2020 00:00:00 GMT", 
      "title": "movie_5"
    }, 
    {
      "id": 7, 
      "release_date": "Fri, 20 May 2022 00:00:00 GMT", 
      "title": "myMovie"
    }
  ], 
  "success": true, 
  "total_movies": 6
}
```
### Endpoints for Actors
Endpoints for actors include GET /actors, POST /actors, PATCH /actors/actor_id, and  DELETE /actors/actor_id.
The general information and sample of these endpoints are similar with the movie endpoints above. 

## Testing
To run the tests, run
```bash
source setup.sh
dropdb agency_test
createdb agency_test
psql agency_test < agency_test.psql
python test_app.py
```

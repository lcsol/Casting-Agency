import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import create_app
from models import setup_db, Movie, Actor


class AgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'Test_movie',
            'release_date': '12-31-2020'
        }

        self.new_movie_2 = {
            'title': 'Test_movie_producer',
            'release_date': '12-31-2025'
        }

        self.new_actor = {
            'name': 'actor_test',
            'age': 20,
            'gender': 'Male'
        }

        self.ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2NzliYzFlMjcxZDBiZThjNmQ5NWEiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0NTI2NywiZXhwIjoxNTkxNjMxNjY3LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.oYu-BMojfhhJwgYX8LtUd2CYk37id6lSDY_9z1zTI84-z8AtBLo5nGEgEMrHDxxUco11gMKTSSvAewjihURxaaTkPyUgwAp2JpN8_2bCmwa1GDToByFbiypsYdaXfQYBWIYMadkVrLo4fyt5tXnSfoDK-r7BvVymSQ9NfP0qYVFBuRj-Rhu3_cbmCs2g3Py9Ot12cG1UWwDJrfy2garX_ayRlBsO4fg2_gGulJheCcZk0EB1WsAYUSY-JhccqiT3Ju0qLS2CgGDcO1eYG7Cl5sJtcVaYut66o_1hfTybL_7GJ4aQJZQZ3xVu015F3xwIlMaVUMFojp6KrE1JCHRODA'
        self.DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E1NjFlMjcxZDBiZThjNmRiNjIiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0NTM4NywiZXhwIjoxNTkxNjMxNzg3LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.M8paX-EhvihbBLVZvbd7oJlSyrPZugBw_QYmkSYTwwZiWYEjeWRUmH_GcccQTD-WBVHAsqnLOHlecqmCAdYwm-Nm0m_uEQ23lflsYqE9BL_yY8XbPJ3ZYUC4hqsEDfA56hXo12ZTKSxObBxY_JDgxpnRTnaVu3pUVJaATZmxkbVamaMw24FJ2SL_q8pHpz9-qXbKgGI_HCaLtAfpCVizD1bJmduYWD1DvDa3O3lppCfoU7SZJpzC48AmFmNxQl_Ol6zpzEBmOPuRrXw5_FViXXYAyGAnJVFBP0XnVR_950xYJp4EixfvXQN09XnViC1SYpHCi-HynSTeEwLFEew87g'
        self.PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E4OGQ3MzBjOTBiZWZhYjE1YmQiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTU0MDk5OCwiZXhwIjoxNTkxNjI3Mzk4LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.UpkRQ9QoAIDUTcf0PrPUUPShZXUSi7zRr69snJn96dcErb8a_uetco6rHysfV0iiS2VIRVozXuTovU9CjQZ8VEQDf8AL-OlkwTkjRgleYh7FZ4GdMARoc4U12sNwsAW-RqreUiCzYJ_gum0zBf8qr6nGbkJzSrkKR7PNxj_HSHF48IvptOJ3uHnbSHsrL4pOk3dt9YEK5WuaDooqJq8_sZfD7GrWBmKbzNwalgwytl9-fgApOqV56jtZi0prXf0f-zbh7CSoDzOlieXcanUXgMbhBnLP9NGW_gRlo2JOL8x9Ccr6a7BGw2Q1VHzzdmLV1pHkVbZd8FdKS_cETR4_fg'
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    '''
    ===============================================
    Tests for Movies
    ===============================================
    '''
    def test_get_movies(self):
        res = self.client().get('/movies',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_movies'])
    
    def test_400_get_movies_beyond_valid_page(self):
        res = self.client().get('/movies?page=1000',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')
    
    def test_create_movie(self):
        res = self.client().post('/movies',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['movies'])
    
    def test_405_create_movie_not_allowed(self):
        res = self.client().post('/movies/5',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')
    
    def test_422_create_movie_unprocessable_entity(self):
        res = self.client().post('/movies',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')

    def test_update_movie(self):
        res = self.client().patch('/movies/2',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json={'title': 'new_movie_update'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'], 'new_movie_update')
    
    def test_404_update_inexistent_movie(self):
        res = self.client().patch('/movies/1000',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json={'title': 'test'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
    
    def test_delete_movie(self):
        res = self.client().delete('/movies/1',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])
        self.assertEqual(movie, None)
    
    def test_422_delete_inexistent_movie(self):
        res = self.client().delete('/movies/1000',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')

    '''
    ===============================================
    Tests for Actors
    ===============================================
    '''
    def test_get_actors(self):
        res = self.client().get('/actors',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_actors'])
    
    def test_400_get_actors_beyond_valid_page(self):
        res = self.client().get('/actors?page=1000',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')
    
    def test_create_actor(self):
        res = self.client().post('/actors',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['actors'])
    
    def test_405_create_actor_not_allowed(self):
        res = self.client().post('/actors/5',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_update_actor(self):
        res = self.client().patch('/actors/2',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)}, 
            json={'name': 'new', 'age': 99})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], 'new')
        self.assertEqual(data['actor']['age'], 99)
    
    def test_404_update_inexistent_actor(self):
        res = self.client().patch('/actors/1000',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json={'name': 'test', 'age': 120})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
    
    def test_delete_actor(self):
        res = self.client().delete('/actors/5',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == 5).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 5)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])
        self.assertEqual(actor, None)
    
    def test_422_delete_inexistent_actor(self):
        res = self.client().delete('/actors/1000',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')
    
    '''
    ===============================================
    Tests of RBAC
    ===============================================
    '''
    def test_get_movies_assistant(self):
        res = self.client().get('/movies',
            headers={"Authorization": "Bearer {}".format(self.ASSISTANT_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_movies'])
    
    def test_403_create_movies_assistant(self):
        res = self.client().post('/movies',
            headers={"Authorization": "Bearer {}".format(self.ASSISTANT_TOKEN)},
            json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')
    
    def test_update_movie_director(self):
        res = self.client().patch('/movies/4',
            headers={"Authorization": "Bearer {}".format(self.DIRECTOR_TOKEN)},
            json={'title': 'new_movie_director'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'], 'new_movie_director')
    
    def test_403_delete_movies_director(self):
        res = self.client().delete('/movies/3',
            headers={"Authorization": "Bearer {}".format(self.DIRECTOR_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_create_movie_producer(self):
        res = self.client().post('/movies',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)},
            json=self.new_movie_2)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['movies'])
    
    def test_delete_movie_producer(self):
        res = self.client().delete('/movies/5',
            headers={"Authorization": "Bearer {}".format(self.PRODUCER_TOKEN)})
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == 5).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 5)
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])
        self.assertEqual(movie, None)    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
    
    
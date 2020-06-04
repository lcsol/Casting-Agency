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

        self.ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2NzliYzFlMjcxZDBiZThjNmQ5NWEiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTI4MjY5NiwiZXhwIjoxNTkxMzY5MDk2LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.Ndf0RNLiL41mS1xjt3t8K46RxSmmyfhqJXfAFhhh3SougIIo_IabU6k4GGM03Umrbm0hs_kOAPlKMdZ4IQaBd__Yti-WkMebPhSBtFEvrftjr5qLTUWYJs7dCEgNEgIbycE7LQ1OxifeaqENCHEzo44s7bGfLoUtIKI1Pjuh3ovm3JygT7CTXBAwsKfKMa5Pae2uXXkWlm4rirTTgHutJZ55GVVpFR83gjeGXbGRQCRbATP_tyWjR44OtVqliFdusBhoPbfMWzGFm1trBGwbtCID4fgsJNRP5s9DfalQLFGWjCkzl01GUH_PdcpuZ_qZWYKSc2G8nS2QvfW3H8MseA'
        self.DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E1NjFlMjcxZDBiZThjNmRiNjIiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTI4Mjc5NywiZXhwIjoxNTkxMzY5MTk3LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.bdhzlHfQuzPbN26o4bPo7nVESxG3DwlV2maOISYLZe5oJRq_REwxjStPxthLobs0O6INhbXGnlLu64zJMtCRR107pA9nWSzrxj0FjLJ5l09Q7W9uH5eLcZQh2VrRUUYaeYeR5neXI7XW7-d_28MMj5M5JGHA4uv8cOp_ql4gWxBUo9aSqyBFlawZdB8Cx9F81AN-HJmcgTMvhUGlyhmPRBQm2nhCdQniYaaU9jeBObIJD8b6TiszYGcgPh9_dMFECmvQpzoZfnGRxM4kQEViFPTsERVCGf4bsHyifu7G0N8RH5p9OSaSx4j-npwG3rU49p6BjGzd1RpEEmItyqu2Rw'
        self.PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhNM2NuSjEyNjFLSGJMaWppTk54eSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jbC1mc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2N2E4OGQ3MzBjOTBiZWZhYjE1YmQiLCJhdWQiOiJtb3ZpZV9hY3RvciIsImlhdCI6MTU5MTIzNzQyOSwiZXhwIjoxNTkxMzIzODI5LCJhenAiOiJHQW1FaHcyTEQycGU0TVpZSzlZMUhsRTJBU3N0NzhvQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Rn9minQt2VOO-xRuz9fMprfsiJLu2mXHzI8vxhlp3A8PTaF5t8bODLx9lWQ8NY4Vn8Ip5raVpMny_Is7kX0HA562hU2nFSZrmZqVREGwKDQ5NfXYwtG6bl9EVeNJWrqXbG1Z7O8iayKArtY6p_y-aZcTgHEf9U_gVy-P2IMHrrjJFcgbZPxaSh4-365o-SBqgyTJv_I73FRIMr6KPekyv4OECwgJnt7gzebh2b77zLnAO7Kduz4-HJ7kxyG1E-YCBlSDdILvQ94gl81tjHMkGrBbbgy41JXlb46n-EOSFDxJZoOQ6oozNwRH_s9BebbcHTzBsEW_I2LBuC_zym5PYg'
        
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
    
    
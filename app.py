import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import requires_auth, AuthError

MOVIES_PER_PAGE = 10

def paginate(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * MOVIES_PER_PAGE
    end = start + MOVIES_PER_PAGE
    movies = [movie.format() for movie in selection]
    # cur_movies = movies[start:end] if end < len(movies) else movies
    cur_movies = movies[start:end]
    return cur_movies


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    db = setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Contect-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    
    # ROUTES
    '''
    =============================================
    Movies
    =============================================
    '''
    # GET movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            selection = Movie.query.order_by(Movie.id).all()
            movies = paginate(request, selection)
            if len(movies) == 0:
                abort(404)
            return jsonify({
                'success': True,
                'movies': movies,
                'total_movies': len(selection)
            })
        except Exception:
            abort(400)
        finally:
            db.session.close()

    # Create new movies
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        try:
            body = request.get_json()
            new_title = body.get('title')
            new_release_date = body.get('release_date')
            movie = Movie(title=new_title, release_date=new_release_date)
            movie.insert()
            selection = Movie.query.order_by(Movie.id).all()
            cur_movies = paginate(request, selection)
            return jsonify({
                'success': True,
                'created': movie.id,
                'movies': cur_movies
            })
        except Exception as e:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()

    # Update movies
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)
        data = request.get_json()
        title = data.get('title')
        release_date = data.get('release_date')
        try:
            if title:
                movie.title = title
            if release_date:
                movie.release_date = release_date
            movie.update()
            return jsonify({
                'success': True,
                'movie': movie.format()
            })
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()
            

    # Delete movies
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        try:
            movie = Movie.query.get(movie_id)
            if not movie:
                abort(404)
            movie.delete()
            selection = Movie.query.order_by(Movie.id).all()
            cur_movies = paginate(request, selection)
            return jsonify({
                'success': True,
                'deleted': movie_id,
                'movies': cur_movies,
                'total_movies': len(selection)
            })
        except Exception as e:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()
    
    '''
    =============================================
    Actors
    =============================================
    '''
    # GET actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            selection = Actor.query.order_by(Actor.id).all()
            actors = paginate(request, selection)
            if len(actors) == 0:
                abort(404)
            return jsonify({
                'success': True,
                'actors': actors,
                'total_actors': len(selection),
            })
        except Exception:
            abort(400)
        finally:
            db.session.close()

    # Create new actors
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        body = request.get_json()
        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')
        if (not new_name) or (not new_age) or (not new_gender):
            abort(422)
        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            actor.insert()
            selection = Actor.query.order_by(Actor.id).all()
            cur_actors = paginate(request, selection)
            return jsonify({
                'success': True,
                'created': actor.id,
                'actors': cur_actors
            })
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()

    # Update actors
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        try:
            if name:
                actor.name = name
            if age:
                actor.age = age
            if gender:
                actor.gender = gender
            actor.update()
            return jsonify({
                'success': True,
                'actor': actor.format()
            })
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()
            

    # Delete actors
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        try:
            actor = Actor.query.get(actor_id)
            if not actor:
                abort(404)
            actor.delete()
            selection = Actor.query.order_by(Actor.id).all()
            cur_actors = paginate(request, selection)
            return jsonify({
                'success': True,
                'deleted': actor_id,
                'actors': cur_actors,
                'total_actors': len(selection)
            })
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()
    
    '''
    ==================================
    error handlers
    ==================================
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400
  
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404
  
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405
  
    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable entity'
        }), 422
    
    # error handler for AuthError
    @app.errorhandler(AuthError)
    def handle_auth_error(e):
        response = jsonify(e.error)
        response.status_code = e.status_code
        return response

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
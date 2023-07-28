from flask import request, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from config import app, db, api

from models.user import User


class Users( Resource ):
    def get( self ):
        return make_response( [ u.to_dict() for u in User.query.all() ] )

    def post( self ):
        data = request.json
        
        # HANDLING OUR VALIDATION IN THE MODEL:
        # try:
        #     user = User( name = data['name'], age = data['age'] )
        # except ValueError as v_error:
        #     return make_response( { 'error': str( v_error ) }, 422 )
        # except Exception as any_e:
        #     return make_response( 
        #         { 'error': str( any_e ) }, 422 )
        
        user = User( name = data['name'], age = data['age'] )

        db.session.add( user )
        try:
            db.session.commit()
        except IntegrityError as i_error:
            return make_response( { 'error': str( i_error ) }, 422 )

        return make_response( user.to_dict(), 201 )

api.add_resource( Users, '/users' )



if __name__ == '__main__':
    app.run( port = 5555, debug = True )


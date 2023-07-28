from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db

class User( db.Model, SerializerMixin ):
    __tablename__ = 'users'
    serialize_rules = ( '-created_at', '-updated_at' )

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )
    age = db.Column( db.Integer )

    created_at = db.Column( db.DateTime, server_default = db.func.now() )
    updated_at = db.Column( db.DateTime, onupdate = db.func.now() )

    __table_args__ = (
        db.CheckConstraint( 'age >= 18' ),
    )

    # VALIDATION THAT HAPPENS WHEN WE TRY TO CREATE AN INSTANCE
    # @validates( 'age' )
    # def check_age( self, key, age_given ):
    #     if age_given < 18:
    #         raise ValueError( 'Adults only please!' )
    #     return age_given

    

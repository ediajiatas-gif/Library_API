# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# from sqlalchemy import String, Date, Column, ForeignKey, Table
# from datetime import date
# from flask_marshmallow import Marshmallow #Importing Marshmallow class
# from marshmallow import ValidationError #importing Marshmallow class

# WHat is an ORM:
# ORM is a tool that allows us to use python objects instead of sql queries to talk to DB

# #Step 1
# app = Flask(__name__) #Instatiating our Flask app

# #Step 2
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' #Connecting a sqlite db to our flask app

# #Step 3: Create Base Class

# class Base(DeclarativeBase):
#   pass
#   # you could add your own configuration

# # Instantiate your SQLAlchemy database
# db = SQLAlchemy(model_class = Base)
# ma = Marshmallow() #made instance of both classes

# # Initialize my extension onto my Flask app
# db.init_app(app) #adding the db to the app
# ma.init_app(app)

# loan_books = Table(
#     'loan_books',
#     Base.metadata,
#     Column('loan_id', ForeignKey('loans.id')),
#     Column('book_id', ForeignKey('books.id'))
# )

# class Users(Base):
#   __tablename__ = 'users'

#   id: Mapped[int] = mapped_column(primary_key=True)
#   first_name: Mapped[str] = mapped_column(String(250), nullable=False)
#   last_name: Mapped[str] = mapped_column(String(250), nullable=False)
#   email: Mapped[str] = mapped_column(String(350), nullable=False, unique=True)
#   password: Mapped[str] = mapped_column(String(150), nullable=False)
#   DOB: Mapped[date] = mapped_column(Date, nullable=True)
#   address: Mapped[str] = mapped_column(String(500), nullable=True)
#   role: Mapped[str] = mapped_column(String(30), nullable=False)

#   loans: Mapped[list['Loans']] = relationship('Loans', back_populates='user')

# class Loans(Base):
#     __tablename__ = 'loans'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
#     loan_date: Mapped[date] = mapped_column(Date, nullable=True)
#     deadline: Mapped[date] = mapped_column(Date, nullable=True)
#     return_date: Mapped[date] = mapped_column(Date, nullable=True)

#     user: Mapped['Users'] = relationship('Users', back_populates='loans')
#     books: Mapped[list['Books']] = relationship("Books",secondary=loan_books, back_populates='loans')
   
# class Books(Base):
#     __tablename__ = 'books'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     genre: Mapped[str] = mapped_column(String(360), unique=True, nullable=False)
#     age_category: Mapped[str] = mapped_column(String(120), nullable=False)
#     publish_date: Mapped[date] = mapped_column(Date, nullable=True)
#     author: Mapped[str] = mapped_column(String(500), nullable=True)

#     loans: Mapped[list['Loans']] = relationship("Loans",secondary=loan_books, back_populates='books')

# class UserSchema(ma.SQLAlchemyAutoSchema):
#   class Meta:
#     model = Users #Creates a schema that validates the data as defined by our Users Model

# user_schema = UserSchema()

# @app.route('/users', methods=['POST']) #"listener" waits for a post request and will run functions when a post request is made
# def create_user():
#   try:
#     data = user_schema.load(request.json)#data we get back from the request
#   except: ValidationError
#   print(data)
#   return jsonify("Creating a user")
#   # 1) get my user data - responsibility for my client (frontend)
#   # 2) Create a User object from my user date
#   # 3) add User to session
#   # 4) commit to session
  
  

# with app.app_context():
#   db.create_all()
#   # creates all tables defined by our models in the context of the app's configuration and db

# app.run(debug=True) #makes sure we are in debug mode and auto refreshes 
# # Finally, we run our Flask app


# # Install Marshmallow (library / package)
# # pip instal flask_marshmallow, marshmallow_sqlalchemy 
# #schema = validate data, deserialize (json to python), serialize (python to json)

#flask limiter limits amount of requests
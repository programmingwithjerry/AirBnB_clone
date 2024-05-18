This team project is part of the ALX Full-Stack Software Engineer program. It's the initial step in creating a complete web application: an AirBnB clone. This first phase involves developing a custom command-line interface for data management and defining the base classes for data storage.

Step 1: Implement a Command Interpreter (Console)
The console is developed in Python3 and will perform CRUD operations (Create, Read, Update, Delete) on AirBnB objects such as User, City, Review, etc. Detailed information about the models will be provided in a later section.

Models:
Currently, there are 7 models: BaseModel, User, State, City, Amenity, Place, and Review. Each instance has the following attributes:

id: A unique identifier generated using the uuid package.
created_at: A datetime object representing the creation time of the object.
updated_at: A datetime object representing the last update time of the object.
__class__: A string indicating the object's type (model).
Additional attributes are assigned based on the model:

User

first_name: String
last_name: String
password: String
email: String
State

name: String
City

state_id: String
name: String
Amenity

name: String
Place

city_id: String
user_id: String
name: String
description: String
number_rooms: Integer
number_bathrooms: Integer
max_guest: Integer
price_by_night: Integer
latitude: Float
longitude: Float
amenity_ids: List
Review

place_id: String
user_id: String
text: String
Usage:
To start the console, run ./console from the root directory of the repository. The console supports the following commands:

create <class_name>: Create an object of the specified type. The ID of the newly created object will be printed.

update <class_name> <id> <attribute_name> <attribute_value>: Update the specified attribute of the object with the given ID.

destroy <class_name> <id>: Delete the object of the specified type with the given ID.

show <class_name> <id>: Display the object of the specified type with the given ID.

all [<class_name>]: Display all objects of the specified type. If no type is specified, display all objects.

help [<command>]: Show help information for the specified command. If no command is specified, display all documented commands.

import database as db

badges_values = ""
courses_values = ""
locations_values = ""
school_values = ""
comments_values = ""

# Create database and all tables
db.db_structure()

# Insert in the newly created tables
db.db_insert(badges_values, courses_values, locations_values,
             school_values, comments_values)

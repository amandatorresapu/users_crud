from mysqlconnection import connectToMySQL



class User:
    def __init__(self, data):
        self.id = data["id"]
        self.firt_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def make_user(cls,data):
        mysql = connectToMySQL("users_schema")
        query = "INSERT INTO users (first_name, last_name, email) Values (%(first_name)s, %(last_name)s, %(email)s);"
        return mysql.query_db(query, data)

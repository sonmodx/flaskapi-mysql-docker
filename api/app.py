
from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def ConnectorMysql():

    mydb = mysql.connector.connect(
            host=os.environ.get("DATABASE_HOST"),
            user="root",
            passwd="password",
            database="shop",
            port="3306"
    )
    return mydb

@app.route('/')
def index():
    return "Index!"

#get user by ID
@app.route("/getUser/<uid>", methods=["GET"] )
def getUser(uid):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    _id = uid
    sql = "SELECT * FROM Users WHERE uid='{}'; ".format(_id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return jsonify(myresult)
    
#get all users
@app.route("/getUsers", methods=["GET"] )
def getUsers():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Users; "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return jsonify(myresult)

#create user
@app.route("/createUser/<name>/<age>", methods=["POST"] )
def createUser(name,age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO Users VALUES (%s, %s, %s); "
    val = (None,name, age)
    mycursor.execute(sql,val)
    mydb.commit()

    return jsonify(f"Create user successfully")

#delete user
@app.route("/deleteUser/<uid>", methods=["DELETE"] )
def deleteUser(uid):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "DELETE FROM Users WHERE uid = {}".format(uid)

    mycursor.execute(sql)
    mydb.commit()

    return jsonify(f"Delete user with id:{uid} successfully")

#update user
@app.route("/updateUser/<uid>/<name>/<age>", methods=["PATCH"] )
def updateUser(uid,name,age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "UPDATE Users SET name = %s, age = %s WHERE uid = %s"
    val = (name,age,uid)

    mycursor.execute(sql,val)
    mydb.commit()

    return jsonify(f"Update user with id:{uid} successfully")

if __name__ == '__main__':
    app.run()
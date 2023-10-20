from flask_mail import Mail, Message
import firebase_admin
import mysql.connector
import uuid

def get_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pandusai@2003",
        database="Unfold23Law"
    )
    return db


def createuser(email, password, rol):
    db = get_db()
    cursor = db.cursor()
    Uuid=uuid.uuid1()
    cursor.execute("INSERT INTO users (email, pass, roleofuser,uuid) VALUES (%s, %s, %s,%s)", (email, password, rol,Uuid))
    db.commit()
    db.close()
    if cursor.rowcount > 0:
        return True
    else:
        return False


def checkuser(email, password, rol):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND pass = %s AND roleofuser = %s", (email, password, rol))
    result = cursor.fetchone()
    db.close()
    print(result)
    s=[result]
    if result!=None:
        return True
    else:
        return False
    
    
def getUser(email,password,rol):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND pass = %s AND roleofuser = %s", (email, password, rol))
    result = cursor.fetchone()
    db.close()
    print(result)
    s=[result]
    if result!=None:
        return [True,result[0],result[3]]
    else:
        return [False]
    
    


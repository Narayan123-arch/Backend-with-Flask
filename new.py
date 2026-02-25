from flask import Flask,request,jsonify
import psycopg2
app=Flask(__name__)

conn=psycopg2.connect(
dbname="second",
user="postgres",
password="naran07",
host="localhost",
port="5777"


)
cur=conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS suser(
id SERIAL PRIMARY KEY,
name VARCHAR(25),
email VARCHAR(25)

)
""")
conn.commit()
@app.route('/home',methods=["GET"])
def home():
    cur.execute("SELECT * FROM suser")
    row=cur.fetchall()
    users=[]
    for r in row:
      users.append({
         "id":r[0],
         "name":r[1],
         "email":r[2]
    })
    return jsonify({
      "status":"success",
      "count":len(users),
      "data":users
    })
   

@app.route("/add_user",methods=["POST"])
def add():
 data=request.get_json()
 name=data["name"]
 email=data["email"]
 cur.execute(
    "INSERT INTO suser (name,email) VALUES (%s,%s)",(name,email)
 )
 conn.commit()
 return "user successfully added"
if __name__=="__main__":
   app.run(debug=True)
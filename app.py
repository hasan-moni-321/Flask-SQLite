from flask import Flask, render_template, request 
import sqlite3 as sql  

app = Flask(__name__) 


@app.route('/')
def main_app(): 
    return render_template('student.html') 


@app.route('/result', methods=['POST', 'GET'])  
def student_info(): 
    if request.method == 'POST': 
        try:
            nm = request.form['name'] 
            addr = request.form['address']
            city = request.form['city'] 
            pin = request.form['pin'] 

            with sql.connect("database.db") as con: 
                cur = con.cursor()  
                cur.execute("INSERT INTO student_information (name, address, city, pin) VALUES (?, ?, ?, ?)", (nm, addr, city, pin)) 

                con.commit() 
                msg = "Record successfully added" 
        except: 
            con.rollback() 
            msg = 'error in insert operation' 

        finally: 
            return render_template('result.html', msg = msg)  
            con.close() 

if __name__ == "__main__": 
    app.run(debug=True) 


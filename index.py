
import requests,os,re

from flask import Flask,render_template,redirect,url_for,request
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder='template')

@app.route('/')
def lhue():
    return render_template('/index.html')

@app.route('/style')
def style():
    return render_template('/style.html')

@app.route('/design')
def design():
    return render_template('/design.html')

@app.route('/food')
def food():
    return render_template('/food.html')

@app.route('/music')
def music():
    return render_template('/music.html')

# @app.route('/people')
# def people():
#     return render_template('/people.html')




@app.route('/people')
def people():
        path = 'static/uploads/'
        uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))        # Sorting as per image upload date and time
        print(uploads)
        #uploads = os.listdir('static/uploads')
        uploads = ['uploads/' + file for file in uploads]
        uploads.reverse()
        return render_template("people.html",uploads=uploads)            # Pass filenames to front end for display in 'uploads' variable

app.config['UPLOAD_PATH'] = 'static/uploads'             # Storage path    
@app.route("/upload",methods=['GET','POST'])
def upload_file():                                       # This method is used to upload files 
        if request.method == 'POST':
                f = request.files['file']
                print(f.filename)
                #f.save(secure_filename(f.filename))
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
 
                return redirect("/people")           # Redirect to route '/' for displaying images on fromt end

@app.route('/people', methods=['POST'])
def my_form():
    text = request.form['u']
    processed_text = text.upper()

    print(processed_text)

@app.route('/sports')
def sports():
    return render_template('/sports.html')

@app.route('/technology') 
def technology():
    return render_template('/technology.html')

@app.route('/travel')
def travel():
    return render_template('/travel.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

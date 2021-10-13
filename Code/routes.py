from flask import Flask, render_template, redirect, url_for, request, make_response, session
from models import *

types = None


app = Flask(__name__)
app.secret_key = 'akashsreedevvishnu'

# two decorators, same function
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')



@app.route('/test')
def test():
    return render_template('test.html')



@app.route('/samples1')
def sample_select_1():

    session['path'] = None
    path="static\\images\\L1.jpeg"
    session["path"] = path
    return render_template('test.html')

@app.route('/samples2')
def sample_select_2():

    session['path'] = None
    path="static\\images\\L2.jpeg"
    session["path"] = path
    return render_template('test.html')

@app.route('/samples3')
def sample_select_3():

    session['path'] = None
    path="static\\images\\B1.jpeg"
    session["path"] = path
    return render_template('test.html')

@app.route('/samples4')
def sample_select_4():
    
    session['path'] = None
    path="static\\images\\S1.jpg"
    session["path"] = path

    return render_template('test.html')


@app.route("/upload-image", methods=['POST', 'GET'])
def upload_image():

    if request.method == "POST":
        if request.files:
            image = request.files["image"] 
            session['path'] = None
            #session['pathinc'] = None
            try:
              session.get('pathinc')
            except NameError:
              session['pathinc']=None

            while True:
                if session['pathinc'] == None:
                    session['pathinc'] = 0
                
                path  = "static/uploads/Test_img"+str(session.get('pathinc'))+".jpg"
                image = image.save(path)
                session["path"] = path
                session['pathinc'] = session.get('pathinc') + 1

                break

            print("Image Saved")
            return redirect(request.url)

    return render_template("test.html")




@app.route('/models', methods=['GET', 'POST'])
def dl_models():
    if request.method == "POST":

        types = request.form.get("cancertype")
        session['model']=types
        
        if types=="noselect":
            return render_template("test.html", types = "*Please select a valid model before you proceed")
        elif types=="sc":
            return render_template("test.html", types = "You have selected: Model for skin cancer")
        elif types=="bc":
            return render_template("test.html", types = "You have selected: Model for brain cancer")
        elif types=="combined":
            return render_template("test.html", types = "You have selected: Combined model for skin and brain cancer")
        else:
            return render_template("test.html", types = "You have selected: Generalized model to detect any type of cancer")

    return render_template("test.html")


@app.route('/result')
def result():

    path = session.get('path')
    model = session.get('model', None)

    if model =="noselect" or model == None:
        return render_template('test.html', types = "*Please select a valid model before you proceed")
    elif model=="sc":
        result= skin_cancer_model(path)
        if result=="Yes":
            return render_template("result.html", result = "Yes", area = "Skin", accuracy = str(86)+"%")
        else:
            return render_template("result.html", result = "No", area = "No", accuracy = str(86)+"%")
    elif model=="bc":
        result = brain_cancer_model(path)
        if result=="Yes":
            return render_template("result.html", result = "Yes", area = "Brain", accuracy = str(86)+"%")
        else:
            return render_template("result.html", result = "No", area = "No", accuracy = str(86)+"%")
    elif model=="combined":
        result = combined_cancer_model(path)
        if result in ["Brain",'Lung',"Skin"]:
            return render_template("result.html", result = "Yes", area = result, accuracy = str(86)+"%")
        else:
            return render_template("result.html", result = "No", area = "No", accuracy = str(86)+"%")
    else:
        result = gen_cancer_model(path)
        return render_template("result.html", result =result ,area = "NA", accuracy = str(82)+"%")




if __name__ == '__main__':
    app.run(debug=True)

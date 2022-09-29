
from flask import Flask, redirect, url_for ,render_template,request
import requests
import requests
from bs4 import BeautifulSoup
from flask import send_file
import os

import shutil

app = Flask(__name__)


@app.route("/",methods=["GET", "POST"])
def create():
    if request.method == "POST":
        url=request.form.get("url")
        if not(url[:23] == "https://3asq.org/manga/"):
            return("invalid chapter link")
        r = requests.get(url)
        if os.path.exists(os.path.abspath(os.path.join(os.getcwd(),"static/manga",""))):
            shutil.rmtree(os.path.abspath(os.path.join(os.getcwd(),"static/manga","")))
        if os.path.exists(os.path.abspath(os.path.join(os.getcwd(),"static/manga","chapter.zip"))):
            os.remove(os.path.abspath(os.path.join(os.getcwd(),"static/manga","chapter.zip")))
        os.mkdir(os.path.abspath(os.path.join(os.getcwd(),"static/manga","")))
        os.chdir(os.path.abspath(os.path.join(os.getcwd(),"static/manga","")))
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        
        for image in images:
            name = image['id']
            link = image['src']
            with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                
                print('Writing: ', name)
        os.chdir(os.path.abspath(os.path.join(os.getcwd(),"..")))
        shutil.make_archive("chapter", 'zip', os.path.abspath(os.path.join(os.getcwd(),"manga","")))
        

                

            
        
        return redirect(url_for('downloadFile'))
        
    else:
        return render_template('index.html')



@app.route('/download')
def downloadFile():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = os.path.abspath(os.path.join(os.getcwd(),"chapter.zip"))
    return send_file(path, as_attachment=True)
if __name__ == '__main__':
    app.run(port=5000,debug=True) 




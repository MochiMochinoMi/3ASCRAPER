from flask import Flask, redirect, url_for ,render_template,request,session
import requests
import requests
from bs4 import BeautifulSoup
from flask import send_file
import os
import shutil

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/",methods=["GET", "POST"])
def create():
    if request.method == "POST":
        url=request.form.get("search")
        if url[:23] == "https://3asq.org/manga/":
            r = requests.get(url)
            if os.path.exists(os.path.abspath(os.path.join(os.getcwd(),"Manga",""))):
                shutil.rmtree(os.path.abspath(os.path.join(os.getcwd(),"Manga","")),ignore_errors=True)
            if os.path.exists(os.path.abspath(os.path.join(os.getcwd(),"chap",""))):
                shutil.rmtree(os.path.abspath(os.path.join(os.getcwd(),"chap","")))
            os.mkdir(os.path.abspath(os.path.join(os.getcwd(),"Manga","")))
            os.chdir(os.path.abspath(os.path.join(os.getcwd(),"Manga","")))
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
            os.mkdir(os.path.abspath(os.path.join(os.getcwd(),"chap","")))
            namee = soup.find('h1')
            namee=namee.get_text()
            namee=namee.replace(' ', '_')
            session['my_var'] = namee
            name=session['my_var']
            shutil.make_archive("chap/"+name, 'zip', os.path.abspath(os.path.join(os.getcwd(),"Manga","")))                        
            return redirect(url_for('downloadFile'))
        elif url[:30] == "https://tcbscans.com/chapters/":
            r = requests.get(url)
            if os.path.exists(os.path.abspath(os.path.join(os.getcwd(),"static/manga",""))):
                shutil.rmtree(os.path.abspath(os.path.join(os.getcwd(),"static/manga","")))
            if os.path.exists(os.path.abspath(os.path.join(os.getcwd(),"chapter.zip"))):
                os.remove(os.path.abspath(os.path.join(os.getcwd(),"chapter.zip")))
            if os.path.exists(os.path.abspath(os.path.join(os.getcwd(),"chap",""))):
                shutil.rmtree(os.path.abspath(os.path.join(os.getcwd(),"chap","")))
            os.mkdir(os.path.abspath(os.path.join(os.getcwd(),"static/manga","")))
            os.chdir(os.path.abspath(os.path.join(os.getcwd(),"static/manga","")))
            soup = BeautifulSoup(r.text, 'html.parser')
            images = soup.find_all('img')
            
            for image in images[1:]:
                name = image['alt']
                link = image['src']
                with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
                    im = requests.get(link)
                    f.write(im.content)
                    
                    print('Writing: ', name)
            os.chdir(os.path.abspath(os.path.join(os.getcwd(),"..")))
            os.chdir(os.path.abspath(os.path.join(os.getcwd(),"..")))
            os.mkdir(os.path.abspath(os.path.join(os.getcwd(),"chap","")))
            namee = soup.find('h1')
            namee=namee.get_text()
            namee=namee.replace(' ', '_')
            session['my_var'] = namee
            name=session['my_var']
            
            shutil.make_archive("chap/"+name, 'zip', os.path.abspath(os.path.join(os.getcwd(),"static/manga","")))                            
            return redirect(url_for('downloadFile'))
        
        
        else:
            return("invalid chapter link")    
         
    else:
        return render_template('index.html')



@app.route('/download')
def downloadFile():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    name = session.get('my_var', None)
    path = os.path.abspath(os.path.join(os.getcwd(),"chap/"+name+".zip"))
    return send_file(path, as_attachment=True)
if __name__ == '__main__':
    app.run(port=5000,debug=True) 


#manga.scraper
#### Video Demo:  <URL HERE>
## Description:
### The idea?
Honestly i got the idea because i needed to solve a problem that i had, in my dorm room i barley have wifi signal or mobile network and i couldnt read my favorite mangas
due to this problem ,also even if i do have internet the sites that offer these scans are laggy and filled with ads so i created this manga scraping webapp to fix this problem.
### How it works?
Essentially you just go to a site (manga scans site) copy the link paste it in the webscraper and it returns a zip file with the chapter pages in it, its that simple.
### explaining the code?
#### app.py
So as you can tell this is a one page web app and the only input im taking is the chapter link through a post request once i get it i check if its a site that is supported 
by the app if not then it will let you know otherwise it will use the requests library to get the html page and parse it using BeautifulSoup then go through the img tags in the page 
now what might be confusing is all the os path lines those had to be written so i can deploy the app and it can run not only locally but online,explaining briefly first i check
if file called manga exists if it does then its from a prvious use of the app and it needs to be removed same with chapter.zip then i go ahead and create a new manga file and a chap file and 
put all the scraped images in the manga file then i get the name of the chapter from the scraped html to use it for the zip file that im gonna make with shutil.make_archive after this 
i redirect to the route /download that uses send_file to return a download prompt to the user.
#### templates
the index html is a simple one page html with a form to get the link nothing special paired with css for a dynamic search bar and background photo from my fav manga.
#### venv
Is something i learned for this project and is a must to have in any future project.
#### procfile & requirements
I needed to create these so i can deploy the app to heroku.

## What i learned 
the main things that i learned in this project are these:
-dynmaic paths how to work with them how to know where you are and how to maniuplate paths.
-requests and BeautifulSoup all about scraping and accessing tags and getting what i want from them.
-how to return a file (how to let the user download).

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import requests

home_page = Blueprint ('home_page', __name__, template_folder='/templates')

@home_page.route ('/', methods = ['GET'])
@login_required
def news ():
    api_key = "cc3747f4309f44bb9cc0c5d2bbd336df"
    url = f"https://newsapi.org/v2/everything?q=scam&apiKey={api_key}"
    response = requests.get (url)

    count = 0
    article_title = []
    article_description = []
    article_url = []
    img_url = []

    data = response.json ()
    for key, value in data.items ():
        if key == "articles":
            for article in value:
                if article ["title"] != "[Removed]" and article["url"] != "None" and article["urlToImage"] is not None and len (article["description"]) > 100:
                    article_title.append (article ["title"])
                    article_description.append (article ["description"])
                    article_url.append (article ["url"])
                    img_url.append (article ["urlToImage"])
                    
                    count += 1 

                    if count == 6:
                        break

    return render_template ("home.html", user=current_user, title=article_title, description=article_description, url=article_url, img=img_url)
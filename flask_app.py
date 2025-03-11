from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', heading="Welcome to My Flask App")

@app.route("/home")
def home_page():
    return render_template("home.html", heading="Welcome to My Flask App")

# route for the about page
@app.route("/about")
def about():
        first_name = "Elena"
        second_name = "Mijares"
        role = "Data Science Student"
        skills = ["Python", "Flask", "Github/Git", "R", "Research Methods"]
        interests = ["Gender and Politics", "Political sociology", "Social Policy", "Data Science", "Machine Learning"]
        education = "Social Science / Data Science for Public Policy"
        image_url = "/static/image/Profilepic.png"  # Note the /static prefix
        return render_template('about.html', 
                               first_name=first_name,
                               second_name=second_name,
                                role=role,
                                skills=skills,
                                interests=interests,
                                education=education,
                                image_url=image_url)
    
if __name__ == '__main__':
    app.run(debug=True)
from app import app, db
from flask import render_template, redirect, url_for, flash
# Import the SingUpForm and LoginForm class from forms
# from app.forms import SignUpForm, LoginForm
# Import the User model from models
# from app.models import User

# Create our first route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topfive')
def topfive():
    top_five_img = ["ship1.jpg", "ship2.png", "ship3.jpg", "ship4.jpg", "ship5.png"]
    topfive= {"Anvil Hurricane":["Heavy Fighter - 2 seater, great fun with a friend. It's small and agile but can take down massive targets in seconds with its 4 size 3 guns on its manned turret. The design of the ship inside and out is sleek and beautiful, the deep whir of the engines in the cockpit keeps me coming back. One of my favorite ship designs of all time.","ship1.jpg"], "Drake Caterpillar: Pirate Edition":['Heavy Freight - My daily driver. This massive cargo hauler is just fun to fly, it\'s slow and lumbering but it\'s incredibly tanky and can shrug off a full assault from a group of light fighters. Its large carrying capacity makes it suitable for cargo hauling for big profits and its unique landing gear legs makes landing on uneven terrain easy. The special edition livery gives it an "outlaw" style makeover in all black with red accents.','ship2.png'],'Aegis Redeemer':['Heavy Gunship - My preferred multicrew ship when taking friends on a trip to take down a large number of targets. You can easily take down a group of players with the massive size 5 guns on the two manned turrets. Capable of utilizing full ballistics to deliver jaw-dropping amounts of damage to anything that moves.', 'ship3.jpeg'], 'Drake Corsair':['Exploration Vessel - The roadtrip machine. This beautiful ship can take you and three of your friends anywhere in the system in style with tons and tons of guns to boot. The array of size 3 missiles is enough to knock out medium size targets and the pilot\'s 4 size 5 hardpoints can take down capital class ships in seconds. The main event of this ship is its folding wings and unique co-pilot cockpit design.', 'ship4.jpg'],"Anvil Liberator":['Medium Carrier - Currently in concept, not flyable yet. The most anticipated ship for me, it\'s the gateway to other carrier ships like the Drake Kraken which is years away from completion. The Liberator is the perfect solution for me because my team of friends is only 2-4, the Liberator can be the team\'s carrier for each of their ships across any system in the galaxy.','ship5.png']}
    return render_template('topfive.html', topfive=topfive)



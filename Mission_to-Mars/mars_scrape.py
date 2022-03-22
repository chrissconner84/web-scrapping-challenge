#12 Web Scrapping
# # import necessary libraries
from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import mars_facts, marshemispheres, mission_to_mars, mars_space_images

# create instance of Flask app
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client["mars_scrape_db"]
# Drops collection if available to remove duplicates
db.marsdata.drop()
#Declare collection
mdata=db.marsdata
  

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():


    # Run the Mission to Mars scrape function
         
     mars_headlines=mission_to_mars.mission_to_mars()

    # Insert the record
     #mdata.insert_one(mars_headlines) 

    # # Run the Mars facts scrape function
     mars_data = mars_facts.mars_facts()
    #     # Insert the record
     mfs={}
     mfs["html_table"]=mars_data
     mars_headlines.update(mfs)

     #mdata.insert_one(mfs)
    
    # # Run the Mars space image function
     mars_image = mars_space_images.mars_space_image()
     mars_headlines.update(mars_image)
    # # Insert the record
     #mdata.insert_one(mars_image)

    # # Run the Mars hemispheres function
     mars_hemisheres = marshemispheres.marshemisphere()

    # # Insert the record
     #mdata.insert_many(mars_hemisheres)
     mars_headlines.update(mars_hemisheres)   
     mdata.insert_one(mars_headlines)
     #Redirect back to home page
     return redirect("/")
# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    all_mdata = mdata.find_one()
    
    # Return the template with the teams list passed in
    return render_template("index.html", data=all_mdata)

if __name__ == "__main__":
    app.run(debug=True)

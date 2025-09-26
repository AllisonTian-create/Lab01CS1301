#This File will contain the information to be displayed in your portfolio

#CHANGE BELOW
import os

# get current directory of this file (info.py)
BASE_DIR = os.path.dirname(__file__)

profile_picture = os.path.join(BASE_DIR, "Images", "profile.jpeg")
bobby = os.path.join(BASE_DIR, "Images", "BobRoss.jpg")
Bob = os.path.join(BASE_DIR, "Images", "Bob.jpg")
Happy = os.path.join(BASE_DIR, "Images", "Happy.jpg")
dissapointed = os.path.join(BASE_DIR, "Images", "dissapointed.jpeg")
catSpinning = os.path.join(BASE_DIR, "Images", "cat-spinning.gif")

#profile_picture = "Images/profile.jpeg"
#bobby = "Images/BobRoss.jpg"
#Bob = "Images/Bob.jpg"
#Happy = "Images/Happy.jpg"
#dissapointed = "Images/dissapointed.jpeg"
#about_me = "I'm Allison Tian. I'm a first year EE major at Georgia Tech and my computer science skills are dubious. "
#catSpinning = "Images/cat-spinning.GIF"


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/allison-tian"
my_github_url = "https://github.gatech.edu/atian39"
my_email_address = "allisontian18@gmail.com"


education_data ={
    'Degree': 'Bachelor of Engineering in Electrical Engineering',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'At some point',
    'GPA': 'Non-existent'
}

course_data = {
    "code":["CS 1301", "MATH 1551", "MATH 1554", "GT 1000", "CHEM 1310"], 
    "names":["Intro to CS", "Differential Calculus", "Linear Algebra", "Freshman Seminar","Gen Chem for Engineers"], 
    "semester_taken":["1st", "1st", "1st", "1st","1st"],
    "skills":["I know less about Python than I thought I did", "I should have tested out...", "Basically row reduction", "Why did I take this class", "Why am I getting cooked"],
    }
experience_data = {
    "Cashier at Hunam Chinese Restaurant": (["- Packed online orders",
                                                                          "- Served customers", "- Cut the tips off of green beans"],"WebDevLab01/Images/Hunam.jpg"),
    "ArtsCamp Counselor":(["- Taught crochet class",
                                                           "- Repaired sewing machines and helped teach sewing"],"WebDevLab01/Images/crochet.jpg")

}

projects_data = {
    "Campus Pollinator Garden": "Helped design and grow pollinator garden at my highschool",
}

programming_data = {
    "Python": 60,
    "Java": 20,
    "html": 15,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "html": ":(",
}
spoken_icons = {"Chinese":"",
    "English":"",
    "Spanish":""
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
    "Chinese": "Fluent but can't write",
    "Spanish": "Ok",
}
leadership_data = {
    "Gardening Club President": (["- Gardened and stuff"],"WebDevLab01/Images/dog-farmer.png"),

}
activity_data={
    "Crochet Club": ["Held crochet sales for charity/good causes", 
            "Taught people to crochet"]
}

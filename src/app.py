"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}

# Additional activities
activities.update({
    "Drama Club": {
        "description": "Acting workshops and school plays",
        "schedule": "Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["ava@mergington.edu"]
    },
    "Robotics Team": {
        "description": "Build and program robots for competitions",
        "schedule": "Tuesdays and Thursdays, 5:00 PM - 7:00 PM",
        "max_participants": 18,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Art Club": {
        "description": "Drawing, painting, and mixed-media projects",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["isabella@mergington.edu"]
    },
    "Debate Team": {
        "description": "Competitive debate practice and tournaments",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["oliver@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "Hands-on science and engineering challenges",
        "schedule": "Thursdays, 4:30 PM - 6:30 PM",
        "max_participants": 24,
        "participants": ["sophia@mergington.edu"]
    },
    "Math Club": {
        "description": "Problem solving and math contests",
        "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
        "max_participants": 30,
        "participants": ["ethan@mergington.edu"]
    },
    "Photography Club": {
        "description": "Photo walks, editing, and exhibits",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 20,
        "participants": ["mia@mergington.edu"]
    },
    "Volunteer Squad": {
        "description": "Community service projects and outreach",
        "schedule": "Varies (weekend events)",
        "max_participants": 40,
        "participants": ["jack@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Instrumental and vocal rehearsals",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 35,
        "participants": ["amelia@mergington.edu"]
    },
    "Environmental Club": {
        "description": "Sustainability projects and campus cleanups",
        "schedule": "Fridays, 2:30 PM - 4:00 PM",
        "max_participants": 30,
        "participants": ["lucas@mergington.edu"]
    }
})


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

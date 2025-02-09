# Medicine Reminder 


## Basic Details
### Team Name: Hacktivate


### Team Members
- Member 1: Fathima Mehar P S - SCMS School of Engineering and Technology
- Member 2: Fidha V S - SCMS School of Engineering and Technology


### Hosted Project Link
https://medicine-reminder-kk6i.onrender.com/

### Project Description
The Digital Medicine Reminder is a simple yet effective application that helps users manage their medication schedules. It ensures users never miss a dose by providing timely notifications and sound alerts.

### The Problem statement
Many people forget to take their medicines on time, leading to missed doses, ineffective treatment, and potential health risks. Managing multiple medications can be challenging, especially for the elderly, chronically ill patients, and busy individuals.

Existing issues include:
1. Forgetting medication schedules
2. Lack of timely reminders
3. Difficulty tracking past medication intake
4. No : system to manage multiple reminders

The Digital Medicine Reminder solves this by providing automated alerts, sound notifications, and an easy-to-use interface to ensure users never miss a dose again! 

### The Solution
orgetful about your meds? No worries! The Digital Medicine Reminder is like a personal butler for your pills, making sure you never miss a dose again.

Here’s how it works:
1. You set a reminder – Just enter your medicine name and time.
2. We handle the rest – The system schedules it, saves it, and stays on top of things.
3. Right on time! – When it’s time to take your meds, you get a pop-up notification and a gentle (or loud) alert sound.
4. Missed a dose? – Check your past reminders in the log.
5. Need a change? – Edit or delete reminders anytime with ease.

No more sticky notes. No more forgotten pills. Just set it, forget it, and stay healthy!

## Technical Details
### Technologies/Components Used
For Software:

Technologies/Components Used :
  Frontend: HTML, CSS, JavaScript
  Backend: Python (Flask)
  Database: (If applicable, mention SQLite/MySQL)
  Notifications: Plyer (for local notifications)

Frameworks & Libraries Used :

  Backend (Python - Flask) :
    Flask → For running the web server
    Flask-CORS → To allow cross-origin requests (if using API calls)
    Plyer → For desktop notifications
    
  Frontend (JavaScript, CSS):
    Vanilla JavaScript → To handle form submission and fetch requests
    CSS → For styling and UI design
    
  Tools Used :
    Code Editor: Visual Studio Code
    Package Manager: pip (for Python package management)
    Environment Management: venv (Virtual Environment)




### Implementation
For Software:
# Installation
Follow these steps to set up the project on your system:

 1. Clone the Repository (if applicable)
   git clone <repo-url>
   cd medtrack
 2. Create & Activate a Virtual Environment
    python -m venv venv  # Create virtual environment
    source venv/bin/activate  # Activate (Mac/Linux)
    venv\Scripts\activate  # Activate (Windows)
 3. Install Required Dependencies
    pip install flask flask-cors plyer

# Run
1. Start the Flask Server
   python medicine_reminder.py
   (If port 5000 is in use, change it inside app.run(debug=True, port=5001))
   
2.  Open the Application
    http://127.0.0.1:5000


### Project Documentation
For Software:

# Screenshots 
![WhatsApp Image 2025-02-09 at 09 17 09_75c20ddb](https://github.com/user-attachments/assets/88afcece-4d98-4376-be6b-7953db2077f9)

A digital interface for setting and managing medicine reminders, featuring input fields for medicine name and reminder time, along with search and active reminder display functionalities.

![WhatsApp Image 2025-02-09 at 09 47 03_00171d3f](https://github.com/user-attachments/assets/2a2312ee-666f-4a89-9ef9-3476dace7568)

A digital interface for managing medicine reminders, showing a successful reminder set message and the ability to search and view active reminders.

![WhatsApp Image 2025-02-09 at 09 17 11_013ee215](https://github.com/user-attachments/assets/4bbf5739-587a-4483-80d8-651f3e98a49a)

A digital medicine reminder interface with a focus on setting reminders, featuring input fields for medicine name and time, along with search and active reminder display sections.

![WhatsApp Image 2025-02-09 at 09 17 11_4d468201](https://github.com/user-attachments/assets/f06e22bd-eef7-4e1b-bc79-62daf71ce862)

A digital medicine reminder interface on a laptop screen, showing a "Reminder deleted successfully" message and highlighting the active reminder section.

# Diagrams

![WhatsApp Image 2025-02-09 at 09 41 22_e3db50d9](https://github.com/user-attachments/assets/a9e046ea-ceea-4dee-a151-429c7ac06fc6)

The Digital Medicine Reminder architecture consists of a frontend interface with input forms for medicine name and time settings, along with search functionality and an active reminders display section. The system follows a straightforward web-based structure where users can set medication reminders, search existing ones, and view all active reminders in a single interface.

### Project Demo
# Video

https://github.com/user-attachments/assets/7b7cc20e-6124-4ad6-b196-5c4b3e96bf62

This video explains that we can add multiple medicine names and its particular reminder time.When we click the 'Set Reminder' button  it automatically reminds the medicine name at the corresponding time. We can also delete the reminder successfully according to our choice by clicking 'Delete' button.Basically,it's a digital medicine reminder interface on a laptop screen,for a medicine name and reminder time,along with search and active reminder sections.


## Team Contributions
- Fidha V S: Frontend Developing
- Fathima Mehar P S: Backend Developing


---
Made with ❤️ at TinkerHub

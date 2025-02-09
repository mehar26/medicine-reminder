from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from plyer import notification
import time
import threading
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

reminders = []  # Store reminders in a list

# Function to send a notification
def send_notification(medicine_name, delay):
    time.sleep(delay)
    notification.notify(
        title="Medicine Reminder",
        message=f"It's time to take your medicine: {medicine_name}",
        timeout=10
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_reminder', methods=['POST'])
def set_reminder():
    medicine_name = request.form['medicine']
    reminder_time = request.form['time']

    current_time = time.strftime("%H:%M")
    time_format = "%H:%M"

    try:
        reminder_time_struct = time.strptime(reminder_time, time_format)
        current_time_struct = time.strptime(current_time, time_format)
        delay = time.mktime(reminder_time_struct) - time.mktime(current_time_struct)
    except ValueError:
        return jsonify({"status": "error", "message": "Invalid time format. Use HH:MM"})

    if delay < 0:
        delay += 24 * 60 * 60  # Handle next-day reminders

    reminder_id = len(reminders) + 1
    reminders.append({"id": reminder_id, "medicine": medicine_name, "time": reminder_time})

    threading.Thread(target=send_notification, args=(medicine_name, delay)).start()
    return jsonify({"status": "success", "message": f"Reminder set for {medicine_name} at {reminder_time}"})

@app.route('/get_reminders', methods=['GET'])
def get_reminders():
    search_query = request.args.get('search', '').lower()
    filtered_reminders = [r for r in reminders if search_query in r['medicine'].lower()]
    return jsonify(filtered_reminders)

@app.route('/delete_reminder/<int:reminder_id>', methods=['DELETE'])
def delete_reminder(reminder_id):
    global reminders
    reminders = [r for r in reminders if r['id'] != reminder_id]
    return jsonify({"status": "success", "message": "Reminder deleted successfully"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)

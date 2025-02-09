 // Load reminders on page load
function loadReminders(searchQuery = '') {
    fetch(`/get_reminders${searchQuery ? '?search=' + searchQuery : ''}`)
        .then(response => response.json())
        .then(reminders => {
            const remindersListDiv = document.getElementById('remindersList');
            remindersListDiv.innerHTML = '';

            reminders.forEach(reminder => {
                const reminderCard = document.createElement('div');
                reminderCard.className = 'reminder-card';
                reminderCard.innerHTML = `
                    <div class="reminder-info">
                        <strong>${reminder.medicine}</strong><br>
                        <span class="reminder-time">Time: ${reminder.time}</span>
                    </div>
                    <button class="delete-btn" onclick="deleteReminder(${reminder.id})">Delete</button>
                `;
                remindersListDiv.appendChild(reminderCard);
            });
        });
}

// Delete reminder
function deleteReminder(id) {
    fetch(`/delete_reminder/${id}`, { method: 'DELETE' })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                loadReminders();
                showNotification('Reminder deleted successfully', 'success');
            }
        });
}

// Show notification
function showNotification(message, type) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = type;
    notification.style.display = 'block';
    setTimeout(() => {
        notification.style.display = 'none';
    }, 3000);
}

// Form submission
document.getElementById('reminderForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);

    fetch('/set_reminder', { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => {
            showNotification(data.message, data.status);
            if (data.status === 'success') {
                this.reset();
                loadReminders();
            }
        })
        .catch(error => {
            showNotification('An error occurred. Please try again.', 'error');
        });
});

// Search functionality
function searchReminders() {
    const searchQuery = document.getElementById('searchInput').value.trim();
    loadReminders(searchQuery);
}

// Initial load
loadReminders();

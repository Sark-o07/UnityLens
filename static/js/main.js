// Enable tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// Enable Logout Icon
document.getElementById("logoutButton").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the default behavior of the anchor tag (navigating to a new page)
    document.getElementById("logoutForm").submit(); // Submit the form
});

// Function to navigate back to the previous page in the browser's history
function goBack() {
    window.history.back();
  }
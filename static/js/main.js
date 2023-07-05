const chatEntry = document.getElementById('open_chat');

chatEntry.addEventListener('submit', function(event) {
    event.preventDefault();
    console.log('submitted');
    const formData = new FormData(this);
    fetch('/chat', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/chat';
        } else {
            console.error("Error during operation")
        }
    })
    .catch(error => {
        console.error(error);
    });
});
const messageInput = document.getElementById('message');
messageInput.addEventListener('keydown', function(event) {

    if (event.key === 'Enter') {
        const messageInputText = messageInput.value;
        fetch('/chat/add_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({messageInputText})
        })
        .then(response => response.json())
        .then(response => {
            console.log(response)
            messageInput.value = '';
        })
    }
});
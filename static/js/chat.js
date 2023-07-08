const messageInput = document.getElementById('message');
const messagesWindow = document.getElementById('messages_window');

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

function checkMessages() {
    fetch('/chat/check_messages', {
        method: 'POST' })
    .then(response => response.json())
    .then(response => {
        if (response['messages'] === "NONE") {
            console.log('NO NEW MESSAGES') }
        else {
            console.log(response[0])
            for (let i = 0; i < response.length; i++)  {
                    let new_message = document.createElement('div');
                    new_message.innerHTML = `<span class="h5 pe-3">${response[i]['user_name']}</span><span class="h6">${response[i]['submission_date']}</span><br/>${response[i]['message']}`
                    messagesWindow.appendChild(new_message);
            }
        }

    })
}

setInterval(checkMessages, 1000);
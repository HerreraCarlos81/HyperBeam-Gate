async function startHyperbeam() {
    const inputValue = document.getElementById('inputBox').value;
    
    // Adjust the endpoint URL accordingly
    const endpoint = `https://your-lambda-url.amazonaws.com/default/startFunction?value=${encodeURIComponent(inputValue)}`;
    
    try {
        let response = await fetch(endpoint);
        let data = await response.json();

        if (data && data.embed_url) {
            const iframe = document.getElementById('myIframe');
            iframe.src = data.embed_url;

            // Store the session_id in sessionStorage
            sessionStorage.setItem('session_id', data.session_id);
        } else {
            console.error("embed_url not found in response");
        }
    } catch (error) {
        console.error(error);
    }
}

async function terminateHyperbeam() {
    const sessionId = sessionStorage.getItem('session_id');
    
    if (!sessionId) {
        console.error("No session id found");
        return;
    }

    // Adjust the endpoint URL accordingly
    const endpoint = `https://your-lambda-url.amazonaws.com/default/terminateFunction?session_id=${sessionId}`;
    
    try {
        let response = await fetch(endpoint);
        if (response.status === 200) {
            const iframe = document.getElementById('myIframe');
            iframe.src = "";
            
            // Clear session_id from sessionStorage
            sessionStorage.removeItem('session_id');
        } else {
            console.error("Error terminating session");
        }
    } catch (error) {
        console.error(error);
    }
}
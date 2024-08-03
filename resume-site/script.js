var apiUrl = "https://lczsn4gvg0.execute-api.us-east-1.amazonaws.com/Prod/put";
fetch(apiUrl)
    .then(() => fetch("https://lczsn4gvg0.execute-api.us-east-1.amazonaws.com/Prod/get"))
    .then(response => response.json())
    .then((data) =>{
        document.getElementById('clicks').innerHTML = data
    })

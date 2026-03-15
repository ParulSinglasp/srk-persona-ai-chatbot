async function sendMessage() {
  let input = document.getElementById("userInput");
  let message = input.value;

  let chatbox = document.getElementById("chatbox");

  chatbox.innerHTML += "<p><b>You:</b> " + message + "</p>";

  let response = await fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: message,
    }),
  });

  let data = await response.json();

  chatbox.innerHTML += "<p><b>SRK:</b> " + data.reply + "</p>";

  input.value = "";
}

const socket = io("http://localhost:5001");
socket.addEventListener("connect",()=>{
    console.log("connected to server")
})

socket.on("new_signature", (data) => {
    console.log("Received new signature");
    document.getElementById("signature").src = data.image;
  });
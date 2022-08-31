var Chat = (function() { 
    function Chat() {}

    Chat.prototype.showMessage = function (message) {
        var tempNode = document.querySelector('[data-type="template-left"]').cloneNode(true);
        tempNode.querySelector("div.chat-bubble").textContent = message;
        tempNode.style.display = "flex";
        document.getElementById("chatWindow").appendChild(tempNode);
        
    }

    Chat.prototype.showUserMessage = function (message) {
        var tempNode = document.querySelector('[data-type="template-right"]').cloneNode(true);
        tempNode.querySelector("div.chat-bubble").textContent = message;
        tempNode.style.display = "flex";
        document.getElementById("chatWindow").appendChild(tempNode);
        document.getElementById("newMessage").value = "";
    }

    Chat.prototype.disableSendingMessages = function () {
        document.getElementById("sendMessageBlock").style.display = "none";
    }

    Chat.prototype.enableSendingMessages = function (src) {
        if(src==null) {
            src = "Default_Avatar.png";
        }
        document.getElementById("sendMessageBlock").style.display = "flex";
        document.querySelector('[data-type="template-right"]').querySelector("img").src = src;
        document.getElementById("userSendMessage").onclick = function() {
        var message = document.getElementById("newMessage").value;
        userMessage(message);
        }
    }

    return Chat;
})();


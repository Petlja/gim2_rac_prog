var miliseconds = 3000;
var oldData = []
setInterval(readTextFile, miliseconds)
window.addEventListener('load', function () {
    readTextFile()
});

function readTextFile() {
    $.get('/_static/error_log.txt',{ "_": $.now() }, function (data) {
        var div = document.getElementById("errors");
        div.innerHTML = data.replace('\n','').replaceAll('\n','<br>');
    }, 'text')
}

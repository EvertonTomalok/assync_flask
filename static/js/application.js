
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    console.log('http://' + document.domain + ':' + location.port + '/test')
    // var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        var numbers_string = '';
        for (var i = 0; i < msg.number.length; i++){
            var obj = msg.number[i];
            let nome = obj["nome"];
            let clientId = obj["cliente_id"];
	    let total = obj["total"];
            numbers_string += "<p>nome:" + nome + " client_id:" +  clientId + "total: " + total + "</p>";
        }
        $('#log').html(numbers_string);
    });

});


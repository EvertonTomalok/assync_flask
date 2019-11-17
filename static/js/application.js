
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/comandas_ativas');
    console.log('http://' + document.domain + ':' + location.port + '/comandas_ativas')

    //receive details from server
    socket.on('comandas', function(msg) {
        var comandas_string = '';
        for (var i = 0; i < msg.lista_comandas.length; i++){
            var obj = msg.lista_comandas[i];
            let nome = obj["nome"];
            let clientId = obj["cliente_id"];
            let total = obj["total"];
            let inicio = obj["inicio"]
            comandas_string += "<p>nome: " + nome + " | client_id: " +  clientId + " | total: " + total + " | inicio: " + inicio +"</p>";
        }
        $('#log').html(comandas_string);
    });

});


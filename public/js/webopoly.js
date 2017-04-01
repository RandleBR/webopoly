// button click for index.html page

$(function() {
    $('#btnadd').click(function() {
        var dataString = 'gamepiece=' + $("#game_piece").val();
        $("#game_piece").val("");
        $("#game_piece").focus();

        $.ajax({
                type: "POST",
                url: "newgamepiece",
                data: dataString,
                success: function (ret) {
                    result = JSON.parse(ret)
                    if (result.success == true) {            
                        $('#results ul').after('<li>'+result.gamepiece +'-' + result.msg+'</li>')
                    } else {
                        alert(result.msg)
                    }
      
                }
        });
        return false;
    })
})
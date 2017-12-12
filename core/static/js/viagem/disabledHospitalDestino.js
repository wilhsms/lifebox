$(document).ready(function(){
    
    $("#id_localPartida").change(function(){
        $("#id_localChegada option").removeAttr('disabled');
        var value = $("#id_localPartida").val();
        $("#id_localChegada option[value="+value+"]").attr('disabled', 'disabled');
    });
    
    $("#id_localChegada").change(function(){
        $("#id_localPartida option").removeAttr('disabled');
        var value = $("#id_localChegada").val();
        $("#id_localPartida option[value="+value+"]").attr('disabled', 'disabled');
    });
});
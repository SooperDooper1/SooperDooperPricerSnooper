$("#get_price").on('click', function(){
<<<<<<< Updated upstream
=======
    $("#captain_price").css('visibility', 'visible');
>>>>>>> Stashed changes
    $.ajax({
        url: '/get_price/',
        type: 'post',
        headers: {
            'Content-Type': 'application/json'
         },
        data: JSON.stringify({
            "start_date": $("#start_date").val(),
            "end_date": $("#end_date").val(),
        }),
        success: function(response){
            $("#captain_price").css('visibility', 'hidden');
            $('#price').text(response)
            $('#suggested_price').css('visibility', 'visible');
        }
    })

});

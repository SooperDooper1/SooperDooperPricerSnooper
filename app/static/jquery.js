$("#get_price").on('click', function(){
    $('#suggested_price').css('visibility', 'visible').css(background(url:'captain_price.jpg'))
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
            $('#price').text(response)
            $('#suggested_price').css('visibility', 'visible');
        }
    })

});

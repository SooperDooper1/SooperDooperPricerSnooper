$("#get_price").on('click', function(){
    $.ajax({
        url: '/get_price',
        type: 'POST',
        success: function(response){
            $('#price').text(response)
            $('#suggested_price').css('visibility', 'visible');
        }
    })

});

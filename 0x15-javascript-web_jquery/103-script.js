$(document).ready(function () {
    $('#btn_translate').click(translateHello);
    
    $('#language_code').on('keypress', function (event) {
        if (event.keyCode === 13) {
            translateHello();
        }
    });

    function translateHello() {
        const languageCode = $('#language_code').val();
        
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
            $('#hello').text(data.hello);
        }).fail(function () {
            $('#hello').text('Translation not found');
        });
    }
});

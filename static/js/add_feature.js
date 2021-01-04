$('#add').click(function () {
    var key = $('#key').val()
    var value = $('#value').val()
    var new_feature = `{"key":"${key}","value":"${value}"}`

        $('#id_features').val($('#id_features').val() + new_feature + '\n')

        $('#id_main_features').val($('#id_main_features').val() + new_feature + '\n')


})

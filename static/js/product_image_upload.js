var token = '{{csrf_token}}';
var ecommName = "فروشگاه اینترنتی بل"
// upload product images and save paths
$('#upload').submit(function (event) {
    event.preventDefault();
    var directory = ($('#directory').val() == "" ? "base" : $('#directory').val()).replace(/'|"/g, " ")
    var alternative_text = ($('#alternative_text').val() == "" ? ecommName : $('#alternative_text').val()).replace(/'|"/g, " ")
    var title = ($('#file_name').val() == "" ? ecommName : $('#file_name').val()).replace(/'|"/g, " ")
    var data = new FormData($('#upload').get(0));
    data.append('directory', directory)
    data.append('alternative_text', alternative_text)
    data.append('title', title)
    $.ajax({
        headers: {"X-CSRFToken": token},
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: data,
        success: function (response) {
            if (response.error == false) {
                if ($('#is_thumbnail').prop("checked")) {
                    $('#id_thumbnail').val(response['file-path'])
                    $('#id_thumbnail').after(`<div class="upload-image-preview"> <a class="delete_image" href="" id="${directory}/${data.get('file_source').name}">x</a> <img id="" src="${response['file-path']}"/></div>`)

                } else {
                    newImg = `{"title": "${title}","path": "${response['file-path']}","alt":"${alternative_text}"}`
                    $('#id_images').val($('#id_images').val() !== "" ?$('#id_images').val()+ "\n" + newImg  : newImg)
                    $('#images').append(`<div class="upload-image-preview"> <a class="delete_image" href="" id="${directory}/${data.get('file_source').name}">x</a> <img id="" src="${response['file-path']}"/></div>`)

                }
            } else {
                response.errors.forEach(error => alert(error))
            }
        },
        cache: false,
        processData: false,
        contentType: false,

    });
    return false;
})

// $('#id_images').prop('disabled', true)
$('#id_images').prop('rows', 2)
$('document').ready(function () {
    if ($('#update-heading').text() == "update") {
        var thumbnail = $('#id_thumbnail').val()
        $('#id_thumbnail').after(`<div class="upload-image-preview"> <a class="delete_image" href="" id="${thumbnail.substr(thumbnail.indexOf('uploads') + 8, thumbnail.length)}">x</a> <img id="" src="${thumbnail}"/></div>`)
        var images = $('#id_images').text().split('\n')
        images.forEach(image => {
            image = JSON.parse(image)
            newImg = `{"title": "${image.title}","path": "${image.path}","alt":"${image.alt}"}`
            $('#images').append(`<div class="upload-image-preview"> <a class="delete_image" href="" id="${image.path.substr(image.path.indexOf('uploads') + 8, image.path.length)}">x</a> <img id="" src="${image.path}"/></div>`)

        })
    }
})


$(document).on('click', '.delete_image', function (event) {
    event.preventDefault()
    if (this.images) {
        this.images.delete()
    }
    $.ajax({
        url: `/admin/panel/${event.target.id}/delete`,
        success: function (response) {
            if (response.error == false) {
                event.target.parentNode.remove()
                var images = $('#id_images').val().split('\n')
                var newImages = ''
                images.forEach(image => {
                    if (image.includes(event.target.id)) {
                    } else {
                        newImages += image + '\n'
                    }
                })
                $('#id_images').val(newImages)
            } else {
                console.log(response.errors)
            }
        }
    })
})
$(document).on('submit', '#comment-form', function (e) {
    e.preventDefault();
    const id = $(this).data("id");
    const username = $(this).data("username");
    const token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        type: 'POST',
        url: "http://127.0.0.1:8000/api/comment/create/photo/" + id,
        headers: {
            "X-CSRFTOKEN": token
        },
        data: {
            text: $('#text').val(),
        },
        success: function (json) {
            console.log(json.id)
            document.getElementById("comment-form").reset();
            $(".comments").prepend(`<div class=comment-${json.id}>` + "<p class='description comment-inline'>" + "<span>" + username + "</span>" + json.text + "</p>" + `<button type='button' class='btn-close  comment-delete' style='width: 5px; height: 5px' aria-label='Закрыть' data-id=${json.id} data-token=${token}>` + "</button>" + "</div>");
        },
    });
});


$(document).ready(function () {
    $("body").on("click", ".comment-delete", function (e) {
        e.preventDefault();
        const id = $(this).data("id");
        const token = $(this).data("token");

        $.ajax({
            url: `http://127.0.0.1:8000/api/comment/${id}/delete/`,
            type: 'DELETE',
            dataType: 'json',
            headers: {
                "X-CSRFTOKEN": token
            },
            data: {
                id: id
            },
            success: function (response) {
                $(".comments .comment-" + id).remove();
            }
        });
        return false;
    });
});

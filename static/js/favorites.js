$(document).ready(function () {
    $("body").on("click", ".manage-favorite", function (e) {
        e.preventDefault();
        const id = $(this).data("id");
        const token = $(this).data("token");

        $.ajax({
            url: "http://127.0.0.1:8000/api/favorites/photo/" + id,
            type: 'PUT',
            dataType: 'json',
            headers: {
                "X-CSRFTOKEN": token
            },
            data: {
                id: id,
            },
            success: function (response) {
                if (response.favorites === "Yes") {
                    $(".manage-favorite-" + id).text("Убрать из избранного").removeClass("btn-outline-success").addClass("btn-outline-danger");
                } else {
                    $(".manage-favorite-" + id).text("Добавить в избранное").removeClass("btn-outline-danger").addClass("btn-outline-success");
                }
            }
        });
        return false;
    });
});

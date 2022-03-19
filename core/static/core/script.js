// Отправка сообщения в database
$(".form-message").submit(function (e) {
    e.preventDefault();
    console.log(window.location.href);
    $.ajax({
        method: 'POST',
        data: $(this).serialize(), // получаяем данные формы
        url: '/api/obrashenie/',
        success: function (response) {
            alert('Поздравляю ваше сообщение отправлено в database');
        },
        error: function (response) {
            alert('Внимание!! Что-то пошло не так');
        }
    });
});
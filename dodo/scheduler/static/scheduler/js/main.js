var addSchedule = function () {
    var title = document.getElementById("title").value;
    var text = document.getElementById("text").value;
    var dt_start = document.getElementById("date-start").value + " " + document.getElementById("time-start").value;
    var dt_end = document.getElementById("date-end").value + " " + document.getElementById("time-end").value;
    var params = {'title': title, 'text': text, 'dt_start': dt_start, 'dt_end': dt_end};
    var empty_element = ""
    var del_list = {"":"", " ":"", "  ":""}
    for (var key in params) {
        if (params[key] in del_list) {
            empty_element += key + ", "
        }
    }
    if (!(empty_element in del_list)) {
        alert(empty_element+"항목을 입력해주십시오.");
        return;
    }
    // post schedule
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "http://127.0.0.1:8000/schedule/post/",
        data: params,
        success: function(response) {
            alert("\'"+response.schedule.title+"\' 일정이 추가되었습니다.")
        },
        error: function(request, status, error){
            alert("일정을 추가하는데 실패했습니다.")
        }
    })
}

$(document).ready(function() {
    var now = new Date();
    var day = ("0" + now.getDate()).slice(-2);
    var month = ("0" + (now.getMonth() + 1)).slice(-2);
    var hour = ("0" + (now.getHours())).slice(-2);
    var min = ("0" + (now.getMinutes())).slice(-2);
    var today_date = now.getFullYear()+"-"+(month)+"-"+day;
    var today_time = hour+":"+min;
    $('#date-start').val(today_date);
    $('#date-end').val(today_date);
    $('#time-start').val(today_time);
    $('#time-end').val(today_time);
});

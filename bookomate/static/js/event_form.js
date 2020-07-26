const calculateTimeToMinutes = function(time) {
    let timeArray = time.split(":");
    let minutes = 0;
    minutes += Number(timeArray[0]) % 24 * 60;
    minutes += Number(timeArray[1]);
    return minutes; 
};

const calculateDuration = function(startTime, endTime) {
    let startMinutes = calculateTimeToMinutes(startTime);
    let endMinutes = calculateTimeToMinutes(endTime);
    if (endMinutes < startMinutes) {
        return (endMinutes + 1440) - startMinutes;
    } else {
        return endMinutes - startMinutes;
    }
};

const timeFromMinutes = function(minutes) {
    let hours = Math.floor(minutes / 60) % 24;
    let timeMinutes = minutes % 60;
    return ("0" + hours).slice(-2) + ":" + ("0" + timeMinutes).slice(-2);
}
const dateToday = function() {
    let today = new Date();
    return today.getFullYear() + '-' + ("0" + (today.getMonth() + 1)).slice(-2) + '-' + today.getDate();
}
const currentTime = function() {
    let time = new Date();
    return ("0" + time.getHours()).slice(-2) + ":"
     +("0" + time.getMinutes()).slice(-2);
};
const calculateEnd = function(start, duration) {
    let startMinutes  = calculateTimeToMinutes(start);
    return timeFromMinutes(startMinutes + duration);
};

const updateDurationButtons = function() {
    let start = $("#start_time").val();
    let end = $("#end_time").val();
    let duration = calculateDuration(start, end);
    $(".duration span.active").toggleClass("active");
    switch (duration) {
        case 30:
            $("#btn_30m").toggleClass("active");
            break;
        case 60:
            $("#btn_1h").toggleClass("active");
            break;
        case 120:
            $("#btn_2h").toggleClass("active");
            break;
        default:
            $("#inp_other").val(duration);
            $("#btn_other").toggleClass("active");
    };
};

const updateEndTime = function(duration) {
    let startTime = $("#start_time").val();
    let endTime = calculateEnd(startTime, duration);
    $("#end_time").val(endTime);
};
const durationButtonListener = function() {
    let id = $(this).attr("id");
    let start =$("#start_time").val();
    let duration;
    switch (id) {
        case "btn_30m":
            duration = 30;
            break;
        case "btn_1h":
            duration = 60;
            break;
        case "btn_2h":
            duration = 120;
            break;
        case "btn_other":
            duration = Number($("#inp_other").val()) || 0;
            break;
        case "inp_other":
            duration = Number($("#inp_other").val()) || 0;
            break;
    };
    updateEndTime(duration);
    updateDurationButtons()
};
const deleteAction = function() {
    if(confirm("Are you sure you would like to delete this event?")) {
        window.location.href = window.location.href + '/delete'
        return false;
    } else {
    };
};

$(() => {
    let openedTime = currentTime();
    $("#start_date").val($("#start_date").val() || dateToday);
    $("#start_time").val($("#start_time").val() || openedTime);
    $("#end_time").val($("#end_time").val() || calculateEnd(openedTime, 60));
    updateDurationButtons();
    $("#end_time").on("change", updateDurationButtons);
    $(".duration span").on("click", durationButtonListener);
    $("#inp_other").on("change", durationButtonListener);
    $("#btn_delete").on("click", deleteAction);
    
});
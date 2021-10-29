// getting all required elemenets
const microscopy_quiz = document.getElementById("microscopy-quiz");
const feature_quiz = document.getElementById("feature-quiz");
const start_btn_container = document.querySelector(".start_btn");
const start_btn = document.querySelector(".start_btn button");
const info_box = document.querySelector(".info_box");
const exit_btn = info_box.querySelector(".buttons .quit");
const continue_btn = info_box.querySelector(".buttons .restart");
const quiz_box = document.querySelector(".quiz_box");
const logo_paragraph_box = document.querySelector(".choose-type");
const question_choose = document.querySelector(".question-chooser");
const quit_btn = document.querySelector(".quit-btn");


// if microscopy quiz button is clicked
// microscopy_quiz.onclick = () => {
//     logo_paragraph_box.classList.add("deactivate");
//     question_choose.classList.add("deactivate");
//     quit_btn.classList.add("deactivate");
//     start_btn_container.classList.add("activeInfo");
// }

// if feature quiz button is clicked
// feature_quiz.onclick = () => {
//     logo_paragraph_box.classList.add("deactivate");
//     question_choose.classList.add("deactivate");
//     quit_btn.classList.add("deactivate");
//     start_btn_container.classList.add("activeInfo");
// }


// if start button clicked
start_btn.onclick = () => {
    info_box.classList.add("activeInfo");
}

// // hide the info box
exit_btn.onclick = () => {
    // logo_paragraph_box.classList.remove("deactivate");
    // question_choose.classList.remove("deactivate");
    // quit_btn.classList.remove("deactivate");
    info_box.classList.remove("activeInfo");
    start_btn_container.classList.remove("activeInfo");
}

// If continue button is clicked
continue_btn.onclick = () => {
    info_box.classList.remove("activeInfo");
    quiz_box.classList.add("activeQuiz");
}

$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "{% url '/quiz/microscopy_quiz' %}",
        data: "data",
        dataType: "dataType",
        success: function (response) {
            
        }
    });    
});
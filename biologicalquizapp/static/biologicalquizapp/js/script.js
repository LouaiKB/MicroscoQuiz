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
const images_field = document.querySelector(".images");
const option_list = document.querySelector(".option_list");
const bottom_quest_counter = quiz_box.querySelector(".total_que");
const timerCount = quiz_box.querySelector(".timer .timer_sec");
const timerLine = quiz_box.querySelector("header .time_line");
const result_box = document.querySelector(".result_box");
const restart_quiz = result_box.querySelector(".buttons .restart");
const quit_quiz = result_box.querySelector(".buttons .quit");
const timeText = document.querySelector(".timer .time_text");
const timeCount = document.querySelector(".timer .timer_sec");

// if start button clicked
start_btn.onclick = () => {
    info_box.classList.add("activeInfo");
}

// return to choosing menue
exit_btn.onclick = () => {
    location.href = window.location.origin + '/quizapp';
}



// If continue button is clicked
continue_btn.onclick = () => {
    info_box.classList.remove("activeInfo");
    quiz_box.classList.add("activeQuiz");
    startTimer(20);
    startTimerLine(0);
}

let que_count = 0;
let counter;
let timeValue = 20;
let widthValue = 0;

quit_quiz.onclick = () => {
    location.href = window.location.origin + '/quizapp';
}

restart_quiz.onclick = () => {
    window.location.reload();
}

// getting questions and options from array
function showQuestions(index, data, num_img) {
    var url_origin = window.location.origin;
    const images_field = document.querySelector(".images");
    const option_list = document.querySelector(".option_list");
    if(num_img == 3) {
        let img_tag = '<img src='+ url_origin+'/static/'+data[index]['images'][0]+' alt="cell" class="img-option">' + 
                      '<img src='+url_origin+ '/static/'+data[index]['images'][1]+' alt="cell" class="img-option">' +
                      '<img src=' + url_origin+'/static/'+data[index]['images'][2]+' alt="cell" class="img-option">';
        images_field.innerHTML = img_tag;
    } else if(num_img == 2) {
        let img_tag = '<img src=' + url_origin+'/static/'+data[index]['images'][0]+' alt="cell" class="img-option">' + 
                      '<img src='+ url_origin+'/static/'+data[index]['images'][1]+' alt="cell" class="img-option">';
        images_field.innerHTML = img_tag;
    }
    
    let option_tag = '';

    for (let i = 0; i < 4; ++i) {
        if (data[index]['answers'][i] === data[index]['correct_answer']) {
            option_tag += '<div class="option"><span>' + data[index]['answers'][i] + '</span></div>';
        } else {
            option_tag += '<div class="option"><span>' + data[index]['answers'][i] + '</span></div>';
        }                  
    }
    option_list.innerHTML = option_tag;
    
    const option = option_list.querySelectorAll(".option");
    for (let i = 0; i < option.length; i++) {
        option[i].setAttribute("onclick", `optionSelected(this)`);
        
    }
}

function queCounter(index, question_len) {
    let totalQuesCountTag = '<span><p>' + index + '</p>of<p>' + question_len + '</p>Questions</span>';
    bottom_quest_counter.innerHTML = totalQuesCountTag;
}


function startTimerLine(time) {
    counterLine = setInterval(timer, 26);
    function timer() {
        time += 1
        timerLine.style.width = time + "px";
        if (time > 800) {
            clearInterval(counterLine);
        }
    }
}

function showResultBox(all_score) {
    info_box.classList.remove("activeInfo");
    quiz_box.classList.remove("activeQuiz");
    result_box.classList.add("activeResult");
    const scoreText = result_box.querySelector(".score_text");
    if (all_score == 30) {

        if (score >= 21) {
            let scoreTag = `<span>Congratulation! very good You got ${score} out of ${all_score}</span>`;
            scoreText.innerHTML = scoreTag;
        } 
        else if (score > 15 && score < 21) {
            let scoreTag = `<span>Good job!, You got ${score} out of ${all_score}</span>`;
            scoreText.innerHTML = scoreTag;    
        }
        else if (score < 15) {
            let scoreTag = `<span>Hard luck!, sorry You got ${score} out of ${all_score}</span>`;
            scoreText.innerHTML = scoreTag;
        }
    }
    else if (all_score == 20) {
        if (score >= 16) {
            let scoreTag = `<span>Congratulation! very good You got ${score} out of ${all_score}</span>`;
            scoreText.innerHTML = scoreTag;
        } 
        else if (score > 10 && score < 16) {
            let scoreTag = `<span>Good job!, You got ${score} out of ${all_score}</span>`;
            scoreText.innerHTML = scoreTag;    
        }
        else if (score < 10) {
            let scoreTag = `<span>Hard luck!, sorry You got ${score} out of ${all_score}</span>`;
            scoreText.innerHTML = scoreTag;
        }

    }
}


var url = window.location.href;
const csrf = document.getElementsByName('csrfmiddlewaretoken');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;



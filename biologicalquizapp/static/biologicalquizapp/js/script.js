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
const next_btn = document.querySelector(".next_btn");
const images_field = document.querySelector(".images");
const option_list = document.querySelector(".option_list");



// if start button clicked
start_btn.onclick = () => {
    info_box.classList.add("activeInfo");
}

// // hide the info box
exit_btn.onclick = () => {
    info_box.classList.remove("activeInfo");
    start_btn_container.classList.remove("activeInfo");
}

// If continue button is clicked
continue_btn.onclick = () => {
    info_box.classList.remove("activeInfo");
    quiz_box.classList.add("activeQuiz");
}

$.ajax({
    type: 'GET',
    url: `${url}save`,
    success: function (response) {
        var data = response.data;
        var data_len = response.data.length;
        var image = response.data[0].images;
        index = 0;
        next_btn.onclick = () => {
            if (index < data_len- 1) {
                index++;
                var num_img = image.length;
                console.log('number images ' + num_img);
                showQuestions(index, data, num_img);
            } else {
                console.log('questions completed');
            }
        }
    },
    error: function(response) {
        console.log('wronnnnnnnnnnnnnggg!!!!')
    }
});

let que_count = 0;

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
            option_tag += '<div class="option"><span>' + data[index]['answers'][i] + '</span>' +
                           '<div class="icon tick"><i class="fas fa-check"></i></div></div>';
        } else {
            option_tag += '<div class="option"><span>' + data[index]['answers'][i] + '</span>' +
                           '<div class="icon cross"><i class="fas fa-times"></i></div></div>';
        }                  
    }
    option_list.innerHTML = option_tag;
}



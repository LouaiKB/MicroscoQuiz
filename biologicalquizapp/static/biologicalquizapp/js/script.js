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
const img = document.getElementById("img");

next_btn.onclick = () => {
    console.log(img);
}

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

const url = window.location.href;
console.log("sdfjlsdkfj " + url);

// function call_ajax() {
    // return 
$.ajax({
    type: 'GET',
    url: `${url}save`,
    success: function (response) {
        var data = response.data;
        var data_len = response.data.length;
        var image = response.data[0].images;
        console.log('length: ', image.length);
        const images_field = document.querySelector(".images");
        const option_list = document.querySelector(".option_list");
        // var next_btn = document.querySelector(".next_btn");
        // console.log('response length ' + response.data);
        console.log(data);
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
// }
// call_ajax();

let que_count = 0;


// $.when(call_ajax()).done(function(response){
//     console.log(response.data.length)
//     next_btn.onclick = () => {
//         console.log('response length ' + response.data.length);
//         if (que_count < response.data.length - 1) {
//             que_count++;
//             var num_img = response.data['images'].length;
//             console.log('number images ' + num_img);
//             showQuestions(que_count, response.data, num_img);
//         } else {
//             console.log('questions completed');
//         }
//     }
// });

console.log(window.location.origin);


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
    let option_tag = '<div class="option"><span>' + data[index]['answers'][0] + '</span></div>' +
                     '<div class="option"><span>' + data[index]['answers'][1] + '</span></div>' + 
                     '<div class="option"><span>' + data[index]['answers'][2] + '</span></div>' + 
                     '<div class="option"><span>' + data[index]['answers'][3] + '</span></div>';
    option_list.innerHTML = option_tag;
}



// if (index < data_len - 1) {
//     index++;
//     var num_img = image.length;
//     console.log('number images ' + num_img);
//     // showQuestions(que_count, response.data, num_img);
//     if(num_img == 3) {
//         let img_tag = '<img src="{% static ' + data[index]['images'][0] + ' %}" alt="cell" class="img-option">' + 
//                       '<img src="{% static ' + data[index]['images'][1] + ' %}" alt="cell" class="img-option">' +
//                       '<img src="{% static ' + data[index]['images'][2] + ' %}" alt="cell" class="img-option">';
//         images_field.innerHTML = img_tag;
//     } else if(num_img == 2) {
//         let img_tag = '<img src="{% static ' + data[index]['images'][0] + ' %}" alt="cell" class="img-option">' + 
//                       '<img src="{% static ' + data[index]['images'][1] + ' %}" alt="cell" class="img-option">';
//         images_field.innerHTML = img_tag;
//     }
//     let option_tag = '<div class="option"><span>' + data[index]['answer'][0] + '</span></div>' +
//                      '<div class="option"><span>' + data[index]['answer'][1] + '</span></div>' + 
//                      '<div class="option"><span>' + data[index]['answer'][2] + '</span></div>' + 
//                      '<div class="option"><span>' + data[index]['answer'][3] + '</span></div>';
//     option_list.innerHTML = option_tag;
// } else {
//     console.log('questions completed');
// }
// }
// Getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");

// if user press any key and release
inputBox.onkeyup = (e) => {
    let userData = e.target.value;
    let emptyArray = [];
    if (userData) {
        emptyArray = metadatas.filter((data) => {
            // filtering array value and user char to lowercase and return only 
            // those word/setence 
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data) => {
            return data = '<li>' + data + '</li>';
        });
        console.log(emptyArray);
        searchWrapper.classList.add("active");
        showSuggestions(emptyArray);
        let allList = suggBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            // adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", "select(this)"); 
        }
    } else {
        searchWrapper.classList.remove("active");
    }
}

function select(element) { 
    let selectUserData = element.textContent;
    inputBox.value = selectUserData;
    searchWrapper.classList.remove("active");
 }

function showSuggestions(list) {
    let listData;
    if (!list.length) {
        var userValue = inputBox.value;
        listData = '<li>' + userValue + '</li>'; 
    } else {
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
}
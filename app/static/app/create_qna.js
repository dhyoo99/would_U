function gray(e) {
    e.parentNode.childNodes[1].setAttribute('class', '');
    e.parentNode.childNodes[3].setAttribute('class', '');
    e.parentNode.childNodes[5].setAttribute('class', '');
    e.parentNode.childNodes[7].setAttribute('class', '');
    e.setAttribute('class', 'gray-count')
}

var script = document.getElementById("script")
var scrNext = document.getElementById("script_next")

var qna1 = document.getElementById("question_1")
var qna2 = document.getElementById("question_2")
var qna3 = document.getElementById("question_3")
var qna4 = document.getElementById("question_4")
var qna5 = document.getElementById("question_5")
var qna6 = document.getElementById("question_6")
var qna7 = document.getElementById("question_7")
var qna8 = document.getElementById("question_8")
var qna9 = document.getElementById("question_9")

var back1 = document.getElementById("back_1")
var back2 = document.getElementById("back_2")
var back3 = document.getElementById("back_3")
var back4 = document.getElementById("back_4")
var back5 = document.getElementById("back_5")
var back6 = document.getElementById("back_6")
var back7 = document.getElementById("back_7")
var back8 = document.getElementById("back_8")
var back9 = document.getElementById("back_9")

var next1 = document.getElementById("next_1")
var next2 = document.getElementById("next_2")
var next3 = document.getElementById("next_3")
var next4 = document.getElementById("next_4")
var next5 = document.getElementById("next_5")
var next6 = document.getElementById("next_6")
var next7 = document.getElementById("next_7")
var next8 = document.getElementById("next_8")
var next9 = document.getElementById("next_9") // done 버튼 만들기

scrNext.addEventListener("click", () => {
    script.style.display = 'none';
    scrNext.style.display = 'none';
    qna1.style.display = 'flex';
})

back1.addEventListener("click", () => {
    script.style.display = 'block';
    scrNext.style.display = 'block';
    qna1.style.display = 'none';
})

next1.addEventListener("click", () => {
    qna1.style.display = 'none';
    qna2.style.display = 'flex';
})

back2.addEventListener("click", () => {
    qna1.style.display = 'flex';
    qna2.style.display = 'none';
})

next2.addEventListener("click", () => {
    qna2.style.display = 'none';
    qna3.style.display = 'flex';
})

back3.addEventListener("click", () => {
    qna2.style.display = 'flex';
    qna3.style.display = 'none';
})

next3.addEventListener("click", () => {
    qna3.style.display = 'none';
    qna4.style.display = 'flex';
})

back4.addEventListener("click", () => {
    qna3.style.display = 'flex';
    qna4.style.display = 'none';
})

next4.addEventListener("click", () => {
    qna4.style.display = 'none';
    qna5.style.display = 'flex';
})

back5.addEventListener("click", () => {
    qna4.style.display = 'flex';
    qna5.style.display = 'none';
})

next5.addEventListener("click", () => {
    qna5.style.display = 'none';
    qna6.style.display = 'flex';
})

back6.addEventListener("click", () => {
    qna5.style.display = 'flex';
    qna6.style.display = 'none';
})

next6.addEventListener("click", () => {
    qna6.style.display = 'none';
    qna7.style.display = 'flex';
})

back7.addEventListener("click", () => {
    qna6.style.display = 'flex';
    qna7.style.display = 'none';
})

next7.addEventListener("click", () => {
    qna7.style.display = 'none';
    qna8.style.display = 'flex';
})

back8.addEventListener("click", () => {
    qna7.style.display = 'flex';
    qna8.style.display = 'none';
})

next8.addEventListener("click", () => {
    qna8.style.display = 'none';
    qna9.style.display = 'flex';
})

back9.addEventListener("click", () => {
    qna8.style.display = 'flex';
    qna9.style.display = 'none';
})

var qna = document.getElementById("qna")

next9.innerHTML = "done!"
next9.addEventListener("click", () => {
    if (document.getElementsByClassName('gray-count').length < 9) {
        alert("선택하지 않은 QnA가 있어요.");
        return false;
    } else {
        qna.submit();
    }
})

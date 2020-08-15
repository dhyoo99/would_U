// next, back 처리
var first_view = document.getElementById("first_signup");
var second_view = document.getElementById("second_signup");
var next = document.getElementById("next");
var back = document.getElementById("back");

next.addEventListener("click", () => {
    second_view.style.display = 'block';
    first_view.style.display = 'none';
})

back.addEventListener("click", () => {
    first_view.style.display = 'block';
    second_view.style.display = 'none';
})

// 에러 처리
var error = document.getElementById("error").innerHTML;
var id = document.getElementById("username");
var pw = document.getElementById("password");
var pn = document.getElementById("planetname");

if (error === '중복된 아이디입니다.') {
    id.focus();
} else if (error === '비밀번호가 일치하지 않습니다.') {
    pw.focus();
} else if (error === '중복된 행성 이름입니다.') {
    second_view.style.display = 'block';
    first_view.style.display = 'none';
    pn.focus();
}
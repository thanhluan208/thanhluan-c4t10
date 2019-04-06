var table = document.getElementById("table");
var background = document.getElementById("back-ground");
var back = document.getElementById('back');

// Initial:
back.style.display = 'none';

table.addEventListener('click',function(e){
    back.style.display = 'block';
    background.setAttribute('class', 'scaleTable');
    addHtml = `
        <div id="bottle"></div>
    `;
    background.insertAdjacentHTML('afterbegin', addHtml);
    backButton();
});

var mirror = document.getElementById("mirror");
mirror.addEventListener('click',function(e){
    back.style.display = "block";
    background.setAttribute('class',"scaleMirror");
    backButton();
});
var drawers = document.getElementById("drawers");
drawers.addEventListener('click',function(e){
    console.log("halo");
});
var door = document.getElementById("door");
door.addEventListener('click',function(){
    console.log("door");
});

function backButton() {
    var back = document.getElementById("back");
    back.addEventListener('click', function(e){
        background.removeAttribute('class', 'scaleTable');
        back.style.display = "none";
    })
}
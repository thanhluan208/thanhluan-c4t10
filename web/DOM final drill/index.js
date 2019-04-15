function startClick() {
    btn[0].remove();
}



var song = document.getElementById("song_container");
console.log("helo");
var songs = song.getElementsByClassName("song");
console.log(songs);
for(var i = 0 ; i < songs.length; i++){
    var songss = songs[i];
    var title = songss.getElementsByClassName("title");
    console.log(title[0].textContent);
    var artist = songss.getElementsByClassName("artist");
    console.log(artist[0].textContent);
    var button = songss.getElementsByClassName('btn');
    button[0].addEventListener('click', function(e){
        var btn = e.target;
        var div = btn.parentNode;
        div.remove();
    });
    var edit = songss.getElementsByClassName("edit");
    edit[0].addEventListener("click", function(e){
        var bnt = e.target
        var divv = bnt.parentNode
        var x = divv.getAttribute("song_id")
        console.log(x)
    });
    var more = songss.getElementsByClassName("more")
    more[0].addEventListener("click", function(e){
        var more = e.target;
        var div = more.parentNode;
        var y = div.getAttribute("song_id");
        console.log(y);
        console.log(title[0].textContent);
        console.log(artist[0].textContent);
    });
    
};  
var add = document.getElementById("add")
console.log(add)
add.addEventListener("click", function(){
    var div = document.createElement("div");
    document.body.appendChild(div);
    div.textContent = ("alo alo");
    div.classname = "song";
})
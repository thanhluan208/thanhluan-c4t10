function startClick() {
    alert("start clicked");
}



var btn = document.getElementById('btn');
btn.textContent = "search";
btn.addEventListener("click",function(e){
    console.log(e)
});

var searchBar = document.getElementById("search_bar");
searchBar.style.backgroundColor = "black";
searchBar.style.color = "#ffffff";


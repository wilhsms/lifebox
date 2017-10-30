
function getSearch(e){
    if (e == null || e.keyCode == 13)
        this.window.location = "?page=1&search=" + this.document.getElementById("search").value;
}
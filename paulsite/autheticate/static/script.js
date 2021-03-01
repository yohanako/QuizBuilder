window.onload = initall;
var  saveAnsButton ;
function initall() {
    saveAnsButton=document.getElementById('save_ans')
    saveAnsButton.onclick = save_ans;
}
function save_ans() {
    var ans = $("input:radio[name=name]:checked").val()
    alert("answer submited go next")
    var url = '/save_ans?ans='+ans
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    //  alert(req.responseText)
    }
  };
  req.open("GET", url, true);
  req.send();
}
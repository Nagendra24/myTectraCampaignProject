function myfunction(){
var x = document.getElementById("myBtn");
var x2 = document.getElementById("myBtn2");
if (x.style.display == "none"){
x.style.display = "block";
x2.style.display = "none";
//window.location="http://localhost:8000/home_page/user";
}
}

function myfunction2(){
var x2 = document.getElementById("myBtn2");
var x = document.getElementById("myBtn");
if (x2.style.display == "none"){
x2.style.display = "block";
x.style.display = "none";
//window.location="http://localhost:8000/home_page/group";
}
}

function processAjaxData(response, urlPath){
     document.getElementById("myBtn2").innerHTML = response.html;
     document.title = response.pageTitle;
     window.history.pushState({"html":response.html,"pageTitle":response.pageTitle},"", urlPath);
 }


//function openCity(evt, tabName) {
//    var i, tabcontent, tablinks;
//    tabcontent = document.getElementsByClassName("tabcontent");
//    for (i = 0; i < tabcontent.length; i++) {
//        tabcontent[i].style.display = "none";
//    }
//    tablinks = document.getElementsByClassName("tablinks");
//    for (i = 0; i < tablinks.length; i++) {
//        tablinks[i].className = tablinks[i].className.replace(" active", "");
//    }
//    document.getElementById(tabName).style.display = "block";
//    evt.currentTarget.className += " active";
//}






 $(document).ready(function()
 {
 $('.delete').click(function()
 {
   if(confirm('Are you sure to delete this item'))
   {
   return true;
   }
   else
   {
   return false;
   }
 }
 );
 }
 );

 $(document).ready(function() {
     $('#example').DataTable();
 });

 $(document).ready(function() {
     $('#example2').DataTable();
 });


 $(document).ready(function() {
 $('#modalBodyForm').formValidation({
     framework: 'bootstrap',
     excluded: ':disabled',
     icon: {
         valid: 'glyphicon glyphicon-ok',
         invalid: 'glyphicon glyphicon-remove',
         validating: 'glyphicon glyphicon-refresh'
     },
 });
 });

function toggle(source) {
    checkboxes = document.getElementsByName('infoitems');
    for(var i=0, n=checkboxes.length;i<n;i++) {
      checkboxes[i].checked = source.checked;
    }
  }

function togglehello(source) {
checkboxes = document.getElementsByName('permissionitems');
for(var i=0, n=checkboxes.length;i<n;i++) {
checkboxes[i].checked = source.checked;
}
}


function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("defaultOpen").click();

function validationCheck(){


}
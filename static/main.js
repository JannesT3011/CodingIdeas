
document.getElementById('newbutton').addEventListener('click',
function(){
    var body = document.getElementById("MAIN").classList.add("blur")
    document.querySelector('.popupcontainer').style.display = 'flex';

}); // this control the new button  to open up the popup form 

document.querySelector('.close').addEventListener('click',
function(){
    var body = document.getElementById("MAIN").classList.remove("blur")
    document.querySelector('.popupcontainer').style.display = 'none';
}); //  this close the popup form 
const newProjectBtn = document.querySelector('.addNew')
const popup = document.querySelector('.popupcontainer')
const cross = document.querySelector('.cross')

newProjectBtn.addEventListener('click', () => {
    popup.style.display = "block"
})

cross.addEventListener('click', () => {
    popup.style.display = "none"
})
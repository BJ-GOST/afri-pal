// Logout Button
let showBtn = document.querySelector("#logout");
let div = document.querySelector(".logout-div");
let hideBtn = document.querySelector('.hide-btn');
showBtn.addEventListener('click', () => {
    if (div.style.display === 'none') {
        div.style.display = 'flex';
    } else {
        div.style.display = 'none';
    }
});
hideBtn.addEventListener('click', () => {
    div.style.display = 'none';
})



// Floating div for new jobs script
let showButton = document.querySelectorAll(".view-details");
let hideButton = document.querySelector(".hide--div-btn");
let floatingDiv = document.querySelector(".floating-container");

for (let i = 0; i <= showButton.length - 1; i++) {
    showButton[i].addEventListener('click', () => {
        if (floatingDiv.style.display === 'none') {
            floatingDiv.style.display = 'flex';
        } else {
            floatingDiv.style.display = 'none';
        }
    })
};
hideButton.addEventListener('click', () => {
    floatingDiv.style.display = 'none';
});
// 




//floating div for pending jobs
let showDiv = document.querySelectorAll('.view-div');
let closeDiv = document.querySelector('.hide-div-btn');
let pendingDiv = document.querySelector('.floating-pending-container');
for (let j = 0; j <= showDiv.length - 1; j++) {
    showDiv[j].addEventListener('click', () => {
        if (pendingDiv.style.display === 'none') {
            pendingDiv.style.display = 'flex';
        } else {
            pendingDiv.style.display = 'none';
        }
    })
}
closeDiv.addEventListener('click', () => {
    pendingDiv.style.display = 'none';
});
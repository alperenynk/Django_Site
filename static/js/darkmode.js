const body = document.querySelector("body");
const darkButton = document.querySelector(".bb8-toggle__checkbox");
const header = document.querySelector(".header");
const p1 = document.querySelector("#p1");
const p2 = document.querySelector("#p2");
const p3 = document.querySelector("#p3");
const p4 = document.querySelector("#p4");
const p5 = document.querySelector("#p5");
const p6 = document.querySelector("#p6");
const p7 = document.querySelector("#p7");
const p8 = document.querySelector("#p8");

darkButton.addEventListener("click", () => {
    darkButton.classList.toggle("dark");
    if (darkButton.classList.contains("dark")) {
        body.style.backgroundColor = "#222831";
        body.style.color = "#ffffff";
        header.style.backgroundColor = "#222831";
        p1.style.color = "#f0f0f0";
        p2.style.color = "#f0f0f0";
        p3.style.color = "#f0f0f0";
        p4.style.color = "#f0f0f0";
        p5.style.color = "#f0f0f0";
        p6.style.color = "#f0f0f0";
        p7.style.color = "#f0f0f0";
        p8.style.color = "#f0f0f0";
    } else {
        body.style.backgroundColor = "#fff";
        body.style.color = "#212529";
        header.style.backgroundColor = "#fff";
        p1.style.color = "#212529";
        p2.style.color = "#212529";
        p3.style.color = "#212529";
        p4.style.color = "#212529";
        p5.style.color = "#212529";
        p6.style.color = "#212529";
        p7.style.color = "#212529";
        p8.style.color = "#212529";
    }
});

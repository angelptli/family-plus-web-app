const faqquestions = document.querySelectorAll(".question");

faqquestions.forEach((faqquestion) => {
    faqquestion.addEventListener("click", event => {
        const currentActiveQuestion = document.querySelector(".question.active");
        if(currentActiveQuestion && currentActiveQuestion!==faqquestion) {
            currentActiveQuestion.classList.toggle("active");
            currentActiveQuestion.nextElementSibling.style.maxHeight = 0;
        }


        faqquestion.classList.toggle("active");
        const faqanswer = faqquestion.nextElementSibling;
        if(faqquestion.classList.contains("active")) {
            faqanswer.style.maxHeight = faqanswer.scrollHeight + "px";
        }
        else {
            faqanswer.style.maxHeight = 0;
        }

    });
});
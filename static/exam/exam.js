if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

function classPageMenu(button) {
    var active = [
        "bg-violet-100",
        "text-gray-900",
        "border-b-2",
        "border-primary",
        "rounded-t",
    ];
    var examPage = document.getElementById("examPage");
    var peoplePage = document.getElementById("peoplePage");
    var settingsPage = document.getElementById("settingsPage");
    var examButton = document.getElementById("examButton");
    var peopleButton = document.getElementById("peopleButton");
    var settingsButton = document.getElementById("settingsButton");
    if (button === "exams") {
        examPage.classList.remove("hidden");
        examPage.classList.add("block");
        peoplePage.classList.remove("block");
        peoplePage.classList.add("hidden");
        settingsPage.classList.remove("block");
        settingsPage.classList.add("hidden");
        examButton.classList.add(...active);
        peopleButton.classList.remove(...active);
        settingsButton.classList.remove(...active);
    } else if (button === "people") {
        examPage.classList.remove("block");
        examPage.classList.add("hidden");
        peoplePage.classList.remove("hidden");
        peoplePage.classList.add("block");
        settingsPage.classList.remove("block");
        settingsPage.classList.add("hidden");
        examButton.classList.remove(...active);
        peopleButton.classList.add(...active);
        settingsButton.classList.remove(...active);
    } else if (button === "settings") {
        examPage.classList.remove("block");
        examPage.classList.add("hidden");
        peoplePage.classList.remove("block");
        peoplePage.classList.add("hidden");
        settingsPage.classList.remove("hidden");
        settingsPage.classList.add("block");
        examButton.classList.remove(...active);
        peopleButton.classList.remove(...active);
        settingsButton.classList.add(...active);
    }
}

function profileheaderModal() {
    var profileModal = document.getElementById("profileheadermodal");
    if (profileModal.classList.contains("block")) {
        profileModal.classList.remove("block");
        profileModal.classList.add("hidden");
    } else {
        profileModal.classList.remove("hidden");
        profileModal.classList.add("block");
    }
}

function logoutModal() {
    var logoutButton = document.getElementById("logoutmodal");
    if (logoutButton.classList.contains("block")) {
        logoutButton.classList.remove("block");
        logoutButton.classList.add("hidden");
    } else {
        logoutButton.classList.remove("hidden");
        logoutButton.classList.add("block");
    }
}

function createclassModal() {
    var createclass = document.getElementById("createclassmodal");
    if (createclass.classList.contains("block")) {
        createclass.classList.remove("block");
        createclass.classList.add("hidden");
    } else {
        createclass.classList.remove("hidden");
        createclass.classList.add("block");
    }
}

function joinclassModal() {
    if (
        typeof document.getElementById("notjoinedsection") != undefined &&
        document.getElementById("notjoinedsection") != null
    ) {
        var class_code = document.getElementById("classcodeprefilled").value;
        console.log(class_code);
        document.getElementById("class_code").value = class_code;
    }
    var joinclass = document.getElementById("joinclassmodal");
    if (joinclass.classList.contains("block")) {
        joinclass.classList.remove("block");
        joinclass.classList.add("hidden");
    } else {
        joinclass.classList.remove("hidden");
        joinclass.classList.add("block");
    }
}

function deleteclassModal() {
    var deleteclassButton = document.getElementById("deleteclassmodal");
    if (deleteclassButton.classList.contains("block")) {
        deleteclassButton.classList.remove("block");
        deleteclassButton.classList.add("hidden");
    } else {
        deleteclassButton.classList.remove("hidden");
        deleteclassButton.classList.add("block");
    }
}

function copyClassCode() {
    var copyText = document.getElementById("classcode");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    var copyanimation = ["fa-regular", "fa-copy"];
    var tickanimationclasses = [
        "fa-solid",
        "fa-circle-check",
        "origin-bottom",
        "animate-bounce",
        "transition",
        "duration-1000",
        "ease-in-out",
    ];

    var copyicon = document.getElementById("copyclasscodeicon");
    copyicon.classList.remove(...copyanimation);
    copyicon.classList.add(...tickanimationclasses);
    setTimeout(function () {
        copyicon.classList.remove(...tickanimationclasses);
        copyicon.classList.add(...copyanimation);
    }, 2000);
}

function createexamModal() {
    var createexam = document.getElementById("createexammodal");
    if (createexam.classList.contains("block")) {
        createexam.classList.remove("block");
        createexam.classList.add("hidden");
    } else {
        createexam.classList.remove("hidden");
        createexam.classList.add("block");
    }
}

function createQuestionModal(qid) {
    var title = document.getElementById("createquestiontitle");
    if (qid === undefined) {
        title.innerHTML = "Create New Question";
        document.getElementById("action").value = "createquestion";
        document.getElementById("question").value = "";
        document.getElementById("option1").value = "";
        document.getElementById("option2").value = "";
        document.getElementById("option3").value = "";
        document.getElementById("option4").value = "";
    } else {
        title.innerHTML = "Edit Question";
        document.getElementById("action").value = "updatequestion";

        document.getElementById("question").value = document.getElementById(
            "q" + qid
        ).innerHTML;
        document.getElementById("questiontype").value = document.getElementById(
            "qtype" + qid
        ).innerHTML;
        changeQuestionType();
        if (
            document.getElementById("qtype" + qid).innerHTML === "SingleMCQ" ||
            document.getElementById("qtype" + qid).innerHTML === "MultipleMCQ"
        ) {
            for (var i = 0; i < 4; i++) {
                var option = document.getElementsByClassName(qid + "answer")[i]
                    .innerHTML;
                document.getElementById("option" + (i + 1)).value = option;
            }
        }
    }

    var createquestion = document.getElementById("createquestionmodal");
    if (createquestion.classList.contains("block")) {
        createquestion.classList.remove("block");
        createquestion.classList.add("hidden");
    } else {
        createquestion.classList.remove("hidden");
        createquestion.classList.add("block");
    }
}

function changeQuestionType() {
    var qtype = document.getElementById("questiontype").value;
    var truefalseblock = document.getElementById("truefalseblock");
    var mcqblock = document.getElementById("mcqblock");
    var subjectiveblock = document.getElementById("subjectiveblock");
    if (qtype === "SingleMCQ") {
        for (var i = 1; i < 5; i++) {
            document
                .getElementById("option" + i + "iscorrect")
                .setAttribute("type", "radio");
            document
                .getElementById("option" + i + "iscorrect")
                .setAttribute("name", "optioniscorrect");
            document.getElementById("option" + i + "iscorrect").required = true;
            document.getElementById("option" + i).required = true;
        }
        truefalseblock.classList.remove("block");
        truefalseblock.classList.add("hidden");
        mcqblock.classList.remove("hidden");
        mcqblock.classList.add("block");
        subjectiveblock.classList.remove("block");
        subjectiveblock.classList.add("hidden");
    } else if (qtype === "MultipleMCQ") {
        for (var i = 1; i < 5; i++) {
            document
                .getElementById("option" + i + "iscorrect")
                .setAttribute("type", "checkbox");
            document
                .getElementById("option" + i + "iscorrect")
                .setAttribute("name", "option" + i + "iscorrect");
            document.getElementById(
                "option" + i + "iscorrect"
            ).required = false;
            document.getElementById("option" + i).required = true;
        }
        truefalseblock.classList.remove("block");
        truefalseblock.classList.add("hidden");
        mcqblock.classList.remove("hidden");
        mcqblock.classList.add("block");
        subjectiveblock.classList.remove("block");
        subjectiveblock.classList.add("hidden");
    } else if (qtype === "TrueFalse") {
        truefalseblock.classList.remove("hidden");
        truefalseblock.classList.add("block");
        mcqblock.classList.remove("block");
        mcqblock.classList.add("hidden");
        subjectiveblock.classList.remove("block");
        subjectiveblock.classList.add("hidden");
        for (var i = 1; i < 5; i++) {
            document.getElementById(
                "option" + i + "iscorrect"
            ).required = false;
            document.getElementById("option" + i).required = false;
        }
    } else if (qtype === "Subjective") {
        truefalseblock.classList.remove("block");
        truefalseblock.classList.add("hidden");
        mcqblock.classList.remove("block");
        mcqblock.classList.add("hidden");
        subjectiveblock.classList.remove("hidden");
        subjectiveblock.classList.add("block");
        for (var i = 1; i < 5; i++) {
            document.getElementById(
                "option" + i + "iscorrect"
            ).required = false;
            document.getElementById("option" + i).required = false;
        }
    }
}

function deletequestionModal(qid) {
    var deletequestion = document.getElementById("deletequestionmodal");
    if (deletequestion.classList.contains("block")) {
        deletequestion.classList.remove("block");
        deletequestion.classList.add("hidden");
    } else {
        deletequestion.classList.remove("hidden");
        deletequestion.classList.add("block");
        document.getElementById("deletequestionid").value = qid;
    }
}

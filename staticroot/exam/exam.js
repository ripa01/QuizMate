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

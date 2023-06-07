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

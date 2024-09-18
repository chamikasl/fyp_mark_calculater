function validateForm() {

    var rmit = parseFloat(document.getElementById("rmit").value);
    var cis = parseFloat(document.getElementById("cis").value);
    var sppm = parseFloat(document.getElementById("sppm").value);
    var errorMessage = document.getElementById("error-message");

    if (isNaN(rmit) || isNaN(cis) || isNaN(sppm)) {
        errorMessage.textContent = "Please enter valid numbers for all fields.";
        return false;
    }

    if (rmit < 0 || rmit > 100 || cis < 0 || cis > 100 || sppm < 0 || sppm > 100) {
        errorMessage.textContent = "Marks must be between 0 and 100.";
        return false;
    }

    errorMessage.textContent = "";
    return true;
}

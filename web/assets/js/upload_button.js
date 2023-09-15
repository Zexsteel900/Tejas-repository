const inputUploadFile = document.getElementById("image-upload");
inputUploadFile.onchange = function () {
    imageUploadInput.src = URL.createObjectURL(inputUploadFile.files[0]);
}
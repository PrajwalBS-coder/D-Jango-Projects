// const previewImage = () => {
//     const fileInput = document.getElementById('img');
//     const file = fileInput.files[0];
//     console.log(file)
//     const imgTag = document.getElementById('outputimg');

//     const reader = new FileReader();
//     reader.onload = () => {
//         imgTag.src = reader.result;
//         console.log("Done")
//     };
//     reader.readAsDataURL(file);
// };

// document.getElementById('img').addEventListener('change', previewImage);
// console.log('Hello')
// const previewImage = () => {
//     const fileInput = document.getElementById('img');
//     const file = fileInput.files[0];
//     const imgTag = document.getElementById('outputimg');

//     if (file) {
//         const reader = new FileReader();
//         reader.onload = () => {
//             imgTag.src = reader.result; // Replace the current image's source
//             console.log("New image loaded");
//         };
//         reader.readAsDataURL(file);
//     } else {
//         console.log("No file selected");
//     }
// };

// document.getElementById('img').addEventListener('change', previewImage);

document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.getElementById("img");
    const imgTag = document.getElementById("outputimg");

    fileInput.addEventListener("change", () => {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = () => {
                imgTag.src = reader.result;
            };
            reader.readAsDataURL(file);
        } else {
            console.log("No file selected");
        }
    });
});


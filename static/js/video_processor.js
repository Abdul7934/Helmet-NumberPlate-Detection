document.addEventListener('DOMContentLoaded', () => {
    const videoInput = document.getElementById('video');
    const uploadButton = document.querySelector('button[type="submit"]');

    uploadButton.addEventListener('click', (e) => {
        if (!videoInput.files.length) {
            e.preventDefault();
            alert("Please select a video file before uploading.");
        }
    });
});

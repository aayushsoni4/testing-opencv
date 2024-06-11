const video = document.getElementById('video');

// Access the device camera and stream to the video element
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing webcam: ", err);
    });

// Periodically capture the current frame from the video element
setInterval(() => {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const dataUrl = canvas.toDataURL('image/jpeg');
    const imageData = dataUrl.split(',')[1];

    Streamlit.setComponentValue({ image: `data:image/jpeg;base64,${imageData}` });
}, 1000);

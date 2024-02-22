if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            const video = document.getElementById('video');
            video.srcObject = stream;
        })
        .catch(error => {
            console.error('Error al acceder a la webcam: ', error);
        });
}

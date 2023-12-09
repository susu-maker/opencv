// // 取得 前鏡頭permission
// const checkForVideoAudioAccess = async () => {
//     try {
//         const cameraResult = await navigator.permissions.query({ name: 'camera' });
//         // The state property may be 'denied', 'prompt' and 'granted'
//         console.log('cameraResult success');
//         console.log(cameraResult);
//         this.isCameraAccessGranted = cameraResult.state !== 'denied';
//         console.log(this.isCameraAccessGranted);
//         const microphoneResult = await navigator.permissions.query({ name: 'microphone' });
//         console.log('microphoneResult success');
//         this.isMicrophoneAccessGranted = microphoneResult.state !== 'denied';
//         console.log('success')
//     } catch(e) {
//         console.log('failed');
//         console.error('An error occurred while checking the site permissions', e);
//     }

//     return true;
//   }
// // 開啟攝像頭
// checkForVideoAudioAccess().then(function(result){
//     if(navigator.mediaDevices.getUserMedia === undefined){
//         console.log('yes');
//     }
//     let constraints = { 
//         audio: !this.isMicrophoneAccessGranted,
//         video: !this.isCameraAccessGranted,
//         // video: {
//         //     // width: 720,height:720,
//         //     facingMode: "user"  //開前鏡頭
//         // } 
//     }
//     navigator.mediaDevices.getUserMedia(constraints)
//         .then(function (stream) {
//             var video = document.querySelector('video');
//             // 旧的浏览器可能没有srcObject
//             if ("srcObject" in video) {
//                 video.srcObject = stream;
//             } else {
//                 //避免在新的浏览器中使用它，因为它正在被弃用。
//                 video.src = window.URL.createObjectURL(stream);
//             }
//             video.onloadedmetadata = function (e) {
//                 video.play();
//             };
//         })
//         .catch(function (err) {
//             console.log('failed');
//             console.log(err.name + ": " + err.message);
//         });
// })
if ("mediaDevices" in navigator && "getUserMedia" in navigator.mediaDevices) {
    // ok, 浏览器支持它
}

async function a(){
    const videoStream = await navigator.mediaDevices.getUserMedia({ video: true });
    console.log(videoStream.state);
    console.log('hahaha2')
};
console.log('hahaha');
a








        


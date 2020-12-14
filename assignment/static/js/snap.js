const webcamElement = document.getElementById('webcam');
const canvasElement = document.getElementById('canvas');
const snapSoundElement = document.getElementById('snapSound');
const webcam = new Webcam(webcamElement, 'user', canvasElement, snapSoundElement);
const formElement = document.getElementById('file-upload-form');
const newElement = document.getElementById('rightdevice');


// Condition for checking up the user device
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
    webcam.start()
   .then(result =>{
      console.log("webcam started");
   })
   .catch(err => {
       console.log(err);
   });
   $('#clickbutton').show();
}
else{
    $('#clickbutton').hide();
    $('#heading').hide();
    newElement.append("Not a right platform to click image");
}


function photo(){
    var picture = webcam.snap();

    webcam.stop();
    // $("#webcam").hide();
    var blob = dataURItoBlob(picture);
    image_name = Math.random().toString(36).substring(7);

    var form_data = new FormData(formElement);
    form_data.append("files", blob, image_name+".jpg");
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/uploadimage");

    // check when state changes, 
    xmlhttp.onreadystatechange = function() {

    if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var bn = xmlhttp.response;
        newElement.innerHTML = '<h2>Image Uploaded Successfully</h2>\
                                <h3>Uploaded Image</h3>\
                                <img src="'+picture+'"/>';
        $("canvas").remove();
        $("video").remove();
        $("#heading").remove();
        $("button").remove();
    }
    }

    xmlhttp.send(form_data);

}


$('#cameraFlip').click(function() {
  webcam.flip();
  webcam.start();
});


function dataURItoBlob(dataURI) {
    // convert base64/URLEncoded data component to raw binary data held in a string
    var byteString;
    if (dataURI.split(',')[0].indexOf('base64') >= 0)
        byteString = atob(dataURI.split(',')[1]);
    else
        byteString = unescape(dataURI.split(',')[1]);

    // separate out the mime component
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

    // write the bytes of the string to a typed array
    var ia = new Uint8Array(byteString.length);
    for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }

    return new Blob([ia], {type:mimeString});
}


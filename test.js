function changeImage(president) {
  const imgElement = document.getElementById("presidentImage");
  if (president == "trump") {
    imgElement.src = "trump.jpg"; // Update the image source for the USA flag
  } else if (president == "biden") {
    imgElement.src = "biden.jpg"; // Update the image source for the UK flag
  }
}

function changeAudio(audio_file_name) {
  const audioElement = document.getElementById("audio");
  audioElement.src = audio_file_name + ".wav";
}

const audioElement = document.getElementById("audio");
var presidentFlag = "-1";
var count = 0;
audioElement.addEventListener("ended", (event) => {
  console.log("hello");
  if (presidentFlag === "-1") {
    changeAudio("d" + count.toString());
    changeImage("trump");
    presidentFlag = "d";
  } else if (presidentFlag === "d") {
    presidentFlag = "j";
    changeAudio("j" + count.toString());
    changeImage("biden");
    count++;
  } else if (presidentFlag === "j") {
    presidentFlag = "d";
    changeAudio("d" + count.toString());
    changeImage("trump");
  }
});

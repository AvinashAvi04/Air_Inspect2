
window.addEventListener("load",()=>{
  let dropArea = document.getElementById('drop-area');
console.log("drop-area",dropArea);

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false);
});

function highlight(e) {
  dropArea.classList.add('highlight');
}

function unhighlight(e) {
  dropArea.classList.remove('highlight');
}

dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
  let dt = e.dataTransfer;
  let files = dt.files;

  handleFiles(files);
}

function handleFiles(files) {
  ([...files]).forEach(uploadFile);
}

function uploadFile(file)
 {
  console.log("file",file);
  let url = 'YOUR_BACKEND_ENDPOINT'; // URL to your backend API that handles the upload
  let formData = new FormData();

  formData.append('file', file);

  fetch(url, {
    method: 'POST',
    body: formData
  })
  .then(() => { /* Handle success */ })
  .catch(() => { /* Handle error */ });
}

})




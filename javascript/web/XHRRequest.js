function sampleRequest() {
   let xhr = new XMLHttpRequest();
   xhr.open("GET", "./XHRRequest.js", true);
   
   /**
    * 0 = unset
    * 1 = opened
    * 2 = headers_received
    * 3 = loading
    * 4 = done
    */
   xhr.onreadystatechange = function () {
       console.log(xhr.readyState);
       console.log(xhr.responseText);
       if (xhr.readyState == 4) {
           document.write(xhr.responseText);
       }
   }

   xhr.send();
}

sampleRequest();
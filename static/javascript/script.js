document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generate-pdf').addEventListener('click', function() {
        let element = document.getElementById('pdf-content');
        setTimeout(function() {
          html2pdf().from(element).save();
        }, 6000);
      });
}); 


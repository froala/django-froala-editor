function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

if (typeof django !== 'undefined' && typeof django.jQuery !== 'undefined') {
  (function ($) {
    $(document).on('formset:added', function (event, $row, formsetName) {
      $row.find('textarea').each(function () {
        var froala_script = this.nextElementSibling.innerText.replace('__prefix__', this.closest('tr').id.split('-')[-1]);
        this.parentElement.innerHTML = this.outerHTML;
        django.jQuery(this.closest('td')).append("<script>" + froala_script + "</script>");
      });
    });
  })(django.jQuery);
}

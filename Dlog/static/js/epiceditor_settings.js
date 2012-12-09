var content = $("#id_content").val();
console.log(content);
if(content == null) {
	content = "# TODO \r\n Writing something use the markdown Syntax";
}

var opts = {
  container: 'epiceditor',
  basePath: '/static/epiceditor',
  clientSideStorage: false,
  localStorageName: 'epiceditor',
  parser: marked,
  file: {
    name: 'epiceditor',
    defaultContent: content,
    autoSave: 100
  },
  useNativeFullscreen : false,
  focusOnLoad: false,
  shortcut: {
    modifier: 18,
    fullscreen: 70,
    preview: 80,
    edit: 79
  }
}
var editor = new EpicEditor(opts);
editor.load();

// Listen the editor change and put value back to the hidden field.
$("#blog_form").submit(function() {
	console.log("This form is going to submit! Save the content.");
	var new_content = editor.exportFile();
	console.log(new_content);
	$("#id_content").val(new_content);
});

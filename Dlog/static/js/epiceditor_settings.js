var content = document.getElementById("content").value;
if(content == null) {
	content = "# TODO \r\n Writing something use the markdown Syntax";
}
console.log(content);

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
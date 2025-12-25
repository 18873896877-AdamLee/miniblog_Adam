//For submit articles
tinymce.init({
    selector: '#content',
    directionality:'ltr',
    language:'zh_CN',
    height:800,
    width:'100%',
    plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            'save table contextmenu directionality emoticons template paste textcolor',
            'codesample markdown',
    ],
     toolbar: 'insertfile undo redo | \
     styleselect | \
     bold italic | \
     alignleft aligncenter alignright alignjustify | \
     bullist numlist outdent indent | \
     link image uploadimage | \
     print preview media fullpage | \
     forecolor backcolor emoticons |
     codesample fontsizeselect fullscreen',
    fontsize_formats: '10pt 12pt 14pt 18pt 24pt 36pt',
    nonbreaking_force_tab: true,
    paste_data_images: true,
    images_upload_handler: function (blobInfo, success, failure) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload-image');
        xhr.setRequestHeader('X-CSRFToken', getCsrfToken());
        xhr.onload = function() {
            if (xhr.status === 200) {
                const json = JSON.parse(xhr.responseText);
                success(json.location);
            } else {
                failure('Image upload failed: ' + xhr.statusText);
            }
        };
        const formData = new FormData();
        formData.append('file', blobInfo.blob(), blobInfo.filename());
        xhr.send(formData);
    },
    setup: function(editor) {
        editor.on('init', function() {
            editor.setMode('markdown');
        });
    }
});

function getCsrfToken() {
    return document.querySelector('meta[name=csrf-token]').getAttribute('content');
}

//For add plugin
tinymce.init({
    selector: '#pluginContent',
    directionality:'ltr',
    language:'zh_CN',
    plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            'save table contextmenu directionality emoticons template paste textcolor',
            'codesample markdown',
    ],
    toolbar: 'insertfile undo redo | \
     styleselect | \
     bold italic | \
     alignleft aligncenter alignright alignjustify | \
     bullist numlist outdent indent | \
     link image | \
     print preview media fullpage | \
     forecolor backcolor emoticons |
     codesample fullscreen',
    paste_data_images: true,
    images_upload_url: '/upload-image',
    images_upload_handler: function (blobInfo, success, failure) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload-image');
        xhr.setRequestHeader('X-CSRFToken', getCsrfToken());
        xhr.onload = function() {
            if (xhr.status === 200) {
                const json = JSON.parse(xhr.responseText);
                success(json.location);
            } else {
                failure('Image upload failed: ' + xhr.statusText);
            }
        };
        const formData = new FormData();
        formData.append('file', blobInfo.blob(), blobInfo.filename());
        xhr.send(formData);
    },
    setup: function(editor) {
        editor.on('init', function() {
            editor.setMode('markdown');
        });
    }
});

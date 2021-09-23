$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  if (status === 'success') {
    console.log(data);
    $('#hello').text(data.hello);
  }
});

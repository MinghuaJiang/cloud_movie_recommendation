
$('#search').keypress(function(event) {
    event.preventDefault();
    if (event.keyCode == 13){



        var url = "http://localhost:5001/api/v1/search/"+$('#search').val()
        $.get(url).done(function(data){
            json = JSON.parse(data)
            $.each(json, function(k,v){
                alert(v.movie_title.text().substr(0,10))
                $('#result').append("<li class='collection-item'>"+v.movie_title.substr(0, 10) + "..."+"</li>")
            })
            $('.awesome-results').show();
        });
    }
})
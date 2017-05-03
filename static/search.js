    var movie_query = new Bloodhound({
      datumTokenizer: Bloodhound.tokenizers.whitespace,
      queryTokenizer: Bloodhound.tokenizers.whitespace,
      // url points to a json file
      //  prefetch:
      local: {{search.query|tojson|safe}}
    });

    // passing in `null` for the `options` arguments will result in the default
    // options being used
    $('.prefetch .typeahead').typeahead(null, {
      name: 'movie_query',
      source: movie_query
    });
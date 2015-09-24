var bloodHound = new Bloodhound({
    datumTokenizer: function (datum) {
        return Bloodhound.tokenizers.whitespace(datum.value);
    },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    remote: {
        url: 'a/?q=%QUERY',
        wildcard: '%QUERY',
        filter: function (data) {
            // Map the remote source JSON array to a JavaScript object array
            return $.map(data.results, function (d) {
                return {
                    value: d
                };
            });
        }
    }
});

// Initialize the Bloodhound suggestion engine
bloodHound.initialize();

// Instantiate the Typeahead UI
$('.typeahead').typeahead(null, {
    display: 'value',
    source: bloodHound.ttAdapter()
});
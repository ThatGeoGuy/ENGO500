// Definitions
var rootURI = 'http://demo.student.geocens.ca:8080/SensorThings_V1.0/';

// callback in a parameter that represents a function to be executed whenever the data is loaded successfully
function getData(path, callback) {
    $.getJSON(path, callback);
}

// Get root directory information
var root;
var things;
var dataStreams;

root = getData(rootURI, function(jsonData) {
    root = jsonData;
	console.log(root);
	
	// Get things on database, display to screen
	things = getData(root.Collections[0].Things.uri, function(jsonData) {
		things = jsonData;
		console.log(things);
		$('#thingsLevel').append($('<div id=thingElement>' + things.Things[0].Description + '</div>').hide().fadeIn(500));
		
		// Get dataStreams for things
		dataStreams = getData( rootURI + things.Things[0].Datastreams["Navigation-Link"], function(jsonData) {
			dataStreams = jsonData;
			console.log(dataStreams);
			// If a thing is clicked, load it's datastreams
			$('#thingElement').click(function() {
					for(var i=0; i< dataStreams.Datastreams.length; i++){
						$('#dataStreamsLevel').append($('<div id=dataStreamElement>' + i + ' ' + dataStreams.Datastreams[i].Description + '</div>').hide().fadeIn(500));
						
					}	
			});

			return dataStreams
		});
		return things;
	});
	return root;
});


console.log("CHEESE");

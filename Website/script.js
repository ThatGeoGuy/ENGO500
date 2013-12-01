var rootURI, root, things, stream; 

$(document).ready(function() {
	// Definitions
	rootURI = 'http://demo.student.geocens.ca:8080/SensorThings_V1.0/';

	$.getJSON(rootURI, function(data) {
		root = data; 
		
		$.getJSON(root.Collections[0].Things.uri,function(data) {
			things = data;
			$('#thingsLevel').prepend($('<div class="thingElement">' + things.Things[0].Description + '</div>').fadeIn(500));

			$.getJSON(rootURI + things.Things[0].Datastreams["Navigation-Link"],function(data) { 
				stream = data; 
				var loaded = false;

				$('.thingElement').click(function() {
					if(!loaded) { 
						for(var i = 0; i < stream.Datastreams.length; ++i) {
							$('#streamsLevel').append($(
								'<li><div class="streamElement">' + 
								stream.Datastreams[i].Description + 
								'</div></li>').fadeIn(500));
							loaded = true;
						} 
					} else { 
						$('li').fadeOut(500,function() {
							$(this).remove()
						});
						loaded = false;
					}
				});
			});
		});
	}); 
});

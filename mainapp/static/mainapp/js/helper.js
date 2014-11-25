window.HELPER = (function () {
    function HELPER () {
         
    }

    /* AJAX STUFF */
    // using jQuery
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}

    function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	function sameOrigin(url) {
	    // test that a given url is a same-origin URL
	    // url could be relative or scheme relative or absolute
	    var host = document.location.host; // host + port
	    var protocol = document.location.protocol;
	    var sr_origin = '//' + host;
	    var origin = protocol + sr_origin;
	    // Allow absolute or scheme relative URLs to same origin
	    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
	        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
	        // or any other URL that isn't scheme relative or absolute i.e relative.
	        !(/^(\/\/|http:|https:).*/.test(url));
	}
     
    var HELPER = {
        post: function(url, data, success, failure) {
        	/* CRSF */
   //      	$.ajaxSetup({
			//     beforeSend: function(xhr, settings) {
			//         if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
			//             // Send the token to same-origin, relative URLs only.
			//             // Send the token only if the method warrants CSRF protection
			//             // Using the CSRFToken value acquired earlier
			//             var csrftoken = getCookie('csrftoken');
			//             console.log(csrftoken);
			//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
			//         }
			//     }
			// });

			// $.ajaxSetup({ 
			// 	beforeSend: function(xhr, settings) {
			// 		function getCookie(name) {
			// 		 var cookieValue = null;
			// 		 if (document.cookie && document.cookie != '') {
			// 		     var cookies = document.cookie.split(';');
			// 		     for (var i = 0; i < cookies.length; i++) {
			// 		         var cookie = jQuery.trim(cookies[i]);
			// 		         // Does this cookie string begin with the name we want?
			// 		     if (cookie.substring(0, name.length + 1) == (name + '=')) {
			// 		         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
			// 		         break;
			// 		     }
			// 		 }
			// 		}
			// 		return cookieValue;
			// 		}
			// 		if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
			// 		 // Only send the token to relative URLs i.e. locally.
			// 		 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			// 		}
			// 	} 
			// });
			// $.ajaxSetup({
			// 	data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
			// });
			
			data.csrfmiddlewaretoken = getCookie('csrftoken');
			
			/* AJAX REQUEST */
    		$.ajax({
			    url: url,
			    data: data,
			    type: 'POST',
			    success: function(data) {
			    	console.log(data);
			    	success(data);
			    },
			    failure: function(data) { 
			    	failure(data);
			    }
			}); 
    	},
    	post_upload: function(url, data, success, failure) {
        	/* CRSF */
        	data.csrfmiddlewaretoken = getCookie('csrftoken');

        	$.ajaxSetup({
			    beforeSend: function(xhr, settings) {
			        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
			            // Send the token to same-origin, relative URLs only.
			            // Send the token only if the method warrants CSRF protection
			            // Using the CSRFToken value acquired earlier
			            var csrftoken = getCookie('csrftoken');
			            console.log(csrftoken);
			            xhr.setRequestHeader("X-CSRFToken", csrftoken);
			        }
			    }
			});

			/* AJAX REQUEST */
    		$.ajax({
			    url: url,
			    data: data,
			    type: 'POST',
			    cache: false,
			    processData: false,
			    contentType: false,
			    success: function(data) {
			    	console.log(data);
			    	success(data);
			    },
			    failure: function(data) { 
			    	failure(data);
			    }
			}); 
    	},
    };
     
    return HELPER;
}());
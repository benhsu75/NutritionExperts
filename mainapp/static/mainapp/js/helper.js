window.HELPER = (function () {
    function HELPER () {
         
    }
     
    var HELPER = {
        post: function(url, data, success, failure) {
    		$.ajax({
			    url: url,
			    data: data,
			    type: 'POST',
			    success: function(data) {
			    	success(data);
			    },
			    failure: function(data) { 
			    	failure(data);
			    }
			}); 
    	}
    };
     
    return HELPER;
}());
//
//	jQuery Validate example script
//
//	Prepared by David Cochran
//
//	Free for your use -- No warranties, no guarantees!
//

$(document).ready(function(){

	// Validate
	// http://bassistance.de/jquery-plugins/jquery-plugin-validation/
	// http://docs.jquery.com/Plugins/Validation/
	// http://docs.jquery.com/Plugins/Validation/validate#toptions

		$('#contact-form').validate({
	    rules: {
	      title: {
	        minlength: 2,
	        required: true
	      },
	      autocomplete: {
	        required: true
	      },
	      password: {
	      	required: true,
	      	password: true
	      },
	        username: {
	        minlength: 2,
	        username: true,
	        required: true
	      },
	      author: {
	        minlength: 2,
	        required: true
	      },
	      isbn: {
	      	isbn: true,
	        required: true
	      },
	      name: {
	        minlength: 2,
	        required: true
	      },
	      email: {
	        required: true,
	        email: true
	      },
	      subject: {
	      	minlength: 2,
	        required: true
	      },
	      message: {
	        minlength: 2,
	        required: true
	      }
	    },
			highlight: function(element) {
				$(element).closest('.form-group').removeClass('has-success').addClass('has-error');
			},
			success: function(element) {
				element
				.text('OK!').addClass('valid')
				.closest('.form-group').removeClass('has-error').addClass('has-success');
			}
	  });

}); // end document.ready
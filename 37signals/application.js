<script>

	alert('hello world');
$(document).ready(function(){
	  $(this).on("click",function(){
	  	$(this).text("hi");
	  });
	  $('#hr').on('mouseenter',function(){
	    $(this).find('#Headline').text('Highrise remembers the important things about people you’d normally forget.');
		$('#subHeadline').text('Keep a permanent record of people you do business with. Know who you talked to, when you talked to them, what was said, and when to follow up next. Over 20,000,000 contacts are 
		    		tracked using Highrise.');
		    });
	   $('#cf').on('mouseenter',function(){
	     $(this).find('#Headline').text('Basecamp remembers the important things about people you’d normally forget.');
		$('#subHeadline').text('Keep a permanent record of people you do business with. Know who you talked to, when you talked to them, what was said, and when to follow up next. Over 20,000,000 contacts are 
		    		tracked using Highrise.');
		    });
		});
</script>

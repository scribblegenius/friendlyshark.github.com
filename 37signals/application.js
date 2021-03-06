$(document).ready(function(){
	  
		function reset(){
		$('#Headline').removeClass('smaller').text('Making collaboration productive and enjoyable for people every day.');
		$('#arrow').removeClass();
		$('#subHeadline').text('Frustration-free web-based apps for collaboration, sharing information, and making decisions.');
		    };
	   var apos = "'"; 

	  $('#bc').on('mouseenter',function(){
	    $('#Headline').text('Basecamp is the project management tool you wish you had on your last project.');
	    $('#arrow').removeClass().addClass('arrowbc');
	    $('#Headline').toggleClass('smaller');
		$('#subHeadline').text("Are you still managing projects with email? Are you still using Excel for your to-do lists? It"+ apos +"s time to upgrade to Basecamp. Manage projects and collaborate with your team and clients the modern way.");
		    });
	  $('#hr').on('mouseenter',function(){
	    $('#Headline').text("Highrise remembers the important things about people you"+ apos +"d normally forget.");
	    $('#arrow').removeClass().addClass('arrowhr');
	    $('#Headline').toggleClass('smaller');
		$('#subHeadline').text('Keep a permanent record of people you do business with. Know who you talked to, when you talked to them, what was said, and when to follow up next. Over 20,000,000 contacts are tracked using Highrise.');
		    });
	    $('#cf').on('mouseenter',function(){
	    $('#Headline').text('From near or far, Campfire helps teams work together over the web in real-time');
		$('#arrow').removeClass().addClass('arrowcf');
	    $('#Headline').toggleClass('smaller');
		$('#subHeadline').text("Share ideas, discussions, concepts, images, code samples, videos, mockups, and documents in a real-time private chat room. It"+ apos +"s game changing. We couldn"+ apos +"t run our own business without Campfire.");
		    });
	    $('.apps').find('div').on('mouseleave',reset);
	});
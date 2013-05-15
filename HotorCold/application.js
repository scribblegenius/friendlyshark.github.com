$(document).ready(function(){
	var randomnumber = -1;
    var userguess =-1;
    function setRandom()
    {
    	if(randomnumber == -1)
    		randomnumber = Math.floor(Math.random()*101);
    	else
    		randomnumber = -1;
    	$('#test').text(randomnumber);
    }

	$('#playbutton').on('click',function(){ 
		$(this).toggleClass('playclick');
		$('.PlayScreen').slideToggle();
		setRandom();
	});

	$('#submit').on('click',function(){ 
		userguess = $('#UserGuessTextBox').val();
		$('#test').text(randomnumber+" "+userguess);
	});



});
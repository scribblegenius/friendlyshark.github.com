$(document).ready(function(){
	var randomnumber = -1;
    var userguess =-1;
    var prevuserguess = -1;
    var tries =0;
    function InitializeGame()
    {
    	tries=0;
    	userguess =-1;
    	prevuserguess = -1;
    	AnnounceStatus("Guess the numer :D!");
    	if(randomnumber == -1)
    	{
    		randomnumber = Math.floor(Math.random() * 101) + 1;
    	}
    	else
    	{
    		randomnumber = -1;
    	}
    }
    function CheckUserGuess(guess)
    {
    	tries++;
    	prevuserguess = userguess;
    	userguess = guess;
    	display(prevuserguess + " " + userguess + " " + randomnumber);
    	if(userguess == randomnumber){
    		if(tries == 1)
    		{
    			AnnounceStatus("God? Is that you? ...er..Guess again? ");
    		}
    		else if(tries > 5)
    		{
    			AnnounceStatus("Victory in " +tries +" attempts!! Guess again? ");
    		}
    		else
    		{
    			AnnounceStatus("Victory in " +tries +" attempts!! You are good!Guess again? ");
    		}
    		InitializeGame();
    	}
    	else if(Math.abs(randomnumber-userguess) < Math.abs(randomnumber - prevuserguess))
    	{
    		AnnounceStatus("Hot!( Attempt "+tries);
    	}
    	else
    	{
    		AnnounceStatus("Cold!( Attempt "+tries);
    	}
    }

	function AnnounceStatus(text)
	{
		$('#Announce').text(text);
	}
	function display(text)
	{
		$('#test').text(text);
	}
	$('#playbutton').on('click',function(){ 
		$(this).toggleClass('playclick');
		$('.PlayScreen').slideToggle();
		InitializeGame();
	});

	$('#submit').on('click',function(){ 
		CheckUserGuess($('#UserGuessTextBox').val());
	});



});
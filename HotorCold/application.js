$(document).ready(function(){
	var randomnumber = -1;
    var userguess =-1;
    var prevuserguess = -1;
    var tries =0;
	AnnounceStatus("Guess the number :D!");
    function InitializeGame()
    {
    	tries=0;
    	userguess =-1;
    	prevuserguess = -1;
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
    			AnnounceStatus("God? Is that you? ...er..Guess again?( Just to be sure it's you hehe :D ) ");
    		}
    		else if(tries > 5)
    		{
    			AnnounceStatus("Victory in " +tries +" attempts!! Guess again? ");
    		}
    		else
    		{
    			AnnounceStatus("Victory in " +tries +" attempts!! You are good!Guess again? ");
    		}
    	}
    	else if(Math.abs(randomnumber-userguess) < Math.abs(randomnumber - prevuserguess))
    	{
    		if(randomnumber-userguess < 65)
    			AnnounceStatus("Kinda Warm! Attempt "+tries);
    		else if(randomnumber-userguess < 45)
    			AnnounceStatus("Warm! Attempt "+tries);
    		else if(randomnumber-userguess < 25)
    			AnnounceStatus("Warmer! Attempt "+tries);
    		else if(randomnumber-userguess < 15)
    			AnnounceStatus("Hotter! Attempt "+tries);
    		else if(randomnumber-userguess < 10)
    			AnnounceStatus("Red Hot! Attempt "+tries);
    		else if(randomnumber-userguess < 5)
    			AnnounceStatus("Surface of the Sun Hot!! Attempt "+tries);
    		else if(randomnumber-userguess < 3)
    			AnnounceStatus("Everything is melting!! Attempt "+tries);
    		else if(randomnumber-userguess < 2)
    			AnnounceStatus("Cant.Take.Heat.End this already!! Attempt "+tries);
    		else if(randomnumber-userguess < 2)
    			AnnounceStatus("Heat beyond human cognition! Attempt "+tries);
    		else
    			AnnounceStatus("Lukewarm! Attempt "+tries);
    	}
    	else
    	{
    		if(randomnumber-userguess > 65)
    			AnnounceStatus("North Pole cold!! Attempt "+tries);
    		else if(randomnumber-userguess > 45)
    			AnnounceStatus("Freezing cold! Attempt "+tries);
    		else
    			AnnounceStatus("Colder! Attempt "+tries);
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
$(document).ready(function(){
	var randomnumber = -1;
    var userguess =-1;
    var prevuserguess = 0;
    var tries =0;
	AnnounceStatus("Guess the number :D!");
    function InitializeGame()
    {
    	tries=0;
    	userguess =-1;
    	prevuserguess = 0;
    	if(randomnumber == -1)
    	{
    		randomnumber = (Math.floor(Math.random() * 101) + 1);
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
    	var diff1 = randomnumber-userguess;
    	var diff2 = randomnumber-prevuserguess;
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
    		InitializeGame();
    	}
    	else if(Math.abs(diff1) < Math.abs(diff2))
    	{
    	
    		AnnounceStatus("Hotter! Attempt "+tries);
    		// if( diff1 < 65)
    		// 	AnnounceStatus("Kinda Warm! Attempt "+tries);
    		// else if( diff1 < 45)
    		// 	AnnounceStatus("Warm! Attempt "+tries);
    		// else if( diff1 < 25)
    		// 	AnnounceStatus("Warmer! Attempt "+tries);
    		// else if( diff1 < 15)
    		// 	AnnounceStatus("Hotter! Attempt "+tries);
    		// else if( diff1 < 10)
    		// 	AnnounceStatus("Red Hot! Attempt "+tries);
    		// else if(diff1 < 5)
    		// 	AnnounceStatus("Surface of the Sun Hot!! Attempt "+tries);
    		// else if( diff1 < 3)
    		// 	AnnounceStatus("Everything is melting!! Attempt "+tries);
    		// else if( diff1 < 2)
    		// 	AnnounceStatus("Cant.Take.Heat.End this already!! Attempt "+tries);
    		// else if(diff1 < 2)
    		// 	AnnounceStatus("Heat beyond human cognition! Attempt "+tries);
    			
    	}
    	else
    	{

    		// if(diff1 > 65)
    		// 	AnnounceStatus("North Pole cold!! Attempt "+tries);
    		// else if(diff1 > 45)
    		// 	AnnounceStatus("Freezing cold! Attempt "+tries);
    		// else
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
$(document).ready(function(){
	var randomnumber = -1;
    var userguess =-1;
    var prevuserguess = -1;
    function InitializeGame()
    {
    	userguess =-1;
    	prevuserguess = -1;
    	if(randomnumber == -1)
    	{
    		randomnumber = Math.floor(Math.random()*101);
    	}
    	else
    	{
    		randomnumber = -1;
    	}
    }
    function CheckUserGuess(guess)
    {
    	prevuserguess = userguess;
    	userguess = guess;
    	if(userguess == randomnumber){
    		AnnounceStatus("Victory! You guessed it right! Guess again? ");
    		InitializeGame();
    	}
    	else if(Math.abs(randomnumber-userguess) > Math.abs( randomnumber - prevuserguess))
    	{
    		AnnounceStatus("Hot!");
    	}
    	else
    	{
    		AnnounceStatus("Cold!");
    	}

    }
	function AnnounceStatus(text)
	{
		$('#Announce').text(text);
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
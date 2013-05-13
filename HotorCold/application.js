$(document).ready(function(){
	$('#playbutton').on('click',function(){ 
		$(this).toggleClass('playclick');
		$(this).find().closest('.PlayScreen').toggleClass('PlayScreenShow').slideDown();
	});
});
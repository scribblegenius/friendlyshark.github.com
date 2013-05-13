$(document).ready(function(){
	$('#playbutton').on('click',function(){ 
		$(this).toggleClass('playclick');
		$('.PlayScreen').removeClass().toggleClass('PlayScreenShow').slideDown();
	});
});
$(document).ready(function(){
	$('#playbutton').on('click',function(){ 
		$(this).toggleClass('playclick');
		$(this).find().closest('.PlayArea').toggleClass('PlayAreaShow').slideDown();
	});
});
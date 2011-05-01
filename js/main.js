$(document).ready(function(){
	$('.toggle').click(function() {
		var id = $(this).attr('data-target');
		$('#' + id).toggle('slow');
		return false;
	});
 });

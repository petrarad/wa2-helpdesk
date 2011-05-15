$(document).ready(function(){
	$('.toggle').click(function() {
		var id = $(this).attr('data-target');
		$('#' + id).toggle('slow');
		return false;
	});

	$('.toggle-edit').click(function() {
		var id = $(this).attr('data-target');
		$('#' + id + '-data').toggle();
		$('#' + id + '-form').toggle();

		var msg = $(this).html();
		$(this).html($(this).attr('data-alt'));
		$(this).attr('data-alt', msg);
		return false;
	});
	
	$('.confirmSubmit').submit(function(){
		return confirm('Are you sure?');
	})
 });

/* global $ */
// Ensure the DOM is fully loaded before trying to manipulate it
$(document).ready(function () {
  // When the add_item div is clicked, add a new list item
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  // When the remove_item div is clicked, remove the last list item
  $('#remove_item').click(function () {
    $('.my_list li:last').remove();
  });

  // When the clear_list div is clicked, remove all list items
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});

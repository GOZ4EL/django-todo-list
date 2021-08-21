from django.test import TestCase
from django.urls import reverse

from . models import TodoListItem

class TodoAppView(TestCase):
    def test_view_todo_items_list_is_showed(self):
        """The items in the todo list items are showed on the main page."""
        todoitem = TodoListItem.objects.create(content="Test Item.")
        response = self.client.get('/todoapp/')
        self.assertQuerysetEqual(response.context['all_items'], [todoitem])

    def test_view_new_item_is_added(self):
        """
        A new item is added to the todo list item whenever a 
        post request is made to the '/addTodoItem/' dir.
        """
        content = "Test Content"
        self.client.post('/addTodoItem/', {'content': content})
        response = self.client.get('/todoapp/')
        self.assertContains(response, content)

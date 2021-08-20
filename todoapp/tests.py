from django.test import TestCase
from django.urls import reverse

from . models import TodoListItem

class TodoAppView(TestCase):
    def test_view_todo_items_list_is_showed(self):
        todoitem = TodoListItem.objects.create(content="Test Item.")
        response = self.client.get('/todoapp/')
        self.assertQuerysetEqual(response.context['all_items'], [todoitem])

    def test_view_new_item_is_showed(self):
        content = "Test Content"
        self.client.post('/addTodoItem/', {'content': content})
        response = self.client.get('/todoapp/')
        self.assertContains(response, content)

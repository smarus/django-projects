from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        todo_ = request.POST.get('todo')
        important_ = request.POST.get('important')
        if todo_ not in self.all_todos:
            if important_:
                self.all_todos = [todo_] + self.all_todos
            else:
                self.all_todos = self.all_todos + [todo_]

        return redirect('/')

from django.views import View
from django.shortcuts import render
from _collections import deque
from django.views.generic import TemplateView
from django.http.response import HttpResponse, Http404

entries = {"change_oil": "Change oil",
           "inflate_tires": "Inflate tires",
           "diagnostic": "Get diagnostic test"}

ticket_number = 1
line_of_cars = {}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(TemplateView):
    template_name = 'tickets/menu_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entries'] = entries
        return context


#  initial_value = {'key ': 'value'}

#  def get(self, request, *args, **kwargs):
#   return render(request, 'tickets/menu_view.html', {'value': self.initial_value})
class GetTicketView(View):

    def get(self, request, ticket_type, *args, **kwargs):
        global ticket_number
        if ticket_type not in entries.keys():
            raise Http404()

        total = self.count_time()
        tickets = []
        context = {"ticket_number": ticket_number,
                   "time": total}
        tickets.append(ticket_number)
        if ticket_type not in line_of_cars:
            line_of_cars[ticket_type] = tickets
        else:
            tickets = line_of_cars[ticket_type]
            tickets.append(ticket_number)
        ticket_number += 1
        print(tickets)
        return render(request, 'tickets/get_ticket.html', {'ticket': context})

    def count_time(self):
        total = 0
        for key, value in line_of_cars.items():
            if key == 'change_oil':
                total += len(value) * 2
            elif key == 'inflate_tires':
                total += len(value) * 5
            elif key == 'diagnostic':
                total += len(value) * 30
        return total

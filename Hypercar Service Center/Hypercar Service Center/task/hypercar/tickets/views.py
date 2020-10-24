from django.views import View
from django.shortcuts import render, redirect
from _collections import deque
from django.views.generic import TemplateView
from django.http.response import HttpResponse, Http404

entries = {"change_oil": "Change oil",
           "inflate_tires": "Inflate tires",
           "diagnostic": "Get diagnostic test"}

ticket_number = 1
next_ticket = 0
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

        total = self.count_time(ticket_type)
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
        print(tickets, 'tickets', ticket_type)
        print(line_of_cars, 'line_of_cars')
        return render(request, 'tickets/get_ticket.html', {'ticket': context})

    def count_time(self, ticket_type):
        total = 0
        #  for key, value in line_of_cars.items():
        #     if key == 'change_oil':
        #        total += len(value) * 2
        #     elif key == 'inflate_tires':
        #        total += len(value) * 5
        #    elif key == 'diagnostic':
        #        total += len(value) * 30

        if ticket_type == 'change_oil':
            if ticket_type in line_of_cars:
                total += len(line_of_cars[ticket_type]) * 2
        elif ticket_type == 'inflate_tires':
            if 'change_oil' in line_of_cars:
                total += len(line_of_cars['change_oil']) * 2
            if ticket_type in line_of_cars:
                total += len(line_of_cars[ticket_type]) * 5
        else:
            if 'change_oil' in line_of_cars:
                total += len(line_of_cars['change_oil']) * 2
            if 'inflate_tires' in line_of_cars:
                total += len(line_of_cars['inflate_tires']) * 5
            if ticket_type in line_of_cars:
                total += len(line_of_cars[ticket_type]) * 30

        return total


class ProcessingView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}
        self.next_number = 0

    def get(self, request, *args, **kwargs):
        for key, value in line_of_cars.items():
            self.context[key] = len(value)
        return render(request, 'tickets/processing_view.html',
                      {'data': self.context})

    def post(self, request, *args, **kwargs):
        next_number = 0
        global next_ticket

        if 'change_oil' in line_of_cars and len(line_of_cars['change_oil']) > 0:
            next_ticket = line_of_cars['change_oil'].pop(0)
        elif 'inflate_tires' in line_of_cars and len(line_of_cars['inflate_tires']) > 0:
            next_ticket = line_of_cars['inflate_tires'].pop(0)
        elif 'diagnostic' in line_of_cars and len(line_of_cars['diagnostic']) > 0:
            next_ticket = line_of_cars['diagnostic'].pop(0)
        print(line_of_cars, 'line of cars')
        request.session['next_number'] = next_number
        return redirect('/next', *args, **kwargs)


class NextView(View):
    def get(self, request, *args, **kwargs):
        next_number = request.session.get('next_number', 0)
        print(next_ticket,'NextView')
        if next_number != 0:
            del (request.session['next_number'])
        return render(request, 'tickets/next_view.html', {'next_ticket': next_ticket})

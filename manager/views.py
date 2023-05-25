import json
from http import HTTPStatus

import io
import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.files import File
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.views.generic import CreateView, TemplateView
from reportlab.pdfgen import canvas

from manager.forms import (NewUserForm, EventForm, ContractForm, MaintenanceForm)
from manager.models import Event, TenantContract, MaintenanceRequest
from django.views.generic import FormView


class Home(TemplateView):
    template_name = "home.html"


class Register(CreateView):
    form_class = NewUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class Login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")


class AboutUs(TemplateView):
    template_name = "about-us.html"


class EventFormView(LoginRequiredMixin, FormView):
    template_name = "event-new.html"
    form_class = EventForm
    success_url = reverse_lazy('event-new')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Events(LoginRequiredMixin, TemplateView):
    template_name = "events.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        events = Event.objects.all().filter(date__gte=timezone.now()).order_by("date")
        images = ["images/green.jpg", "images/rose.jpg", "images/blue.jpg"]
        context["next_events"] = [(image, event) for image, event in zip(images, events[:3])]
        context["events"] = events
        return context


class MaintenanceFormView(LoginRequiredMixin, FormView):
    template_name = "maintenance-new.html"
    form_class = MaintenanceForm
    success_url = reverse_lazy('maintenance-new')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.creation_date = timezone.now()
        form.save()
        return super().form_valid(form)


class MaintenanceRequests(LoginRequiredMixin, TemplateView):
    template_name = "maintenance-requests.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        maintenance_requests = MaintenanceRequest.objects.all().filter(status="False").order_by("-relevance")
        context["maintenance_requests"] = maintenance_requests
        return context


class MaintenanceStatus(LoginRequiredMixin, TemplateView):
    template_name = "maintenance-status.html"
    success_url = reverse_lazy('maintenance-requests')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        maintenance_request = MaintenanceRequest.objects.get(id=self.kwargs["pk"])
        context["maintenance_request"] = maintenance_request
        return context


# Class Contract IS NOT WORKING, it doesn't cause problems but it doesn't work
class Contract(LoginRequiredMixin, FormView):
    template_name = "get-contract.html"
    form_class = ContractForm

    def post(self, request, *args, **kwargs):
        try:
            body = json.loads(self.request.body)
        except:
            return JsonResponse({"status": "error", "content": "Unexpected format"}, status=HTTPStatus.BAD_REQUEST)

        user_name = parse_date(body.get('user_name'))
        if not user_name:
            return JsonResponse({"status": "error", "content": "Invalid user name"}, status=HTTPStatus.BAD_REQUEST)

        pdf_buffer = self._generate_pdf_contract()
        contract_uuid = uuid.uuid4()
        TenantContract.objects.create(
            uuid=contract_uuid,
            client=self.request.user,
            file=File(pdf_buffer, name=f"{contract_uuid}.pdf")
        )

        return JsonResponse({"status": "success", "content": {"contract downloaded"}})

    def _generate_pdf_contract(self) -> io.BytesIO:
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(50, 800, "EVENTS AND MORE")
        p.drawString(200, 700, "STAND RESERVATION CONTRACT")

        user = self.request.user
        p.drawString(100, 500, "Reservation made by: " + str(user))
        p.drawString(100, 480, "Entity contact email address: " + str(user.email))

        p.drawString(100, 440, "The payment is to be made by bank transfer. If the payment is not done in 7 ")
        p.drawString(100, 420, "days the reservation will be canceled.")

        p.drawString(100, 380, "If need of cancellation, the client must contact the event organizer.")

        p.drawString(100, 340, "The parties agree to follow the city hall, Catalan, and Spanish laws.")

        p.drawString(470, 50, "Page 1 of 1.")
        p.showPage()
        p.save()
        buffer.seek(0)
        return buffer

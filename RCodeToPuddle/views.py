from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from django.shortcuts import redirect

from RCodeToPuddle.forms import RCodeForm, RCodeScreenshotForm


class RCodePuddleView(TemplateView):
    template_name = "puddle-options.html"

    # def post(self, request, *args, **kwargs):
    #     redirect()


class RCodeTextView(FormView):
    template_name = "puddle-text-input.html"
    form_class = RCodeForm

    def form_valid(self, form):
        return HttpResponseRedirect(reverse("puddle-link", args=[form.get_puddle_id(), "txt"]))

    def validate(self):
        ...


class RCodeImageView(FormView):
    template_name = "screenshot-to-puddle.html"
    form_class = RCodeScreenshotForm

    def form_valid(self, form):
        if (rcode_id := form.get_puddle_id()) is not None:
            return HttpResponseRedirect(reverse("puddle-link", args=[rcode_id, "img"]))
        else:
            return HttpResponseRedirect(reverse("img-search-failed"))


class PuddleFoundView(TemplateView):
    template_name = "puddle-found.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ID As hex with leading "0x" removed, and uppercase to match puddle's conventions
        puddle_rcode_id = hex(int(context['id']))[2:].upper()

        context["puddle_url"] = f"https://puddle.farm/player/{puddle_rcode_id}"

        return context


class RcodeNotFoundView(TemplateView):
    template_name = "rcode-id-not-found.html"

# Create your views here.

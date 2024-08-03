from django.urls import path, register_converter

from .converters import RCodeIDPuddleConverter, TextOrImageConverter
from .views import PuddleFoundView, RCodeTextView, RCodeImageView, RCodePuddleView, RcodeNotFoundView

register_converter(RCodeIDPuddleConverter, "rcode_id_puddle")
register_converter(TextOrImageConverter, "text_or_image")

urlpatterns = [
    path("puddle", RCodePuddleView.as_view(), name="puddle-id-options"),

    path("puddle/from/text", RCodeTextView.as_view(), name="text-to-puddle"),
    path("puddle/from/img", RCodeImageView.as_view(), name="img-to-puddle"),
    path("puddle/at/<rcode_id_puddle:id>/<text_or_image:search_type>", PuddleFoundView.as_view(), name="puddle-link"),

    path("unknown", RcodeNotFoundView.as_view(), name="img-search-failed"),
]

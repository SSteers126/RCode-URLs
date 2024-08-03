from django import forms

import re

from const import TERMINATED_RCODE_ID_REGEX
from utils.get_rcode_id.game_screenshot.image_preperation import prepare_screenshot


class RCodeForm(forms.Form):
    id = forms.IntegerField(min_value=100000000000000000, max_value=999999999999999999)

    def get_puddle_id(self) -> str:

        # Cut the '0x' from the hex value
        return self.cleaned_data["id"]


class RCodeScreenshotForm(forms.Form):
    rcode_img = forms.ImageField(required=True)
    def get_puddle_id(self) -> str | None:

        rcode_id_read = prepare_screenshot(self.cleaned_data["rcode_img"])

        return rcode_id_read if TERMINATED_RCODE_ID_REGEX.match(rcode_id_read) is not None else None

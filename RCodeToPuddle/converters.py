from const import RCODE_ID_PATTERN


class RCodeIDPuddleConverter:
    regex = RCODE_ID_PATTERN

    def to_python(self, value):
        # Raises ValueError on its own, so errors are already covered by django
        return int(value)

    # Converts the number from the R-Code to the Hex string used by Puddle
    def to_url(self, value):
        # Sliced to remove the "0x" prefix supplied by python, and upper to match puddle's conventions
        # print(value)
        return value
        # return hex(int(value))[2:].upper()


class TextOrImageConverter:
    regex = "(img)|(txt)"

    def to_python(self, value):
        return value

    # Converts the number from the R-Code to the Hex string used by Puddle
    def to_url(self, value):
        return value
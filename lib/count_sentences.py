import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self) -> bool:
        """Returns True if the value ends with a period."""
        return self._value.endswith(".")

    def is_question(self) -> bool:
        """Returns True if the value ends with a question mark."""
        return self._value.endswith("?")

    def is_exclamation(self) -> bool:
        """Returns True if the value ends with an exclamation mark."""
        return self._value.endswith("!")

    def count_sentences(self) -> int:
        """Counts the number of valid sentences in the value."""
        sentences = re.split(r"[.!?]+", self._value.strip())
        return len([s for s in sentences if s.strip()])  # Avoid counting empty segments

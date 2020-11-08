import abc

from jinja2 import Environment, FileSystemLoader, select_autoescape


class BaseGenerator(metaclass=abc.ABCMeta):
    def __init__(self, **kwargs):
        self.jinja_env = Environment(
            loader=FileSystemLoader(searchpath="./templates"),
            autoescape=select_autoescape(["html", "xml"]),
        )

    @abc.abstractmethod
    def generate(self):
        pass

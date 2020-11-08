from .base import BaseGenerator


class PythonGenerator(BaseGenerator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate(self):
        template = self.jinja_env.get_template("python/main")
        return template.render()

# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE


class Model:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = []

    def create(self, item):
        self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View:
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for item in self.model.objects:
            item_template = self.template
            for field in self.model.fields:
                if field in item:
                    item_template = item_template.replace("{{" + field + "}}", item[field])
            output += item_template
        return output


# CONTROLLER: Routes messages
class Controller:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        return self.routes[path].render()


# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()


# CREATE AN APPLICATION INSTANCE
app = Application()

# define models (
app.models["user"] = Model("user", ["name", "score"])
app.models["game"] = Model("game", ["game_name", "description"])

# app.models = {
#     "user": Model("user", ["name", "score"]),
#     "game": Model("game", ["game_name", "description"])
# }

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9"},
    {"name": "Carol", "score": "11"},
    {"name": "Ted", "score": "15"},
    {"name": "Alice", "score": "13"}
]

app.models["game"].objects = [
    {"game_name": "Asteroids", "description": "so many rocks."},
]

app.controller.routes = {
    "/scores/": View("\nHello <em>{{name}}</em>, your score is: <strong>{{score}}</strong>.<br>\n",
     app.models["user"]),

    "/game/": View("\nGame: {{game_name}} Desc:{{description}}\n", app.models["game"])
}
# BEGIN TEST
request_path = "/scores/"
write_me = app.controller.route(request_path)
print(write_me)
output_file = open("mvc_output.html", "w")
output_file.write(write_me)
output_file.close()

request_path = "/game/"
write_me = app.controller.route(request_path)
print(write_me)
output_file = open("game.html", "w")
output_file.write(write_me)
output_file.close()

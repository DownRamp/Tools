from plantuml import PlantUML
from os.path import abspath

# create a server object to call for your computations
server = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                          basic_auth={},
                          form_auth={}, http_opts={}, request_opts={})

# Send and compile your diagram files to/with the PlantUML server
server.processes_file(abspath('./example_flow.txt'))
server.processes_file(abspath('./Graphviz_example.txt'))
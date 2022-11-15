import pathlib
import os
from jinja2 import Template

main_dir = pathlib.Path(__file__).parent.resolve()

def read_config(config):
    with open(f"{main_dir}/templates/{config}", "r") as file:
        return file.read()

def create_config(template, vars, name):
    template_data = read_config(template)
    template = Template(template_data)
    configuration_data = template.render(vars)

    output_file = f'{main_dir}/systemd/{name}'
    with open(output_file, 'w') as file:
        file.write(configuration_data)

def copy_and_reload(*args):
    files = ''
    for file in args:
        files += f'{main_dir}/systemd/{file} '
    os.system(f'cp {files} /etc/systemd/system')
    os.system(f'systemctl daemon-reload')

if __name__ == '__main__':
    service_template = 'service.j2'
    timer_template = 'timer.j2'

    service_name = '<name>.service'
    service_vars = {'desc': '<Add Description here>', 
                            'exec': '</path/to/executable/script>'}

    timer_name = '<name>.timer'
    timer_vars = {'desc': '<Add Description here>', 
                          'service': service_name,
                          'time_interval': '00:00:00'}

    create_config(service_template, service_vars, service_name)
    create_config(timer_template, timer_vars, timer_name)
    copy_and_reload(service_name, timer_name)

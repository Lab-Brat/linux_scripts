import pathlib
import os
from jinja2 import Template

main_dir = pathlib.Path(__file__).parent.resolve()


def read_config(config):
    """
    Read Jinja2 template files, return content
    """
    with open(f"{main_dir}/templates/{config}", "r") as file:
        return file.read()


def create_config(filename, template, vars):
    """
    Read Jinja2 temlate, variables and output filename,
    create a configuration file in ./templates
    """
    template = Template(read_config(template))
    configuration_data = template.render(vars)

    with open(f"/etc/systemd/system/{filename}", "w") as file:
        file.write(configuration_data)


def reload():
    """
    Reload systemd.
    """
    os.system(f"sudo systemctl daemon-reload")


if __name__ == "__main__":
    # template names
    service_template = "service.j2"
    timer_template = "timer.j2"

    # service name and variables
    service_name = "test.service"
    service_vars = {"desc": "Test service", "exec": "/home/labbrat/test.sh"}

    # timer name and variables
    timer_name = "test.timer"
    timer_vars = {
        "desc": "Timer for Test service",
        "service": service_name,
        "time_interval": "00:00:00",
    }

    create_config(service_name, service_template, service_vars)
    create_config(timer_name, timer_template, timer_vars)
    reload()

import os
from django.core.management.base import BaseCommand


# Make sure this command is ran before creating any models or performing any migrations.
class Command(BaseCommand):
    help = 'Renames the Django project to Custom name.'

    def add_arguments(self, parser):
        parser.add_arguments('new_project_name', type=str, help=self.help)

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # Logic to rename the project.
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        files_to_rename = ['main/settings/base.py', 'main/wsgi.py', 'manage.py']
        folder_to_rename = 'main'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            filedata = filedata.replace('main', new_project_name)
            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)
        self.stdout.write(self.style.SUCCESS('Project has been successfully renamed to %s. Make sure you rename the \'main\' folder in the \'templates\' and \'static\' folders. %(new_project_name)))


from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Esse command foi previamente feito por CHQ308"

    def handle(self, *args, **options):
        self.stdout.write("Commands okOK")  # msg
        self.stdout.write(self.style.SUCCESS("Commands okOK"))  # sucesso
        self.stdout.write(self.style.WARNING("Commands okOK"))  # warning
        self.stdout.write(self.style.ERROR("Commands okOK"))  # erro
        self.stderr.write("Erro")  # erro
        

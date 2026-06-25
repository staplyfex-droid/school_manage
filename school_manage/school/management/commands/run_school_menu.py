from django.core.management.base import BaseCommand
from school_manage.models import Subject, Teacher, Class, Student, Schedule, Grade
from datetime import datetime

class Command(BaseCommand):
    help = 'Run the school menu'

    def handle(self, *args, **options):
        while True:
            self.stdout.write("\n" + "="*40)
            self.stdout.write("      СИСТЕМА КЕРУВАННЯ ШКІЛЬНИМ РОЗКЛАДОМ      ")
            self.stdout.write("="*40)
            self.stdout.write("1. Додати предмет")
            self.stdout.write("2. Додати вчителя")
            self.stdout.write("3. Додати клас")
            self.stdout.write("4. Додати учня")
            self.stdout.write("5. Додати заняття в розклад (Додатково)")
            self.stdout.write("6. Додати оцінку (Додатково)")
            self.stdout.write("0. Вихід")
            self.stdout.write("-"*40)
            
            choice = input("Оберіть дію: ").strip()

            if choice == '1':
                self.add_subject()

            elif choice == '2':
                self.add_teacher()


    def add_subject(self):
        self.stdout.write("\n--- Додавання предмету ---")
        title = input("Введіть назву предмету: ").strip()
        description = input("Введіть опис предмету: ").strip()

        if not title:
            self.stdout.write("Назва предмету не може бути порожньою.")
            return
        if Subject.objects.filter(name__iexact=title).exists():
            self.stdout.write("Предмет з такою назвою вже існує.")
            return
        Subject.objects.create(name=title, description=description)
        self.stdout.write("Предмет успішно додано.")

    def add_teacher(self):
        self.stdout.write("\n--- Додавання вчителя  ---")
        input_name = input("Введіть ім'я вчителя: ").strip()
        input_subject =input("Введіть предмет, який викладає вчитель: ").strip()
        input_email = input("Введіть email вчителя: ").strip()

        if not input_name:
            self.stdout.write("\n Поле не може бути пустим")
            return
        try: 
            subject = Subject.objects.get(name__iexact=input_subject)  
        except Subject.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Помилка: Предмет '{input_subject}' не знайдено! Спочатку додайте предмет."))
            return
        Teacher.objects.create(name=input_name, email=input_email, subject=subject)
        self.stdout.write(self.style.SUCCESS(f"Вчителя '{input_name}' успішно додано."))

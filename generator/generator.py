from data.data import Person,RegistrationPerson
from faker import Faker
import random

faker_ru = Faker('ru_RU')


def generated_person():
    yield Person(

        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )

def generated_registration_person():
    yield RegistrationPerson(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=faker_ru.random_int(min=18, max=65), 
        salary=random.randint(30000,150000),
        department=faker_ru.random_element(elements=("IT", "HR", "Маркетинг", "Финансы", "Продажи")),
    )
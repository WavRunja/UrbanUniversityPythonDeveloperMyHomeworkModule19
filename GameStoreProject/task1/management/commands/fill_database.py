from django.core.management.base import BaseCommand
from task1.models import Buyer, Game


class Command(BaseCommand):
    help = 'Выполните команду python manage.py fill_database, чтобы заполнить базу данных согласно условию задачи'

    def handle(self, *args, **kwargs):
        # Покупатели
        buyer1 = Buyer.objects.create(name="Ilya", balance=1500.05, age=24)
        buyer2 = Buyer.objects.create(name="Terminator2000", balance=42.15, age=52)
        buyer3 = Buyer.objects.create(name="Ubivator432", balance=0.5, age=16)

        # Игры
        game1 = Game.objects.create(title="Cyberpunk 2077", cost=31, size=46.2, description="Game of the year",
                                    age_limited=True)
        game2 = Game.objects.create(title="Mario", cost=5, size=0.5, description="Old Game", age_limited=False)
        game3 = Game.objects.create(title="Hitman", cost=12, size=36.6, description="Who kills Mark?", age_limited=True)

        # Проверка возрастного ограничения
        def add_buyers_to_game(game, buyers):
            # Проверка покупателя на возрастные ограничения
            eligible_buyers = [buyer for buyer in buyers if not (game.age_limited and buyer.age < 18)]

            if eligible_buyers:
                game.buyer.set(eligible_buyers)
                print(f"Покупатели {[buyer.name for buyer in eligible_buyers]} добавлены к игре {game.title}.")
            else:
                print(f"Ни один покупатель не соответствует возрастному требованию для игры {game.title}.")

        # Назначение игр покупателям
        add_buyers_to_game(game1, [buyer1, buyer2, buyer3])
        add_buyers_to_game(game2, [buyer2, buyer3])
        add_buyers_to_game(game3, [buyer1, buyer2, buyer3])

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена'))

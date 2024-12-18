from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=1000, decimal_places=2)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=100, decimal_places=2)
    size = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')


# >>> Buyer.objects.create(name = 'Tom', balance = '1000.15', age = '55')
# >>> Buyer.objects.create(name = 'Tom', balance = '105', age ='15')
# >>> Game.objects.create(title = 'Game1', cost = '100', size = '5', description = 'game nuber 1')
# >>> Game.objects.create(title = 'Game2', cost = '10', size = '15', description = 'game number 2', age_limited = True)
# >>> Game.objects.create(title = 'Game3', cost = '100', size = '0.7', description = 'game number 3', age_limited = True)
# >>> b1 = Buyer.objects.get(id=1)
# >>> b1 = Buyer.objects.get(id=1)
# >>> b2 = Buyer.objects.get(id=2)
# >>> b3 = Buyer.objects.get(id=3)
# >>> Game.objects.get(id=1).buyer.set((b1, b2, b3))
# >>> Game.objects.get(id=2).buyer.set((b1, b3))
# >>> Game.objects.get(id=3).buyer.set((b1, b1))



class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
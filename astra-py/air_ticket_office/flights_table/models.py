from django.db import models

class f_table(models.Model):
    # direction = models.CharField("Наименование направления",max_length=200, default="", blank=True)
    company_name = models.CharField("Наименование авиакомпании",max_length=200, default="", blank=True)
    # f_name = models.CharField("Наименование рейса",max_length=200, default="", blank=True)
    f_from = models.CharField("Откуда рейс",max_length=200, default="", blank=True)
    f_to = models.CharField("Куда рейс",max_length=200, default="", blank=True)
    when_f = models.DateTimeField("Дата/время вылета", default=None, null=True, blank=True)
    when_t = models.DateTimeField("Дата/время прилета", default=None, null=True, blank=True)
    seats = models.IntegerField("Количество свободных мест", default=0, blank=True)
    passangers = models.IntegerField("Количество зарег.пассажиров", default=0, blank=True)
    aircraft_type = models.CharField("Тип ВС", max_length=200, default="", blank=True)

    def __str__(self):
        return f"({self.company_name}) {self.f_from} - {self.f_to}: {self.when_f}"
    
    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"

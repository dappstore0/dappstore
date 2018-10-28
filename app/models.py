from django.db import models

ratings = [(r, r) for r in range(0, 6)]


class Dapp(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000, null=True, blank=True)  # submission owner
    status = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    homepage = models.CharField(max_length=1000)
    icon = models.CharField(max_length=1000, null=True, blank=True)
    blockchain = models.CharField(max_length=1000)
    current_fund = models.IntegerField(default=0)
    fund_next_stage = models.IntegerField(default=10)
    days_to_go = models.IntegerField(default=10)


class State(models.Model):
    key = models.CharField(max_length=1000, primary_key=True)
    value = models.IntegerField()


class Feedback(models.Model):
    dapp = models.ForeignKey(Dapp, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    rating = models.CharField(max_length=1, choices=ratings, default=0)

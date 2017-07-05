from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ibm(models.Model):
    date = models.CharField(max_length=20, blank=True, primary_key=True)
    aggregate_sentiment = models.FloatField(blank=True, null=True)
    open_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    sentiment_variation = models.FloatField(blank=True, null=True)
    stock_variation = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "IBM"

    class Meta:
        db_table = 'ibm'


class Tesla(models.Model):
    date = models.CharField(max_length=20, blank=True, primary_key=True)
    aggregate_sentiment = models.FloatField(blank=True, null=True)
    open_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    sentiment_variation = models.FloatField(blank=True, null=True)
    stock_variation = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "TESLA"

    class Meta:
        db_table = 'tesla'


class United(models.Model):
    date = models.CharField(max_length=20, blank=True, primary_key=True)
    aggregate_sentiment = models.FloatField(blank=True, null=True)
    open_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    sentiment_variation = models.FloatField(blank=True, null=True)
    stock_variation = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "UAL (United Airlines)"

    class Meta:
        db_table = 'united'


class Snap(models.Model):
    date = models.CharField(max_length=20, blank=True, primary_key=True)
    aggregate_sentiment = models.FloatField(blank=True, null=True)
    open_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    sentiment_variation = models.FloatField(blank=True, null=True)
    stock_variation = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "Snap Inc."

    class Meta:
        db_table = 'snap'


class American(models.Model):
    date = models.CharField(max_length=20, blank=True, primary_key=True)
    aggregate_sentiment = models.FloatField(blank=True, null=True)
    open_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    sentiment_variation = models.FloatField(blank=True, null=True)
    stock_variation = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "American Airlines"

    class Meta:
        db_table = 'american'


class Correlation(models.Model):
    company = models.CharField(max_length=20, blank=True, primary_key=True)
    pearson = models.FloatField(blank=True, null=True)
    spearman = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correlation'
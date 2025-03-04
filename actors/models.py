from random import choice
from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'United States of America'),
    ('UK', 'United Kingdom'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('JP', 'Japan'),
    ('CN', 'China'),
    ('KR', 'South Korea'),
    ('IN', 'India'),
    ('BR', 'Brazil'),
    ('RU', 'Russia'),
    ('AU', 'Australia'),
    ('CA', 'Canada'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('MX', 'Mexico'),
    ('ID', 'Indonesia'),
    ('TR', 'Turkey'),
    ('SA', 'Saudi Arabia'),
    ('IR', 'Iran'),
    ('AR', 'Argentina'),
    ('ZA', 'South Africa'),
    ('NG', 'Nigeria'),
    ('EG', 'Egypt'),
    ('PK', 'Pakistan'),
    ('BD', 'Bangladesh'),
    ('PH', 'Philippines'),
    ('VN', 'Vietnam'),
    ('TH', 'Thailand'),
    ('MY', 'Malaysia'),
    ('NL', 'Netherlands'),
    ('BE', 'Belgium'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('AT', 'Austria'),
)


class Actor(models.Model):
    name = models.CharField(max_length=120)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES , blank=True, null=True)

    def __str__(self):
        return self.name
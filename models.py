from django.db import models
from datetime import date

STATUS_CHOICES = (
    ('APROVADO', 'Aprovado'),
    ('TRAMITANDO', 'Tramitando'),
    ('REJEITADO', 'Rejeitado'),
    ('VISTA', 'Vista'),
    ('PROTOCOLADO', 'Protocolado')
)

CARGO_CHOICES = (
    ('VEREADOR', 'Vereador'),
    ('PREFEITO', 'Prefeito'),
    ('DEPUTADO ESTADUAL', 'Deputado Estadual'),
    ('DEPUTADO FEDERAL', 'Deputado Federal'),
    ('SENADOR', 'Senador'),
    ('OUTRO', 'Outro')
)

class Tema(models.Model):
    tema = models.CharField(max_length=200)

    def __str__(self):
        return self.tema

class Autor(models.Model):
    class Meta():
        verbose_name_plural = "Autores"

    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES, default='VEREADOR')
    cidade = models.CharField(max_length=200, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    telefone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome

class Natureza(models.Model):
    class Meta():
        verbose_name_plural = "Naturezas"

    nome = models.CharField(max_length=200, blank=True)
    sigla = models.CharField(max_length=200, blank=True)

    def __str__(self):
        if self.sigla:
            return self.sigla
        else:
            return self.nome

class Projeto(models.Model):
    class Meta():
        verbose_name_plural = "Projetos"

    nome = models.CharField(max_length=200)
    ementa = models.CharField(max_length=2000)
    numero_legislativo = models.CharField(max_length=200, blank=True)
    ano_legislativo = models.IntegerField(default=0)
    natureza = models.ForeignKey(Natureza, on_delete=models.CASCADE)
    autor = models.ManyToManyField(Autor, related_name='autor_projeto', blank=True)
    tema = models.ManyToManyField(Tema, related_name='tema_projeto', blank=True, null=True)
    comentario = models.TextField(blank=True)
    cidade = models.CharField(max_length=200, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    situacao = models.CharField(max_length=10, choices=STATUS_CHOICES, default='APROVADO')
    arquivo_url = models.URLField(blank=True)

    def __str__(self):
        return "{} {}/{}".format(self.natureza, self.numero_legislativo, self.ano_legislativo)

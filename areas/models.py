from django.db import models



class Empresas(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=30, blank=False)
    razao_social = models.CharField('Razão social', max_length=50, blank=True, unique=True)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=50, blank=False, unique=True)
    cnpj = models.CharField('Cnpj', max_length=20, blank=True, unique=False)
    inscricao_estadual = models.CharField('Inscrição estadual', max_length=20, blank=True)
    inscricao_municipal = models.CharField('Inscrição municipal', max_length=20, blank=True)
    contato = models.CharField(max_length=30, blank=False)
    telefone = models.CharField(max_length=30, blank=False)
    celular = models.CharField(max_length=30, blank=True)
    email = models.EmailField('E-mail', blank=False)
    site = models.CharField(max_length=50, blank=False)
    cep = models.CharField(max_length=9, blank=True)
    endereco = models.CharField(max_length=40, blank=False)
    numero = models.CharField(max_length=10, blank=False)
    complemento = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=50, blank=False)
    cidade = models.CharField(max_length=50, blank=False)
    uf = models.CharField(max_length=2, blank=False)


    def __str__(self):
        return self.nome_fantasia



# Create your models here.
class Areas(models.Model):
    id = models.AutoField(primary_key=True)
    tag_medidor = models.IntegerField(default=0)
    text = models.TextField(max_length=200)
    empresa = models.ForeignKey(Empresas, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text
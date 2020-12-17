from django.db import models
from stdimage.models import StdImageField
from phone_field import PhoneField
from cpf_field.models import CPFField
from django.contrib.auth.models import User


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Product(Base):
    CHOICES = [
        ('household_appliance', 'Eletrodoméstico'),
        ('electronic', 'Eletrônico'),
        ('food', 'Alimento'),
        ('clean', 'Limpeza'),
        ('beauty', 'Beleza'),
        ('clothing', 'Vestuário'),
        ('intimate_care', 'Cuidado íntimo'),
        ('varied', 'Variados'),
    ]
    name = models.CharField('produto', max_length=100)
    type = models.CharField('Tipo', max_length=20, choices=CHOICES)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    amount = models.IntegerField('Quantidade')
    image = StdImageField('Imagem', variations={'thumb': (124, 124)})

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name


class Client(Base):
    CHOICE = [
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    ]
    full_name = models.CharField('Nome completo', max_length=100)
    date_of_birth = models.DateField('Data de nascimento')
    sex = models.CharField('Sexo', max_length=9, choices=CHOICE)
    phone = PhoneField('Telefone', blank=True)
    email = models.EmailField('E-mail', unique=True, default='')
    cpf = CPFField('CPF', unique=True)
    indebted = models.BooleanField('Devendo?', default=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.full_name


class Sale(models.Model):
    client = models.ForeignKey(Client, related_name='cliente', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='products', blank=True, through='SaleProduct')
    date = models.DateTimeField('Data', auto_now_add=True)
    purchase_type = models.BooleanField('Fiado?', default=False)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['id']

    def __str__(self):
        return f'Compra do cliente {self.client} do tipo {self.purchase_type} com ID {self.pk}'


class SaleProduct(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.PROTECT)
    sale = models.ForeignKey(Sale, related_name='sale', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Produto da compra'
        verbose_name_plural = 'Produtos da compra'

    def __str__(self):
        return f'{self.product} da venda {self.sale}'

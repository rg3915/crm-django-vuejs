# Generated by Django 2.1.2 on 2018-10-12 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('description', models.CharField(max_length=500, verbose_name='descrição')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='data de pagto')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='data de vencimento')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='valor')),
                ('payment', models.BooleanField(default=True, help_text='Á vista ou Parcelado.', verbose_name='Á vista?')),
                ('paid', models.BooleanField(default=True, help_text='O fornecedor foi pago?', verbose_name='Pago?')),
                ('cost_center_paid', models.BooleanField(default=False, help_text='O cliente pagou?', verbose_name='Cliente pagou?')),
                ('payment_cost_center_date', models.DateField(blank=True, null=True, verbose_name='data de pagto do cliente')),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
                ('document_jpg', models.FileField(blank=True, null=True, upload_to='')),
                ('cost_center', models.ForeignKey(help_text='Recebido/Pago ao (cliente)', on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='crm.Company', verbose_name='centro de custo')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('paying_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='crm.Employee', verbose_name='fonte pagadora')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='providers', to='crm.Provider', verbose_name='fornecedor')),
            ],
            options={
                'ordering': ('-payment_date',),
            },
        ),
        migrations.CreateModel(
            name='Repayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='data de vencimento')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repayment_companies', to='crm.Company')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'nota de reembolso',
                'verbose_name_plural': 'notas de reembolso',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='RepaymentItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('repayment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repayments', to='financial.Repayment')),
            ],
            options={
                'verbose_name': 'item da nota de reembolso',
                'verbose_name_plural': 'itens das notas de reembolso',
                'ordering': ('expense__payment_date',),
            },
        ),
        migrations.CreateModel(
            name='TypeExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('title', models.CharField(max_length=70, unique=True, verbose_name='título')),
                ('fixed', models.BooleanField(default=False, help_text='Despesa fixa?', verbose_name='fixa')),
            ],
            options={
                'verbose_name': 'Tipo de Despesa',
                'verbose_name_plural': 'Tipos de Despesas',
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='base',
            name='type_expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.TypeExpense', verbose_name='tipo de despesa'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
                'proxy': True,
                'indexes': [],
            },
            bases=('financial.base',),
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
            ],
            options={
                'verbose_name': 'Recebimento',
                'verbose_name_plural': 'Recebimentos',
                'proxy': True,
                'indexes': [],
            },
            bases=('financial.base',),
        ),
        migrations.AddField(
            model_name='repaymentitems',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.Expense', verbose_name='despesa'),
        ),
    ]
# Generated by Django 4.2.1 on 2023-11-23 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao', models.CharField(max_length=200)),
                ('data_nascimento_criacao', models.DateField(null=True)),
                ('cpf_cnpj', models.CharField(max_length=14)),
                ('tipo', models.CharField(choices=[('U', 'Usuário'), ('C', 'Cliente'), ('P', 'Prestador')], default='C', max_length=1)),
                ('excluido', models.BooleanField(default=False)),
                ('login', models.CharField(default='', max_length=200)),
                ('senha', models.CharField(default='', max_length=200)),
                ('descricao_servico', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custo_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=200)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemLocacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('excluido', models.BooleanField(default=False)),
                ('custo_unitario', models.DecimalField(decimal_places=2, default=' ', max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_pessoas', models.IntegerField()),
                ('data_evento', models.DateField(null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orcamentos', to='GestaoEvento.entidade')),
            ],
        ),
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('rendimento', models.DecimalField(decimal_places=4, max_digits=10)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('sigla', models.CharField(default='', max_length=3)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=30)),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='GestaoEvento.entidade')),
            ],
        ),
        migrations.CreateModel(
            name='PratoIngredienteAux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=4, max_digits=10)),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.ingrediente')),
                ('prato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.prato')),
            ],
        ),
        migrations.AddField(
            model_name='prato',
            name='ingredientes',
            field=models.ManyToManyField(through='GestaoEvento.PratoIngredienteAux', to='GestaoEvento.ingrediente'),
        ),
        migrations.CreateModel(
            name='OrcamentoPrestadorAux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.orcamento')),
                ('prestador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.entidade')),
            ],
        ),
        migrations.CreateModel(
            name='OrcamentoPratoAux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.orcamento')),
                ('prato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.prato')),
            ],
        ),
        migrations.CreateModel(
            name='OrcamentoItemLocacaoAux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('item_locacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.itemlocacao')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.orcamento')),
            ],
        ),
        migrations.AddField(
            model_name='orcamento',
            name='itens_locacao',
            field=models.ManyToManyField(through='GestaoEvento.OrcamentoItemLocacaoAux', to='GestaoEvento.itemlocacao'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='pratos',
            field=models.ManyToManyField(through='GestaoEvento.OrcamentoPratoAux', to='GestaoEvento.prato'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='prestadores',
            field=models.ManyToManyField(through='GestaoEvento.OrcamentoPrestadorAux', to='GestaoEvento.entidade'),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='unidade_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.unidademedida'),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(default='', max_length=8)),
                ('bairro', models.CharField(max_length=200)),
                ('complemento', models.CharField(max_length=200)),
                ('cidade', models.CharField(default='', max_length=200)),
                ('estado', models.CharField(default='', max_length=200)),
                ('excluido', models.BooleanField(default=False)),
                ('principal', models.BooleanField(default=False)),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='GestaoEvento.entidade')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='GestaoEvento.entidade')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_impressao', models.DateField(null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.orcamento')),
            ],
        ),
    ]

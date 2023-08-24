# Generated by Django 4.2.1 on 2023-06-01 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao', models.CharField(max_length=200)),
                ('data_nascimento_criacao', models.DateField(null=True)),
                ('cpf_cnpj', models.CharField(max_length=14)),
                ('tipo', models.CharField(choices=[('U', 'Usuário'), ('C', 'Cliente'), ('P', 'Prestador')], default='C', max_length=1)),
                ('excluido', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custo_unidade', models.DecimalField(decimal_places=2, max_digits=10)),
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
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_pessoas', models.IntegerField()),
                ('data_evento', models.DateField(null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orcamentos', to='GestaoEvento.cliente')),
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
            name='Prestador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao', models.CharField(max_length=200)),
                ('data_nascimento_criacao', models.DateField(null=True)),
                ('cpf_cnpj', models.CharField(max_length=14)),
                ('tipo', models.CharField(choices=[('U', 'Usuário'), ('C', 'Cliente'), ('P', 'Prestador')], default='C', max_length=1)),
                ('excluido', models.BooleanField(default=False)),
                ('descricao_servico', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao', models.CharField(max_length=200)),
                ('data_nascimento_criacao', models.DateField(null=True)),
                ('cpf_cnpj', models.CharField(max_length=14)),
                ('tipo', models.CharField(choices=[('U', 'Usuário'), ('C', 'Cliente'), ('P', 'Prestador')], default='C', max_length=1)),
                ('excluido', models.BooleanField(default=False)),
                ('login', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=30)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='GestaoEvento.cliente')),
                ('prestador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='GestaoEvento.prestador')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='GestaoEvento.usuario')),
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
        migrations.AddField(
            model_name='prato',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.usuario'),
        ),
        migrations.CreateModel(
            name='OrcamentoPrestadorAux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.orcamento')),
                ('prestador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.prestador')),
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
            field=models.ManyToManyField(through='GestaoEvento.OrcamentoPrestadorAux', to='GestaoEvento.prestador'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orcamentos', to='GestaoEvento.usuario'),
        ),
        migrations.AddField(
            model_name='itemlocacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.usuario'),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='unidade_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.unidademedida'),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.usuario'),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=200)),
                ('complemento', models.CharField(max_length=200)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.cidade')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='GestaoEvento.cliente')),
                ('prestador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='GestaoEvento.prestador')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='GestaoEvento.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='GestaoEvento.cliente')),
                ('prestador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='GestaoEvento.prestador')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='GestaoEvento.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_impressao', models.DateField(null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.orcamento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoEvento.estado'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-12-03 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0026_inputsshellandtube_calculation_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calculation_id', models.UUIDField(blank=True, null=True)),
                ('q', models.FloatField(blank=True, null=True)),
                ('R', models.FloatField(blank=True, null=True)),
                ('S', models.FloatField(blank=True, null=True)),
                ('F', models.FloatField(blank=True, null=True)),
                ('mldt', models.FloatField(blank=True, null=True)),
                ('deltaT', models.FloatField(blank=True, null=True)),
                ('Nt', models.FloatField(blank=True, null=True)),
                ('Dotl', models.FloatField(blank=True, null=True)),
                ('Ds', models.FloatField(blank=True, null=True)),
                ('A_proj', models.FloatField(blank=True, null=True)),
                ('Ud_min', models.FloatField(blank=True, null=True)),
                ('area_one_tube', models.FloatField(blank=True, null=True)),
                ('area_tube', models.FloatField(blank=True, null=True)),
                ('Gt', models.FloatField(blank=True, null=True)),
                ('Re_t', models.FloatField(blank=True, null=True)),
                ('tube_velocity', models.FloatField(blank=True, null=True)),
                ('hi', models.FloatField(blank=True, null=True)),
                ('hio', models.FloatField(blank=True, null=True)),
                ('pp', models.FloatField(blank=True, null=True)),
                ('pn', models.FloatField(blank=True, null=True)),
                ('ls', models.FloatField(blank=True, null=True)),
                ('lc', models.FloatField(blank=True, null=True)),
                ('Dc', models.FloatField(blank=True, null=True)),
                ('delta_sb_meters', models.FloatField(blank=True, null=True)),
                ('d_bocal', models.FloatField(blank=True, null=True)),
                ('li', models.FloatField(blank=True, null=True)),
                ('lo', models.FloatField(blank=True, null=True)),
                ('lsi', models.FloatField(blank=True, null=True)),
                ('lso', models.FloatField(blank=True, null=True)),
                ('Sm', models.FloatField(blank=True, null=True)),
                ('theta_b', models.FloatField(blank=True, null=True)),
                ('Scd', models.FloatField(blank=True, null=True)),
                ('delta_tb', models.FloatField(blank=True, null=True)),
                ('Dctl', models.FloatField(blank=True, null=True)),
                ('theta_ctl', models.FloatField(blank=True, null=True)),
                ('Fw', models.FloatField(blank=True, null=True)),
                ('Ntb', models.FloatField(blank=True, null=True)),
                ('Stb', models.FloatField(blank=True, null=True)),
                ('Sbp', models.FloatField(blank=True, null=True)),
                ('Swg', models.FloatField(blank=True, null=True)),
                ('Stw', models.FloatField(blank=True, null=True)),
                ('Sw', models.FloatField(blank=True, null=True)),
                ('Nc', models.FloatField(blank=True, null=True)),
                ('Nss', models.FloatField(blank=True, null=True)),
                ('Ncw', models.FloatField(blank=True, null=True)),
                ('Nb', models.FloatField(blank=True, null=True)),
                ('Gc', models.FloatField(blank=True, null=True)),
                ('Pr_s', models.FloatField(blank=True, null=True)),
                ('ji', models.FloatField(blank=True, null=True)),
                ('h_ideal', models.FloatField(blank=True, null=True)),
                ('Rlm', models.FloatField(blank=True, null=True)),
                ('Rs', models.FloatField(blank=True, null=True)),
                ('jl', models.FloatField(blank=True, null=True)),
                ('Fbp', models.FloatField(blank=True, null=True)),
                ('jb', models.FloatField(blank=True, null=True)),
                ('Ntc', models.FloatField(blank=True, null=True)),
                ('jr', models.FloatField(blank=True, null=True)),
                ('Fc', models.FloatField(blank=True, null=True)),
                ('jc', models.FloatField(blank=True, null=True)),
                ('lsi_s', models.FloatField(blank=True, null=True)),
                ('lso_s', models.FloatField(blank=True, null=True)),
                ('js', models.FloatField(blank=True, null=True)),
                ('hs', models.FloatField(blank=True, null=True)),
                ('T_c', models.FloatField(blank=True, null=True)),
                ('tc', models.FloatField(blank=True, null=True)),
                ('tw', models.FloatField(blank=True, null=True)),
                ('Uc', models.FloatField(blank=True, null=True)),
                ('Us', models.FloatField(blank=True, null=True)),
                ('Rd_calc', models.FloatField(blank=True, null=True)),
                ('A_nec', models.FloatField(blank=True, null=True)),
                ('Ea', models.FloatField(blank=True, null=True)),
                ('delta_Pr', models.FloatField(blank=True, null=True)),
                ('delta_Ptt', models.FloatField(blank=True, null=True)),
                ('delta_PT', models.FloatField(blank=True, null=True)),
                ('fi', models.FloatField(blank=True, null=True)),
                ('delta_Pbi', models.FloatField(blank=True, null=True)),
                ('Rcl', models.FloatField(blank=True, null=True)),
                ('Rcb', models.FloatField(blank=True, null=True)),
                ('delta_Pc', models.FloatField(blank=True, null=True)),
                ('Rcs', models.FloatField(blank=True, null=True)),
                ('delta_Pe', models.FloatField(blank=True, null=True)),
                ('Ntw', models.FloatField(blank=True, null=True)),
                ('Dw', models.FloatField(blank=True, null=True)),
                ('delta_Pwi', models.FloatField(blank=True, null=True)),
                ('delta_Pw', models.FloatField(blank=True, null=True)),
                ('delta_Ps', models.FloatField(blank=True, null=True)),
                ('objective_function_1', models.FloatField(blank=True, null=True)),
                ('objective_function_2', models.FloatField(blank=True, null=True)),
                ('error', models.BooleanField(default=True)),
                ('inputs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.inputsshellandtube')),
            ],
        ),
    ]

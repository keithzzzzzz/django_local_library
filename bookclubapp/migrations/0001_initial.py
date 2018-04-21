# Generated by Django 2.0.4 on 2018-04-19 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addr_id_addr', models.AutoField(primary_key=True, serialize=False)),
                ('addr_line_1_addr', models.CharField(default=' ', max_length=254)),
                ('addr_line_2_addr', models.CharField(blank=True, default=' ', max_length=254)),
                ('city_addr', models.CharField(default=' ', max_length=254)),
                ('state_addr', models.CharField(default=' ', max_length=254)),
                ('zip_code_addr', models.CharField(default=' ', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AuctionItem',
            fields=[
                ('item_id_AI', models.AutoField(default=' ', primary_key=True, serialize=False)),
                ('buyout_price_AI', models.FloatField()),
                ('pub_id_AI', models.CharField(default=' ', max_length=20)),
                ('desc_AI', models.CharField(default=' ', max_length=254)),
                ('quantity_AI', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AuctionStatistics',
            fields=[
                ('week_id_AS', models.IntegerField()),
                ('stat_id_AS', models.IntegerField(primary_key=True, serialize=False)),
                ('num_bids_AS', models.IntegerField()),
                ('total_sales_AS', models.FloatField()),
                ('highest_bid_AS', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('bid_id_bid', models.AutoField(primary_key=True, serialize=False)),
                ('starting_bid', models.IntegerField()),
                ('bid_amount_bid', models.IntegerField()),
                ('username_bid', models.CharField(default=' ', max_length=20)),
                ('item_id_bid', models.IntegerField()),
                ('current_bid_bid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN_book', models.CharField(default=' ', max_length=20, primary_key=True, serialize=False)),
                ('rating_book', models.IntegerField()),
                ('pub_date_book', models.DateField()),
                ('pages_book', models.IntegerField()),
                ('summary_book', models.TextField(default=' ')),
                ('age_group_book', models.CharField(default=' ', max_length=20)),
                ('publisher_book', models.CharField(default=' ', max_length=20)),
                ('author_book', models.CharField(default=' ', max_length=20)),
                ('title_book', models.CharField(default=' ', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('username_BL', models.CharField(default=' ', max_length=20)),
                ('ISBN_BL', models.CharField(default=' ', max_length=20, primary_key=True, serialize=False)),
                ('comments_BL', models.CharField(default=' ', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('cc_id_cc', models.IntegerField(primary_key=True, serialize=False)),
                ('card_name_cc', models.CharField(default=' ', max_length=40)),
                ('exp_date_cc', models.DateField()),
                ('sec_code_cc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('shipping_no_del', models.AutoField(primary_key=True, serialize=False)),
                ('username_del', models.CharField(default=' ', max_length=20)),
                ('item_id_del', models.IntegerField()),
                ('start_date_del', models.DateField()),
                ('end_date_del', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN_genre', models.IntegerField()),
                ('genre_id_genre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GenreList',
            fields=[
                ('genre_id_GL', models.AutoField(primary_key=True, serialize=False)),
                ('genre_name_GL', models.CharField(default=' ', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('item_id_rec', models.IntegerField(primary_key=True, serialize=False)),
                ('stat_id_rec', models.IntegerField()),
                ('week_id_rec', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('register_id_reg', models.AutoField(primary_key=True, serialize=False)),
                ('username_reg', models.CharField(default=' ', max_length=20)),
                ('item_id_reg', models.IntegerField()),
                ('start_date_reg', models.DateField()),
                ('end_date_reg', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Telemarketing',
            fields=[
                ('username_tel', models.CharField(default=' ', max_length=20, primary_key=True, serialize=False)),
                ('week_tel', models.CharField(default=' ', max_length=10)),
                ('addr_id_tel', models.IntegerField()),
                ('email_tel', models.CharField(default=' ', max_length=20)),
                ('gender_tel', models.CharField(default=' ', max_length=20)),
                ('phone_tel', models.CharField(default=' ', max_length=15)),
                ('age_tel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username_user', models.CharField(default=' ', max_length=20, primary_key=True, serialize=False)),
                ('fname_user', models.CharField(default=' ', max_length=20)),
                ('mname_user', models.CharField(default=' ', max_length=20)),
                ('lname_user', models.CharField(default=' ', max_length=20)),
                ('usertype_user', models.CharField(default=' ', max_length=20)),
                ('password_user', models.CharField(default=' ', max_length=20)),
                ('email_user', models.EmailField(default=' ', max_length=254)),
                ('phone_user', models.CharField(default=' ', max_length=15)),
                ('dob_user', models.DateField()),
                ('gender_user', models.CharField(default=' ', max_length=10)),
                ('kpoints_user', models.IntegerField()),
                ('addr_id_user', models.IntegerField()),
                ('cc_id_user', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='telemarketing',
            unique_together={('username_tel', 'week_tel')},
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('week_id_rec', 'item_id_rec')},
        ),
        migrations.AlterUniqueTogether(
            name='booklist',
            unique_together={('username_BL', 'ISBN_BL')},
        ),
        migrations.AlterUniqueTogether(
            name='auctionstatistics',
            unique_together={('week_id_AS', 'stat_id_AS')},
        ),
    ]
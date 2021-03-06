# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    nationality = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'

    def __str__(self):
        return self.name

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Authors, models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey('Genders', models.DO_NOTHING, blank=True, null=True)
    saga = models.ForeignKey('Sagas', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=100)
    num_stars = models.CharField(max_length=1, blank=True, null=True)
    language = models.CharField(max_length=2)
    cover_url = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=128, blank=True, null=True)
    pags = models.PositiveIntegerField(blank=True, null=True)
    favorite = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books'

    def __str__(self):
        return self.title[:25]


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Genders(models.Model):
    gender_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    slug = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genders'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail-gender", kwargs={'id': self.slug})


class Sagas(models.Model):
    author = models.ForeignKey(Authors, models.DO_NOTHING, blank=True, null=True)
    saga_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    slug = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sagas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail-saga", kwargs={'id': self.slug})


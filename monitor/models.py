from django.db import models
from django.utils import timezone

# IP-адрес и количество посещений сайта
class Userip(models.Model):
    ip=models.CharField(verbose_name='Айпи адрес',max_length=30)    #айпи адрес
    count=models.IntegerField(verbose_name='Визиты',default=0) # Ip посещения
    class Meta:
        verbose_name = 'Доступ к информации о пользователе'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

# Всего посещений сайта
class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='Всего посещений сайта',default=0) # Всего посещений сайта
    class Meta:
        verbose_name = 'Всего посещений сайта'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

# Статистика посещений за один день
class DayNumber(models.Model):
    day=models.DateField(verbose_name='свидание',default=timezone.now)
    count=models.IntegerField(verbose_name='Количество посещений сайта',default=0) # Всего посещений сайта
    class Meta:
        verbose_name = 'Статистика ежедневных посещений сайта'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)




class GlobalGroup(models.Model):
	nameGroup = models.CharField("Название группы", max_length = 80)
	configFile = models.FileField("Файл конфигурации для группы", upload_to='files/', null=True, blank=True)
	loginGroup = models.CharField("Логин для микротиков, принадлежащих этой группе", max_length =  30, null=True, blank=True)
	passGroup = models.CharField("Пароль для микротиков, принадлежащих этой группе", max_length = 30, null=True, blank=True)



	def __str__(self):
		return self.nameGroup

	class Meta():
		verbose_name = 'Группу'
		verbose_name_plural = 'Группы'

class Group(models.Model):
	nameGroup = models.CharField("Название подгруппы", max_length = 80)
	configFile = models.FileField("Файл конфигурации для подгруппы", upload_to="files/", null=True, blank=True)
	loginGroup = models.CharField("Логин для микротиков, принадлежащих этой подгруппе", max_length =  30, null=True, blank=True)
	passGroup = models.CharField("Пароль для микротиков, принадлежащих этой подгруппе", max_length = 30, null=True, blank=True)
	belongGroupGlobal = models.ForeignKey(GlobalGroup, on_delete=models.CASCADE, verbose_name='группы', null=True, blank=True)


	def __str__(self):
		return f"{self.belongGroupGlobal}  |  {self.nameGroup}" 
		

	class Meta():
		verbose_name = 'Подгруппу'
		verbose_name_plural = 'Подгруппы'


class Mikrot(models.Model):
	mikrotIP = models.CharField("Адрес Микротик", max_length = 20)
	mikrotName = models.CharField("Имя Микротик", max_length =  30)
	mikrotLogin = models.CharField("Логин Микротик", max_length =  30, null=True, blank=True)
	mikrotPass = models.CharField("Пароль Микротик", max_length = 30, null=True, blank=True)
	belongGroup = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='подгруппы', null=True, blank=True)
	belongGroupGlobal = models.ForeignKey(GlobalGroup, on_delete=models.CASCADE, verbose_name='группы', null=True, blank=True)


	def __str__(self):
		return f"{self.belongGroup} | {self.mikrotName}"

	class Meta():
		verbose_name = 'Микротик'
		verbose_name_plural = 'Микротики'
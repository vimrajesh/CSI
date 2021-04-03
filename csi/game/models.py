from django.db import models

class User(models.Model):
    ragamID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    team_members = models.JSONField(default=None, null=True)
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "RID: "+self.ragamID+"; Name: "+self.name

class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    char1_scndinterro = models.BooleanField(default=False)
    char2_scndinterro = models.BooleanField(default=False)
    char3_scndinterro = models.BooleanField(default=False)
    char4_scndinterro = models.BooleanField(default=False)
    char5_scndinterro = models.BooleanField(default=False)

    def __str__(self):
        return self.user
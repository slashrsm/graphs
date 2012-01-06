from django.db import models

# Create your models here.

class SurveyResponse(models.Model):
    # Basic data
    source = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    role = models.CharField(max_length=200)
    time_using = models.CharField(max_length=200)
    num_projects = models.CharField(max_length=200)
    
    # 1st group - statements about scrum
    scrum_1 = models.IntegerField()
    scrum_2 = models.IntegerField()
    scrum_3 = models.IntegerField()
    scrum_4 = models.IntegerField()
    scrum_5 = models.IntegerField()
    scrum_6 = models.IntegerField()
    scrum_7 = models.IntegerField()
    scrum_8 = models.IntegerField()
    scrum_9 = models.IntegerField()
    scrum_comment = models.TextField()
    
    # 2nd group - importance of factors
    import_1 = models.IntegerField()
    import_2 = models.IntegerField()
    import_3 = models.IntegerField()
    import_4 = models.IntegerField()
    import_5 = models.IntegerField()
    import_6 = models.IntegerField()
    import_7 = models.IntegerField()
    import_8 = models.IntegerField()
    import_9 = models.IntegerField()
    import_10 = models.IntegerField()
    import_11 = models.IntegerField()
    import_12 = models.IntegerField()
    import_13 = models.IntegerField()
    import_comment = models.TextField()
    
    # 3rd group - essay
    essay_adv = models.TextField()
    essay_dis = models.TextField()
    essay_again = models.CharField(max_length=100)
    essay_again_comment = models.TextField()
    
    # 4th group - user stories
    stories_1 = models.IntegerField(null=True)
    stories_2 = models.IntegerField(null=True)
    stories_3 = models.IntegerField(null=True)
    stories_4 = models.IntegerField(null=True)
    stories_5 = models.IntegerField(null=True)
    stories_6 = models.IntegerField(null=True)
    stories_7 = models.IntegerField(null=True)
    stories_8 = models.IntegerField(null=True)
    stories_9 = models.IntegerField(null=True)
    stories_10 = models.IntegerField(null=True)
    stories_11 = models.IntegerField(null=True)
    stories_12 = models.IntegerField(null=True)
    stories_comment = models.TextField()
    
    # 5th group - developer satisfaction
    satis_1 = models.IntegerField(null=True)
    satis_2 = models.IntegerField(null=True)
    satis_3 = models.IntegerField(null=True)
    satis_4 = models.IntegerField(null=True)
    satis_5 = models.IntegerField(null=True)
    satis_6 = models.IntegerField(null=True)
    satis_7 = models.IntegerField(null=True)
    satis_8 = models.IntegerField(null=True)
    satis_9 = models.IntegerField(null=True)
    satis_10 = models.IntegerField(null=True)
    satis_11 = models.IntegerField(null=True)
    satis_12 = models.IntegerField(null=True)
    satis_13 = models.IntegerField(null=True)
    satis_14 = models.IntegerField(null=True)
    satis_15 = models.IntegerField(null=True)
    satis_16 = models.IntegerField(null=True)
    satis_17 = models.IntegerField(null=True)
    
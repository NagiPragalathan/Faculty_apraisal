from django.db import models
import datetime
# Create your models here.

                            # Faculty_details

class Users(models.Model):
    id          = models.IntegerField(primary_key=True)
    user_name   = models.CharField(max_length = 200,unique=True)
    mail_id     = models.CharField(max_length=200,unique=True) 
    password    = models.CharField(max_length = 200,unique=True)
    role        = models.IntegerField()   # roles {1,2,3} 1(Admin), 2(HOD), 3(Staff)

class Faculty_details(models.Model):
    id              = models.IntegerField(primary_key=True)
    user_name   = models.CharField(max_length = 200,unique=True)
    role            = models.ForeignKey(Users, on_delete=models.CASCADE)
    image           = models.ImageField(upload_to='photo/%Y/%m/%d',default='images/Screenshot_3.png')

    id_number       = models.IntegerField()
    name            = models.CharField(max_length = 200,unique=True)
    designation     = models.CharField(max_length = 200,default='designation')
    date_of_join    = models.DateField(default=datetime.datetime.now())
    department      = models.CharField(max_length = 200,default='department')
    qualififcation  = models.CharField(max_length = 200,default='qualififcation')
    assessment_period = models.IntegerField(default=0) # auto update....
    experience      = models.IntegerField(default=0)
    bio             = models.CharField(max_length = 200,default='No Bio yet.')


                            # Internal test evaluation 

class Subjects(models.Model):
    subject_image = models.CharField(max_length = 200)
    subject_name  = models.CharField(max_length = 200,unique=True)
    subject_code  = models.CharField(max_length = 200,unique=True)
    semester = models.IntegerField()
    department = models.CharField(max_length = 200)
    discription = models.CharField(max_length = 200,default='No Discription yet.')

class Subject_handled(models.Model):
    faculty_id    = models.IntegerField()
    subject_staff = models.ForeignKey(Faculty_details, on_delete=models.CASCADE)
    subject_name  = models.CharField(max_length = 200,unique=True)
    subject_code  = models.CharField(max_length = 200,unique=True)
    target_pass   = models.CharField(max_length = 200)
    actual_pass   = models.CharField(max_length = 200)

class Test_evaluation(models.Model):
    subject_detials = models.ForeignKey(Subject_handled, on_delete=models.CASCADE) # it's can be access to subject.name, subject.code
    test            = models.CharField(max_length = 200)
    target_pass     = models.CharField(max_length = 200)
    actual_pass     = models.CharField(max_length = 200)


                                # BLOCK DEPT. ACT
class Guest_lecture(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details  = models.CharField(max_length=200)

class Iv_arrangement(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details  = models.CharField(max_length=200)

class Placement_initiative(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details  = models.CharField(max_length=200)

class Organising_online_offline_fdp(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details  = models.CharField(max_length=200)

class Department_Activities(models.Model):
    guest_lecture = models.ForeignKey(Guest_lecture, on_delete=models.CASCADE)
    Iv_arrangement  = models.ForeignKey(Iv_arrangement, on_delete=models.CASCADE)
    Placement_initiative =models.ForeignKey(Placement_initiative, on_delete=models.CASCADE)
    organising_online_offline_fdp = models.ForeignKey(Organising_online_offline_fdp, on_delete=models.CASCADE)


                        # FACULTY ATTENDANCE

class Proper_procedure(models.Model):
    numbers = models.IntegerField()
    total_wrk_days = models.IntegerField()
    calc_in_per = models.FloatField()

class Eme_with_altr(models.Model):
    numbers = models.IntegerField()
    total_wrk_days = models.IntegerField()
    calc_in_per = models.FloatField()

class Eme_without_altr(models.Model):
    numbers = models.IntegerField()
    total_wrk_days = models.IntegerField()
    calc_in_per = models.FloatField()
class Faculty_Attendance(models.Model):
    proper_procedure = models.ForeignKey(Proper_procedure, on_delete=models.CASCADE)
    eme_with_altr = models.ForeignKey(Eme_with_altr, on_delete=models.CASCADE)
    eme_without_altr = models.ForeignKey(Eme_without_altr, on_delete=models.CASCADE)


                                #  CONTRIBUTION TO DEPT AND INST.

class Hod_Convener_of_committe(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details = models.CharField(max_length=200)

class Dept_co_ordinator(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details = models.CharField(max_length=200)

class Contibution_during_emergencies(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details = models.CharField(max_length=200)

class Admission_promotion(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details = models.CharField(max_length=200)

class Worthy_contribution(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details = models.CharField(max_length=200)

class Appreciation(models.Model):
    target = models.IntegerField()
    achieved = models.IntegerField()
    details = models.CharField(max_length=200)

class Contribution(models.Model):
    Hod_Convener_of_committe = models.ForeignKey(Proper_procedure, on_delete=models.CASCADE)
    dept_co_ordinator = models.ForeignKey(Dept_co_ordinator, on_delete=models.CASCADE)
    contibution_during_emergencies = models.ForeignKey(Contibution_during_emergencies, on_delete=models.CASCADE)
    admission_promotion = models.ForeignKey(Admission_promotion, on_delete=models.CASCADE)
    worthy_contribution = models.ForeignKey(Worthy_contribution, on_delete=models.CASCADE)
    appreciation = models.ForeignKey(Appreciation, on_delete=models.CASCADE)



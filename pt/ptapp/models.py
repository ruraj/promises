from django.contrib.auth.models import User
from django.db import models


class BaseTimeModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PromiseUsers(BaseTimeModel):
    user = models.OneToOneField(User, blank=False, null=False)

    def __str__(self):
        return self.user.username


class Promise(BaseTimeModel):
    promise = models.CharField(max_length=1000, blank=False, null=False)
    private = models.BooleanField(default=False)
    promise_maker = models.ForeignKey(PromiseUsers, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    deadline = models.DateTimeField(blank=False, null=False)


class PromiseState(BaseTimeModel):
    promise = models.ForeignKey(Promise, blank=False, null=False)
    state_description = models.CharField(max_length=1000, blank=False, null=False)


class Comments(BaseTimeModel):
    comments = models.CharField(max_length=1000, blank=False, null=False)
    commenter = models.ForeignKey(PromiseUsers, blank=False, null=False)


class PromiseComments(Comments):
    promise = models.ForeignKey(Promise, blank=False, null=False)


class PromiseStateComments(Comments):
    promise_state = models.ForeignKey(PromiseState, blank=False, null=False)

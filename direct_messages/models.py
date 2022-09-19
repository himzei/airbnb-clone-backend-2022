from argparse import ONE_OR_MORE
from django.db import models
from common.models import CommonModel 

class ChattingRoom(CommonModel): 

  users = models.ManyToManyField("users.User")

  def __str__(self): 
    return "Chatting Room."


class Message(CommonModel): 

  text = models.TextField() 
  user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True)
  room = models.ForeignKey("direct_messages.ChattingRoom", on_delete=models.CASCADE)

  def __str__(self): 
    return f"{self.user} says: {self.text}"
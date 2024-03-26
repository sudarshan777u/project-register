from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review

@receiver(post_save, sender=Review)
def send_email_on_save(sender, instance, **kwargs):
    subject = 'Review Details'
    message = (
                f'Name: {instance.user_name.Name}\n'
                f'Moral Character: {instance.Moral_character}\n'
                f'Punctuality: {instance.punctuality}\n'
                f'Health: {instance.health}\n'
                f'Behaviour: {instance.behaviour}\n'
                f'Attitude: {instance.attitude}\n'
                f'Career Goals: {instance.Career_goals}\n'
                f'Understanding Level: {instance.understanding_level}\n'
                f'Positive Attitude and mind: {instance.possitive_attitude_and_mind}\n'
                f'Executive: {instance.executive}\n'
                f'Responsibility: {instance.responsibility}\n'
                f'Response Ability: {instance.response_ability}\n'
                f'Team Handling: {instance.team_handling}\n'
                f'Planning: {instance.planing}\n'
                f'Communication Ability: {instance.communicate_ability}\n'
                f'Passion: {instance.passion}\n'
                f'Confidence: {instance.confidence}\n'
                f'Professional Background: {instance.profissional_background}\n'
                f'Work Experience: {instance.work_experience}\n'
                f'Knowledge Level: {instance.knowledge_level}\n'
                f'English Skills: {instance.english_skils}\n'
                f'Other Languages: {instance.other_languages}\n'
                f'Consider to Client: {instance.consider_to_client}\n'
                f'Internal Hiring: {instance.Internal_hiring}\n'
                f'Reject: {instance.reject}\n'
                f'Created At: {str(instance.created_at)[:18]}\n'
                f'Remarks: {instance.remarks}\n')


    from_email = "jeroldraja12@gmail.com"
    recipient_list = ["chembakurusudarshanreddy@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)

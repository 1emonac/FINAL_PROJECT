from django.db import models

class Question(models.Model):
    text = models.TextField(help_text="Enter the question text.")
    question_type = models.CharField(max_length=20, choices=(('text', 'Text'), ('choice', 'Choice'), ('multiple', 'Multiple')))

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_response = models.TextField(blank=True, null=True)
    choice_responses = models.ManyToManyField(Choice, blank=True)
    user_id = models.IntegerField()

    def __str__(self):
        responses = self.choice_responses.all()
        if self.text_response:
            return self.text_response
        elif responses:
            return ', '.join([choice.choice_text for choice in responses])
        else:
            return 'No response'

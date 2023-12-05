from django.db import models


class Expression(models.Model):
    expression_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.expression_text

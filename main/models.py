from django.db import models


class Ticket(models.Model):
    class Statusticket(models.TextChoices):
        OPEN = 'o', 'Open'
        CLOSED = 'c', 'Closed'
        FROZEN = 'f', 'Frozen'

    name = models.CharField(verbose_name='ticket', max_length=255)
    creator = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='creator_ticket',
        verbose_name='Creator'
    )
    created_at = models.DateField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateField(auto_now=True, verbose_name='Update')
    status = models.CharField(max_length=3,
                              verbose_name='Status',
                              choices=Statusticket.choices,
                              default=Statusticket.OPEN)

    def __str__(self):
        return f' Creator - {self.creator}\
                  Ticket - {self.name} \
                  Status - {self.status}'

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['-created_at']


class Message(models.Model):
    text = models.TextField(verbose_name='Message')
    ticket = models.ForeignKey(Ticket,
                               on_delete=models.CASCADE,
                               related_name='ticket_message',
                               verbose_name='ticket')
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE,
                               verbose_name='Author',
                               related_name='author')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Creator')

    def __str__(self):
        return f'Message - {self.ticket} \
                            {self.author}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'message'
        verbose_name_plural = 'messages'

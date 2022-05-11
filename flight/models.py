from django.utils.translation import gettext as _
from django.db import models
from django.db.models import Model, UniqueConstraint
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import datetime
from data import cities
import random, string


CLASSES = [
    ("E", "Economy"),
    ("B", "Business"),
    ("F", "First"),
]


class Passenger(Model):
    """
    A model represents the entity of passenger.
    it has the field `pssn` as primary key.
    """

    class Meta:
        verbose_name = _("passenger")
        verbose_name_plural = _("passengers")

    pssn = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    special_need = models.BooleanField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"pssn: {self.pssn} - {self.first_name}"


class ClassInfo(Model):
    """
    A model represents the entity of classes: Economy, Business, First.
    the primary key is the django default `id`.
    """

    class Meta:
        verbose_name = _("class info")
        verbose_name_plural = _("classes info")

    type = models.CharField(max_length=30, choices=CLASSES)
    total_seats = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.id} - {self.type}"


class Aircraft(Model):
    """
    A model represents the entity of Aircraft.
    it has the field `model` as primary key.
    """

    model = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=50)
    class_info = models.ManyToManyField(
        ClassInfo, through="HasClass", through_fields=("aircraft", "class_info")
    )

    class Meta:
        verbose_name = _("aircraft")
        verbose_name_plural = _("aircrafts")

    def __str__(self):
        return f"{self.type} - {self.model}"


class HasClass(Model):
    """
    This an intermediary model for m2m relation
    between: Aircraft & ClassInfo.
    `id` is the primary key.
    """

    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    class_info = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.aircraft} - {self.class_info}"


class Plane(Model):
    """
    A model represents the Plane entity
    the primary key is the django default `id`.
    """

    class Meta:
        verbose_name = _("plane")
        verbose_name_plural = _("planes")

    first_flight = models.DateField(auto_now=False, auto_now_add=False)
    total_seats = models.IntegerField()
    last_maintenance = models.DateField(auto_now=False, auto_now_add=False)
    next_maintenance = models.DateField(auto_now=False, auto_now_add=False)

    model = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}"


class Flight(Model):
    """
    A model represents the Flight entity
    the primary key is the django default `flight_code`.

    Objects of this models should be created by an adimn, with
    appropriate unique `flight_code`.
    """

    code = models.CharField(max_length=10, primary_key=True)  # flight_code
    date = models.DateField(auto_now=False, auto_now_add=False)  # flight_date
    time = models.TimeField(auto_now=False, auto_now_add=False)
    delay = models.DurationField(blank=True, default=datetime.timedelta())
    destination = models.CharField(max_length=50, choices=cities)
    source_city = models.CharField(max_length=50, choices=cities)
    active = models.BooleanField()

    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return f"Flight Code: {self.code}"


class WaitingList(Model):
    """
    A model represents the waiting_list entity type.
    `id` is the primary key.
    """

    class Meta:
        verbose_name = _("waiting list")
        verbose_name_plural = _("waiting lists")

    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)  # pssn
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)  # flight_code
    class_type = models.CharField(max_length=30, choices=CLASSES)

    def __str__(self):
        return f"ID: {self.id} - Passenger: {self.passenger}"


class Payment(Model):
    """
    A model represents the Payment_Method entity
    the primary key is the django default `id`
    """

    tax = models.FloatField()

    class Meta:
        verbose_name = _("payment")
        verbose_name_plural = _("payments")

    def __str__(self):
        return f"ID: {self.id}"


class CashMethod(Model):

    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"For Payment: {self.payment}"


class ApplePayMethod(Model):

    apple_id = models.IntegerField()
    device = models.CharField(max_length=50)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.payment


class PaypalMethod(Model):

    account_id = models.CharField(max_length=100)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.payment


class CreditCardMethod(Model):

    name = models.CharField(max_length=100)
    number = models.IntegerField()
    expire_date = models.DateField(auto_now=False, auto_now_add=False)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.payment


class Ticket(Model):
    """
    A model represents the Ticket entity
    the primary key is the django default `id`
    """

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
        constraints = [
            models.UniqueConstraint("seat_number", "flight", name='ticket_constraint')
        ]


    code = models.CharField(max_length=6, unique=True, blank=True)
    checked_in = models.BooleanField(default=False)
    seat_number = models.CharField(max_length=3)
    gate = models.CharField(max_length=50)
    class_type = models.CharField(max_length=50, choices=CLASSES)
    weight = models.FloatField()
    volume = models.FloatField()
    qunatity = models.IntegerField()
    successful = models.BooleanField()
    purchase_date = models.DateField(auto_now=False, auto_now_add=True)
    cost = models.FloatField()

    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)  # pssn
    transaction = models.ForeignKey(Payment, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket ID: {self.code} - Checked In: {self.checked_in} - Class Type: {self.class_type}"


def get_random_unique_code():
    exists = True
    while exists:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        exists = Ticket.objects.filter(code=code).exists()
        if not exists:
            return code

@receiver(post_save, sender=Ticket)
def create_profile(sender, instance, created, **kwargs):

    if created:
        instance.code = get_random_unique_code()
        instance.save()

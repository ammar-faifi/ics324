from ast import For
from re import L
from django.utils.translation import gettext as _
from django.db.models import *

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

    pssn = BigAutoField(max_length=10, primary_key=True)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    birth_date = DateField(auto_now=False, auto_now_add=False)
    phone = CharField(max_length=13)
    address = CharField(max_length=50)
    special_need = BooleanField()


class ClassInfo(Model):
    """
    A model represents the entity of classes: Economy, Business, First.
    the primary key is the django default `id`.
    """

    class Meta:
        verbose_name = _("class info")
        verbose_name_plural = _("classes info")


    type = CharField(max_length=30, choices=CLASSES)
    total_seats = IntegerField()
    price = FloatField()


class Aircraft(Model):
    """
    A model represents the entity of Aircraft.
    it has the field `model` as primary key.
    """

    model = CharField(max_length=50, primary_key=True)
    type = CharField(max_length=50)
    class_info = ManyToManyField(
        ClassInfo, through="HasClass", through_fields=("class_id", "aircraft_model")
    )

    class Meta:
        verbose_name = _("aircraft")
        verbose_name_plural = _("aircrafts")

    def __str__(self):
        return self.type


class HasClass(Model):
    """
    This an intermediary model for m2m relation 
    between: Aircraft & ClassInfo.
    `id` is the primary key.
    """

    aircraft_model = ForeignKey(Aircraft)
    class_id = ForeignKey(ClassInfo)


class Plane(Model):
    """
    A model represents the Plane entity
    the primary key is the django default `id`.
    """

    class Meta:
        verbose_name = _("plane")
        verbose_name_plural = _("planes")

    first_flight = DateField(auto_now=False, auto_now_add=False)
    total_seats = IntegerField()
    last_maintenance = DateField(auto_now=False, auto_now_add=False)
    next_maintenance = DateField(auto_now=False, auto_now_add=False)

    model = ForeignKey(Aircraft, on_delete=CASCADE)

    def __str__(self):
        return self


class Flight(Model):
    """
    A model represents the Flight entity
    the primary key is the django default `flight_code`.

    Objects of this models should be created by an adimn, with
    appropriate unique `flight_code`.
    """

    code = CharField(max_length=10, primary_key=True)  # flight_code
    date = DateField(auto_now=False, auto_now_add=False)  # flight_date
    delay = DurationField()
    destination = CharField(max_length=50)
    source_city = CharField(max_length=50)
    active = BooleanField()

    plane = ForeignKey(Plane, on_delete=CASCADE)

class WaitingList(Model):
    """
    A model represents the waiting_list entity type.
    `id` is the primary key.
    """

    class Meta:
        verbose_name = _("waiting list")
        verbose_name_plural = _("waiting lists")

    passenger = ForeignKey(Passenger, on_delete=CASCADE)  # pssn
    flight = ForeignKey(Flight, ) # flight_code
    class_ = CharField(max_length=30, choices=CLASSES)



class Payment(Model):
    """
    A model represents the Payment_Method entity
    the primary key is the django default `id`
    """

    tax = FloatField()

    class Meta:
        verbose_name = _("payment method")
        verbose_name_plural = _("payment methods")

    def __str__(self):
        return self.name


class CashMehothod(Model):

    payment = ForeignKey(Payment, on_delete=CASCADE, primary_key=True)


class ApplePayMehothod(Model):

    apple_id = IntegerField()
    device = CharField(max_length=50)
    payment = ForeignKey(Payment, on_delete=CASCADE, primary_key=True)


class PaypalMehothod(Model):

    account_id = CharField(max_length=100)
    payment = ForeignKey(Payment, on_delete=CASCADE, primary_key=True)


class CreditCardMehothod(Model):

    name = CharField(max_length=100)
    number = IntegerField()
    expire_date = DateField(auto_now=False, auto_now_add=False)
    payment = ForeignKey(Payment, on_delete=CASCADE, primary_key=True)


class Ticket(Model):
    """
    A model represents the Ticket entity
    the primary key is the django default `id`
    """

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")

    checked_in = BooleanField(default=False)
    seat_number = AutoField(unique=True)
    gate = CharField(max_length=50)
    class_ = CharField(max_length=50)
    weight = FloatField()
    volume = FloatField()
    qunatity = IntegerField()
    successful = BooleanField()
    purchase_date = DateField(auto_now=False, auto_now_add=True)
    amount = FloatField()

    passenger = ForeignKey(Passenger, on_delete=CASCADE)  # pssn
    transaction = ForeignKey(Payment, on_delete=CASCADE)
    flight = ForeignKey(Flight, on_delete=CASCADE)

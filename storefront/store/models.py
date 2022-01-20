from django.db import models



class Product(models.Model):
    title=models.CharField(max_length=255)
    Description=models.TextField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    inventory=models.IntegerField()
    collection=models.ForeignKey(Collection, on_delete=models.CASCADE)
    
class Order(models.Model):
    payment_pending="pending"
    payment_succesful="succesful"
    payment_failed="failed"

    payment_options=[
        (payment_pending,"P"),
        (payment_succesful,"S"),
        (payment_failed,"F")
    ]
    payment_status=models.CharField(_(choices=payment_options), max_length=250,default=payment_pending)
    placed_at=models.DateTimeField(auto_now=True, auto_now_add=True)

    



class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    surname=models.CharField(_(""), max_length=50)
    emailaddress=models.EmailField(_(""), max_length=254)
    phonenumber=models.name = models.CharField(max_length=255)


class Collection(models.Model):
    title=name = models.CharField(max_length=255)
    
class Order(models.Model):
    product=models.ForeignKey(Product, verbose_name=_(""), on_delete=models.CASCADE)


class Cart(models.Model):
    
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    
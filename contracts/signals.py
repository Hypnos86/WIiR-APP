from django.db.models.signals import pre_save
from django.dispatch import receiver
from contracts.models import ContractAuction
from decimal import Decimal


@receiver(pre_save, sender=ContractAuction)
def calculate_security_sum(sender, instance, **kwargs):
    instance.security_sum = instance.price * instance.security_percent * Decimal(0.01)

# TODO usunąć po zrobieniu view contract
# @receiver(post_save, sender=ContractAuction)
# def create_guarantee_settlement(sender, instance, **kwargs):
#     guranatee = instance.guarantee_settlement
#     if instance.last_report_date != 0:
#         if instance.guarantee.id == 2:
#             guranatee.contract_id = instance.id
#             last_date = instance.last_report_date
#             print(last_date)
#             days_30 = timedelta(days=30)
#             guranatee.dedline_settlement = last_date + days_30
#             print(guranatee.dedline_settlement)
#             guranatee.create(contract=instance.id, dedline_settlement=guranatee.dedline_settlement)
#             print(guranatee.values())

from datetime import datetime
from django.db.models import Q

from apps.client.models import Client
from apps.table.models import Table
from apps.reservation.models import Reservation


def mesa_ocupada(mesa_id, fecha_hora_inicio, fecha_hora_fin):
    reservaciones_existentes = Reservation.objects.filter(
        id_mesa=mesa_id
    ).exclude(
        Q(fecha_hora_fin__lte=fecha_hora_inicio) |
        Q(fecha_hora_inicio__gte=fecha_hora_fin)
    )

    return reservaciones_existentes.exists()

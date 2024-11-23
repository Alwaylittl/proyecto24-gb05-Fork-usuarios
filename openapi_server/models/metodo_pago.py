from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class MetodoPago(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, tipo_tarjeta=None, numero_tarjeta=None, fecha_expiracion=None, cvv=None):  # noqa: E501
        """MetodoPago - a model defined in OpenAPI

        :param id: The id of this MetodoPago.  # noqa: E501
        :type id: int
        :param tipo_tarjeta: The tipo_tarjeta of this MetodoPago.  # noqa: E501
        :type tipo_tarjeta: str
        :param numero_tarjeta: The numero_tarjeta of this MetodoPago.  # noqa: E501
        :type numero_tarjeta: str
        :param fecha_expiracion: The fecha_expiracion of this MetodoPago.  # noqa: E501
        :type fecha_expiracion: date
        :param cvv: The cvv of this MetodoPago.  # noqa: E501
        :type cvv: str
        """
        self.openapi_types = {
            'id': int,
            'tipo_tarjeta': str,
            'numero_tarjeta': str,
            'fecha_expiracion': date,
            'cvv': str
        }

        self.attribute_map = {
            'id': 'id',
            'tipo_tarjeta': 'tipoTarjeta',
            'numero_tarjeta': 'numeroTarjeta',
            'fecha_expiracion': 'fechaExpiracion',
            'cvv': 'cvv'
        }

        self._id = id
        self._tipo_tarjeta = tipo_tarjeta
        self._numero_tarjeta = numero_tarjeta
        self._fecha_expiracion = fecha_expiracion
        self._cvv = cvv

    @classmethod
    def from_dict(cls, dikt) -> 'MetodoPago':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MetodoPago of this MetodoPago.  # noqa: E501
        :rtype: MetodoPago
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this MetodoPago.


        :return: The id of this MetodoPago.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this MetodoPago.


        :param id: The id of this MetodoPago.
        :type id: int
        """

        self._id = id

    @property
    def tipo_tarjeta(self) -> str:
        """Gets the tipo_tarjeta of this MetodoPago.


        :return: The tipo_tarjeta of this MetodoPago.
        :rtype: str
        """
        return self._tipo_tarjeta

    @tipo_tarjeta.setter
    def tipo_tarjeta(self, tipo_tarjeta: str):
        """Sets the tipo_tarjeta of this MetodoPago.


        :param tipo_tarjeta: The tipo_tarjeta of this MetodoPago.
        :type tipo_tarjeta: str
        """
        allowed_values = ["Visa", "MasterCard", "American Express"]  # noqa: E501
        if tipo_tarjeta not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_tarjeta` ({0}), must be one of {1}"
                .format(tipo_tarjeta, allowed_values)
            )

        self._tipo_tarjeta = tipo_tarjeta

    @property
    def numero_tarjeta(self) -> str:
        """Gets the numero_tarjeta of this MetodoPago.


        :return: The numero_tarjeta of this MetodoPago.
        :rtype: str
        """
        return self._numero_tarjeta

    @numero_tarjeta.setter
    def numero_tarjeta(self, numero_tarjeta: str):
        """Sets the numero_tarjeta of this MetodoPago.


        :param numero_tarjeta: The numero_tarjeta of this MetodoPago.
        :type numero_tarjeta: str
        """

        self._numero_tarjeta = numero_tarjeta

    @property
    def fecha_expiracion(self) -> date:
        """Gets the fecha_expiracion of this MetodoPago.


        :return: The fecha_expiracion of this MetodoPago.
        :rtype: date
        """
        return self._fecha_expiracion

    @fecha_expiracion.setter
    def fecha_expiracion(self, fecha_expiracion: date):
        """Sets the fecha_expiracion of this MetodoPago.


        :param fecha_expiracion: The fecha_expiracion of this MetodoPago.
        :type fecha_expiracion: date
        """

        self._fecha_expiracion = fecha_expiracion

    @property
    def cvv(self) -> str:
        """Gets the cvv of this MetodoPago.


        :return: The cvv of this MetodoPago.
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv: str):
        """Sets the cvv of this MetodoPago.


        :param cvv: The cvv of this MetodoPago.
        :type cvv: str
        """

        self._cvv = cvv
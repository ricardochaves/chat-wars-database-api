import json
import os
from functools import wraps

from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate
from django.db.models import Prefetch
from django.http import JsonResponse

import jwt
from database.models import AuDigest
from database.models import Item
from database.models import Player
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from drf.serializers import AuDigestSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from six.moves.urllib import request as req


class AuDigestFilter(filters.FilterSet):
    item = filters.CharFilter(field_name="item__name", lookup_expr="icontains")

    class Meta:
        model = AuDigest
        fields = ["lot_id", "item", "condition", "end_at", "started_at", "status", "finished_at", "prince"]


class AuDigestViewSet(viewsets.ModelViewSet):
    queryset = (
        AuDigest.objects.prefetch_related(Prefetch("item", queryset=Item.objects.all()))
        .prefetch_related(Prefetch("buyer", queryset=Player.objects.all()))
        .prefetch_related(Prefetch("seller", queryset=Player.objects.all()))
    )

    filter_backends = (DjangoFilterBackend,)
    filterset_class = AuDigestFilter
    permission_classes = (IsAuthenticated,)

    serializer_class = AuDigestSerializer

    fields = (
        "lot_id",
        "item",
        "item_bonus",
        "seller",
        "quality",
        "seller_castle",
        "condition",
        "end_at",
        "started_at",
        "buyer_castle",
        "status",
        "finished_at",
        "buyer",
        "prince",
    )


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the access token
    Args:
        required_scope (str): The scope required to access the resource
    """

    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
            API_IDENTIFIER = os.environ.get("API_IDENTIFIER")
            jsonurl = req.urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json")
            jwks = json.loads(jsonurl.read())
            cert = "-----BEGIN CERTIFICATE-----\n" + jwks["keys"][0]["x5c"][0] + "\n-----END CERTIFICATE-----"
            certificate = load_pem_x509_certificate(cert.encode("utf-8"), default_backend())
            public_key = certificate.public_key()
            decoded = jwt.decode(token, public_key, audience=API_IDENTIFIER, algorithms=["RS256"])

            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({"message": "You don't have access to this resource"})
            response.status_code = 403
            return response

        return decorated

    return require_scope

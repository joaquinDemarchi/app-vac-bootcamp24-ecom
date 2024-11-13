from tabnanny import check
from django.shortcuts import render, redirect


def verificar_permisos():
    def deco_verificar_permisos(f):
        def check(request, *arg, **kwargs):
            if not request.user.is_superuser and not request.user.es_admin: #
                return redirect("error_permisos")
            return f(request, *arg, **kwargs)

        return check

    return deco_verificar_permisos

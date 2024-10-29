from django.shortcuts import render, redirect
from django.forms import modelformset_factory, modelform_factory

from . import models


def gerer_refus_lots(request):
    formset_class = modelformset_factory(
        models.RefusLot, fields=["candidat"], extra=1
    )

    if request.method == "POST":
        formset = formset_class(
            request.POST, queryset=models.RefusLot.objects.all()
        )
        if formset.is_valid():
            formset.save()

            return redirect("gerer_refus_lots")
    else:
        formset = formset_class(queryset=models.RefusLot.objects.all())
    return render(
        request,
        "exemple/gerer_refus_lots.html",
        {
            "formset": formset,
        },
    )


def creer_candidat(request):
    form_class = modelform_factory(models.Cocontractant, fields=["nom"])
    formset_class = modelformset_factory(
        models.RefusLot, fields=["candidat"], extra=1
    )

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            form.save()

            return render(
                request,
                "exemple/gerer_refus_lots.html#form-candidat-fields",
                {
                    "formset": formset_class(
                        queryset=models.RefusLot.objects.all()
                    )
                },
            )
    else:
        form = form_class()
    return render(
        request,
        "exemple/gerer_refus_lots.html#form-nouveau-candidat",
        {
            "form": form,
        },
    )

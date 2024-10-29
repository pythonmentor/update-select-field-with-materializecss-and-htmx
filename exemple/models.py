from django.db import models


class Cocontractant(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"Cocontractant: {self.nom}"


class RefusLot(models.Model):
    candidat = models.ForeignKey(
        "Cocontractant", on_delete=models.CASCADE, null=True, blank=True
    )
    lettre_refus = models.FileField(
        upload_to="marches/refus_lots/",
        verbose_name="Lettre de refus",
        blank=True,
    )

    def __str__(self):
        return f"RefusLot d'id {self.id}"

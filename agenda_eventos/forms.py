from django import forms


class EntryForm(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateTimeField()
    description = forms.CharField(widget=forms.Textarea)


class ClientForm(forms.Form):
    Nombre_client = forms.CharField(max_length=45)
    LastName_client = forms.CharField(max_length=45)
    Phone_client = forms.CharField(max_length=45)
    email_client = forms.CharField(max_length=45)
    otherData_client = forms.Textarea()


class FormClasificacionEvento(forms.Form):
    Clasificacion_evento = forms.CharField(max_length=45)


class FormEvento(forms.Form):
    NombreEvento = forms.CharField(max_length=45)
    CodigoEvento = forms.CharField(max_length=45)


class FormDetalleEvento(forms.Form):
    FechaInicio = forms.DateTimeField()
    FechaFin = forms.DateTimeField()
    ClasificacionEvento_idClasificacionEvento = forms.CharField(max_length=45)
    Evento_idEvento = forms.CharField(max_length=45)


class FormEventoCliente(forms.Form):
    ClienteIdCliente = forms.CharField(max_length=45)
    EventoIdEvento = forms.CharField(max_length=45)


class FormMaterial(forms.Form):
    CodigoMaterial = forms.CharField(max_length=45)
    nombreMaterial = forms.CharField(max_length=45)
    CantidadIdeal = forms.IntegerField()
    CantidadInicial = forms.IntegerField()


class FormEventoMaterial(forms.Form):
    EventoIdEvento = forms.CharField(max_length=45)
    MaterialIdMaterial = forms.CharField(max_length=45)

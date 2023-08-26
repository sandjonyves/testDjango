from rest_framework import serializers
from .models  import DataReact,DataEncadreur

from .models import DataReact,DataEncadreur


class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = DataReact
        fields = ('id','name','ville','quartier','niveau', 'classe','matiere','jours','heure','numTel','addEmail','addresse','taux','Price')


class DataSerializersE(serializers.ModelSerializer):

    class Meta : 
        model = DataEncadreur
        fields = ('id','name','prenom','numTel' , 'addEmail','untEnseignaement')
  
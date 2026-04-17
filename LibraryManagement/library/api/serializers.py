from django.db.models.base import ValidationError
from rest_framework import serializers
from library.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    name_len = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = '__all__' # ['name',]

    def get_name_len(self,object):
        return (len(object.name))

    def validate(self,data):
        if len(data['name']) < 3:
            raise serializers.ValidationError("Name is too short.")
        else:
            return data


'''
# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Name is too short.")
#     else:
#         return value

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(validators=[name_length])
    name = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    # def validate(self,data):
        # if data['name'] == data['field2']:
        #     raise serializers.ValidationError("should be different")
        # else:
        #      return data

    def validate_name(self,value):
        if len(value) < 3:
            raise serializers.ValidationError("Name is too short.")
        else:
            return value
'''

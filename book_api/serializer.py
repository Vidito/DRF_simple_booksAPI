from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
    
    # If you want to validate a specific field like title
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters")
        return value

    # If you want to validate a whole object
    def validate(self, data):
        if data['number_of_pages'] < 100:
            raise serializers.ValidationError("Number of pages must be at least 100")
        return data
    

    def get_description(self, data):
        return f"{data.title} is written by {data.author} and published in {data.publish_date}. It has {data.number_of_pages} pages."
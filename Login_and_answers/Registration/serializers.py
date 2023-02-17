from rest_framework import serializers
from .models import User_Details, Answer
import re
from datetime import date
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_Details
        fields=['Email','First_Name','Last_Name','DOB','Gender','password']
    def validate(self, data):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if len(data['Email'])<1:
            raise serializers.ValidationError({'error':'Email Cannot be Empty'})
        if len(data['First_Name'])<1:
            raise serializers.ValidationError({'error':'First Name Cannot be Empty'})
        if len(data['DOB'])<1:
            raise serializers.ValidationError({'error':'DOB Cannot be Empty'})
        if len(data['First_Name'])<2:
            raise serializers.ValidationError({'error':'Name cannot be less than 2 Letters'})
        if len(data['password']) < 8:
            raise serializers.ValidationError({'error':'Password Cannot be less than 8 Characters'})
        if not any(x.isdigit() for x in data['password']):
            raise serializers.ValidationError({'error':'Password Must contain atleast 1 Digit'})
        if not any(x.isupper() for x in data['password']):
            raise serializers.ValidationError({'error':'Password Must contain atleast 1 Uppercase Character'})
        if not any(x.islower() for x in data['password']):
            raise serializers.ValidationError({'error':'Password Must contain atleast 1 Lowercase Character'})
        if (regex.search(data['password'])==None)==True:
            raise serializers.ValidationError({'error':'Password Must contain atleast 1 Special Character i.e : #@%^&*)() etc'})
        if data['DOB']>=date.today():
            raise serializers.ValidationError({'error':'Date of Birth cant be today/ in the future'})

        
            
        return data
#hi
class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer 
        fields=['submission_id', 'user_id', 'question_id', 'option_choice','Attempt_time']
    def validate(self, data):
        if len(data['question_id'])<1:
            raise serializers.ValidationError({'error':'Question Id cannot be empty'})
        if len(data['user_id'])<1:
            raise serializers.ValidationError({'error':'User Id cannot be empty'})
        if len(data['submission_id'])<1:
            raise serializers.ValidationError({'error':'Submission Id cannot be empty'})
        return data
        
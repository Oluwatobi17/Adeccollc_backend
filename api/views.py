from django.http import HttpResponse
from .email_utils import send_custom_email
from django.views.generic import View

class SendFormEmail(View):
    def get(self, request):
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        email = request.GET.get('email', None)
        address = request.GET.get('address', None)
        phone = request.GET.get('phone', None)
        position = request.GET.get('position', None)

        data = "First Name: "+first_name+"\n Last Name: "+last_name+"\n Email: "+email+"\n Address: "+address+"\n Phone: "+phone+"\n Position: "+position;
        # """.format(first_name,last_name,email,address,phone);

        # print(data);
        subject = 'New Application'
        message = data;
        recipient_list = ['officialhardacre@gmail.com']  # Replace with the recipient's email addresses

        send_custom_email(subject, message, recipient_list)

        return HttpResponse("Email Send Successfully!");

class SendFormEmailAirMax(View):
    def get(self, request):
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        zipcode = request.GET.get('zipcode', None)
        email = request.GET.get('email', None)
        address = request.GET.get('address', None)
        phone = request.GET.get('phone', None)
        age = request.GET.get('age', None)
        nearest_nike = request.GET.get('nearest_nike', None)
        nearest_walmart = request.GET.get('nearest_walmart', None)

        data = " First Name: "+first_name+"\n Last Name: "+last_name+"\n Zipcode: "+zipcode+"\n Email: "+email+"\n Address: "+address+"\n Phone: "+phone+"\n Nearest Nike Store: "+nearest_nike+"\n Nearest Waltmart Store: "+nearest_walmart+"\n Age: "+age;
        # """.format(first_name,last_name,email,address,phone);

        # print(data);
        subject = 'New Application'
        message = data;
        recipient_list = ['hardycre.co@gmail.com']  # Replace with the recipient's email addresses

        send_custom_email(subject, message, recipient_list)

        return HttpResponse("Email Send Successfully!");

class SendFormEmailAirJordan(View):
    def get(self, request):
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        zipcode = request.GET.get('zipcode', None)
        email = request.GET.get('email', None)
        address = request.GET.get('address', None)
        phone = request.GET.get('phone', None)
        age = request.GET.get('age', None)
        nearest_nike = request.GET.get('nearest_nike', None)
        nearest_walmart = request.GET.get('nearest_walmart', None)

        data = " First Name: "+first_name+"\n Last Name: "+last_name+"\n Zipcode: "+zipcode+"\n Email: "+email+"\n Address: "+address+"\n Phone: "+phone+"\n Nearest Nike Store: "+nearest_nike+"\n Nearest Waltmart Store: "+nearest_walmart+"\n Age: "+age;
        # """.format(first_name,last_name,email,address,phone);

        # print(data);
        subject = 'New Application'
        message = data;
        recipient_list = ['aaddeex142@gmail.com']  # Replace with the recipient's email addresses

        send_custom_email(subject, message, recipient_list)

        return HttpResponse("Email Send Successfully!");

# def my_email_view(request):
#     # ... Your view logic ...
#     print("Job application received ", request.POST['email']);
#     return HttpResponse("Normal Email Send Successfully!")

    # subject = 'New Application'
    # message = 'This is a test email sent from Django.'
    # recipient_list = ['ganiuibrahim3000@gmail.com']  # Replace with the recipient's email addresses

    # send_custom_email(subject, message, recipient_list)

    # # ... Rest of your view logic ...
    # return HttpResponse("Normal Email Send Successfully!")

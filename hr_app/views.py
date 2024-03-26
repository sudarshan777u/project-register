from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , HttpResponse,redirect
from .models import registration

from datetime import datetime
from django.core.mail import send_mail 
from django.conf import settings 
from django.contrib import messages



def register(request):
    if request.method =="POST":
        name = request.POST.get("name")
        pc = request.POST.get("pc")
        sc = request.POST.get("sc")
        location = request.POST.get("location")
        email = request.POST.get("mail")
        cctc = request.POST.get("cctc")
        ectc = request.POST.get("ectc")
        np = request.POST.get("np")
        d = request.POST.get("d")
        applied_d = request.POST.get("ad")
        exp = request.POST.get("exp")
        g_skills = request.POST.get("g_skills")
        t_skills = request.POST.get("t_skills")  
        s_skills = request.POST.get("s_skills")
        Jps = request.POST.get("htkau")
        c_by = request.POST.get("cb")
        
        created_at = datetime.now()
        # Use the default manager's create() method to create a new registration object
        reg_obj = registration.objects.create(
            Name=name,
            Primary_contact=pc,
            Secondary_contact=sc,
            Location=location,
            Email_Id=email,
            Current_CTC=cctc,
            Expected_CTC=ectc,
            Notice_Period=np,
            Current_designation=d,
            Applied_designation=applied_d,
            experience=exp,
            General_Skills=g_skills,
            Technical_Skills=t_skills,
            Soft_Skills=s_skills,
            Job_portal_source=Jps,
            Contacted_by=c_by,
            created_at=created_at
            )
        print(settings.EMAIL_HOST_USER)
        send_mail(
            'Registration Details',
            f"Name: {name}\nPhone_number: {pc}\nEmail:{email}\n:Location: {location}\nGenaral Skills: {g_skills}\nTechnical Skills: {t_skills}\nSoft Skills: {s_skills}\nCurrent CTC: {cctc}\nNotice_Period: {np}\nCurrent_designation: {d}\nApplied_designation: {applied_d}\nExperience: {exp}\nJob Portal Source: {Jps}\nContacted By: {c_by}",
            settings.EMAIL_HOST_USER,
            [''],
            fail_silently=False,
            )
        return redirect("/success")

        # No need to call obj.save() separately, as create() method already saves the object to the database
        messages.success(request, 'Registration Successful')  # Add a success message

        # Redirect to the same page or another page as needed  
        
    return render(request,"form.html")

def success(request):
    return render(request,"success.html")
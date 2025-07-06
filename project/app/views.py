from django.shortcuts import render
from .models import Register,Login,Query
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("number")
        password=request.POST.get("password")
        confirmpassword=request.POST.get('confirmpassword')
        DOB=request.POST.get("date")
        gender=request.POST.get("gender")
        education=request.POST.get("education")
        profile=request.POST.get("profile")
        resume=request.POST.get("resume")
        user=Register.objects.filter(email=email)
        if user:
            # eml="email already exists"
            return render(request,'register.html')
        else:
            if confirmpassword==password:
                Register.objects.create(name=name,email=email,contact=contact,password=password,confirmpassword=confirmpassword,DOB=DOB,gender=gender,education=education,profile=profile,resume=resume)
                return render(request,'login.html')
            else:
                msg="password unmatched"
                return render(request,'register.html')
            
    else:
        return render(request,'register.html')
    

def login(request):
    return render(request,'login.html')

def logindata(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=Register.objects.filter(email=email)
        if user:
            userData=Register.objects.get(email=email)
            pass1=userData.password
            if password==pass1:
                data={'id':userData.id,'name':userData.name,'email':userData.email,'contact':userData.contact,'password':userData.password,'confirmpassword':userData.confirmpassword,"dob":userData.DOB,'gender':userData.gender,'education':userData.education,'profile':userData.profile,'resume':userData.resume}
                return render(request,'dashboard.html',{'data':data})
            else:
                return render(request,'login.html')
        else:
            return render(request,'register.html')
    else:
        return render(request,'register.html')
        
def dashboard(request):
    return render(request,'dashboard.html')

def query(request,pk):
    userdata=Register.objects.get(id=pk)
    data={'id':userdata.pk,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.DOB,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.profile,'file':userdata.resume} 
    return render(request,'dashboard.html',{'data':data,'query':pk})

def querydata(req,pk):
    if req.method=="POST":
        name = req.POST.get('name')
        email = req.POST.get('email')
        query = req.POST.get('query')
        Query.objects.create(name=name,email=email,query=query)
        userdata=Register.objects.get(email=email)
        data={'id':userdata.pk,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.DOB,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.profile,'file':userdata.resume} 
        return render(req,'dashboard.html',{'data':data})
        

def allquery(request,pk):
    userdata=Register.objects.get(id=pk)
    data={'id':userdata.pk,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.DOB,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.profile,'file':userdata.resume} 
    email=userdata.email
    aquery=Query.objects.filter(email=email)
    return render(request,'dashboard.html',{'data':data,'aquery':aquery})

# def edit(req,id,pk):
#     editdata=Query.objects.get(id=id)
#     userdata=Register.objects.get(email=editdata.email)
#     data={'id':userdata.pk,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.DOB,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.profile,'file':userdata.resume} 
#     return render(req,'dashboard.html',{'editdata':editdata,'data':data})
    
# def updatedata(req,id,pk):
#     if req.method=="POST":
#         name=req.POST.get('name')
#         email=req.POST.get("email")
#         query=req.POST.get("query")
#         olddata=Query.objects.get(id=id)
#         olddata.query=query
#         olddata.save()
#         userdata=Register.objects.get(email=email)
#         aquery=Query.objects.filter(email=email)
#         data={'id':userdata.id,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.DOB,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.profile,'file':userdata.resume} 
#         return render(req,'dashboard.html',{'data':data,'aquery':aquery})
from django.db.models import Q        
def search(request,pk):
    userdata=Register.objects.get(id=pk)
    data={'id':userdata.pk,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.DOB,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.profile,'file':userdata.resume} 
    sdata=request.POST.get('search')
    aquery=Query.objects.filter(Q(email=userdata.email) & Q(query__icontains=sdata))
    return render(request,'dashboard.html',{'aquery':aquery, 'data':data})


    
    
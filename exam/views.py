from datetime import datetime
from django.shortcuts import render, redirect
from .models import Class, Exam, Question, Option, AnswerSheet, Answer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from .forms import CreateuserForm
# Create your views here.

#custom functions here for reusability

def joinclass(class_code, user):
    class_obj = Class.objects.get(code=class_code)
    class_obj.students.add(user)
    class_obj.save()
    return '/home/class/'+class_obj.code


def landingPage(request):
    print(request.get_full_path())
    data = {}
    return render(request, 'landing.html', data)



def registrationView(request):
    form = CreateuserForm()
    if request.method == "POST":
        form = CreateuserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            print(form.errors)
    data = {"form": form}
    return render(request, 'auth/register.html', data)


def loginView(request):
    data = {}
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            data['error'] = "Invalid Credentials"
        
    return render(request, 'auth/login.html', data)


def logoutView(request):
    logout(request)
    return redirect('/login')

def changeView(request):
    data = {}
    
    if request.method=='POST':
        username = request.user.username
        current_password = request.POST['password']
        
        user = authenticate(request, username=username, password = current_password)
        
        if user is not None:
            
            current_user = User.objects.get(username=username)
            
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            
            if password1 == password2:
                current_user.set_password(password1)
                current_user.save() 
            else:
              data['error'] = "New Password and Confirm Password does not match!"
        else:
            data['error'] = "Current Password does not match."
            
    
    return render(request, 'reusable/change.html', data)






@login_required(login_url='/login')
def homeView(request):
    if request.method == "POST" and request.POST.get('action')== "create_class":
        class_name = request.POST.get('class_name')
        class_desc = request.POST.get('class_desc')
        class_obj = Class.objects.create(name=class_name, description=class_desc, teacher=request.user)
        class_obj.save()
        return redirect('/home/class/'+class_obj.code)

    elif request.method == "POST" and request.POST.get('action')== "join_class":
        return redirect(joinclass(request.POST.get('class_code'), request.user))

    classAsTeacher = Class.objects.filter(teacher=request.user.id)
    classAsStudent = Class.objects.filter(students = request.user.id)
    exams = Exam.objects.filter(classes__id__in = classAsStudent | classAsTeacher,date__range=[date.today(), datetime.now() + timedelta(days=365)])

    data  = {"classAsTeacher": classAsTeacher, "classAsStudent":classAsStudent, "exams": exams}
    return render(request, 'exam/home.html', data)

@login_required(login_url='/login')
def classView(request, class_code):
    if request.method == "POST":
        if request.POST.get('action')== "join_class":
            return redirect(joinclass(request.POST.get('class_code'), request.user))
        elif request.POST.get('action') == "deleteClass":
            class_obj = Class.objects.get(code=class_code)
            class_obj.delete()
            return redirect('/home')

        elif request.POST.get('action') == "editClass":
            class_obj = Class.objects.get(code=class_code.upper())
            class_obj.name = request.POST.get('class_name')
            class_obj.description = request.POST.get('class_desc')
            class_obj.save()
            return redirect('/home/class/'+class_code)
        elif request.POST.get('action') == "create_exam":
            exam_start_time = datetime.strptime(request.POST.get('exam_start_time'), '%H:%M')
            exam_obj = Exam.objects.create(name=request.POST.get('exam_name'), duration= int(request.POST.get('exam_duration')), instruction=request.POST.get('exam_instruction'), date=datetime.strptime(request.POST.get('exam_date'),'%Y-%m-%d'), start_time=exam_start_time, classes=Class.objects.get(code=class_code))
            exam_obj.save()
            return redirect('/home/exam/details/'+str(exam_obj.id))


    classes = Class.objects.get(code=class_code.upper())
    joined = request.user.id == classes.teacher.id or request.user.id in classes.students.values_list('id', flat=True)
    #filter upcomingexams according to exam_date
    exams = Exam.objects.filter(classes=classes.id, date__range=[datetime.now(), datetime.now() + timedelta(days=365)])
    archived_exams = Exam.objects.filter(classes=classes.id, date__range=[datetime.now() - timedelta(days=365), datetime.now()-timedelta(days=1)])
    teacher_status = request.user.id == classes.teacher.id
    teacher = {'status':teacher_status, 'color':{'primary': 'rose-200' if teacher_status else 'indigo-100', 'secondary': 'rose-300' if teacher_status else 'indigo-300'}}
    
    data = {"class":classes ,"exams": exams, "archived_exams": archived_exams, "joined": joined, "teacher": teacher}
    return render(request, 'exam/class.html', data)

@login_required(login_url='/login')
def examStart(request, exam_id):
    
    exam = Exam.objects.get(id=exam_id)
    class_obj = Class.objects.get(id=exam.classes.id)
    questions = Question.objects.filter(exam=exam.id)
    if(request.user.id == Exam.objects.get(id=exam_id).classes.teacher.id):
        return redirect('/home/exam/'+str(exam.id))
    started = True if exam.start_time <= datetime.now().time() and exam.date == datetime.now().date() else False
   
    submitted = True if AnswerSheet.objects.filter(exam=exam_id, student=request.user.id).exists() else False
    data = {"exam": exam, "class": class_obj, "questions": questions, "started": started,  'submitted': submitted}
    return render(request, 'exam/examStart.html', data)


@login_required(login_url='/login')
def examDetailsView(request, exam_code):

    exam_obj = Exam.objects.get(id=exam_code)
    class_obj = Class.objects.get(id=exam_obj.classes.id)
    if class_obj.teacher.id != request.user.id:
        return redirect('/home/exam/start/'+str(exam_code))
    questions = Question.objects.filter(exam=exam_obj.id)
    if request.method == "POST":
        if request.POST.get('action') == "updateexam":
            Exam.objects.filter(id=exam_code).update(name=request.POST.get('exam_name'), duration= int(request.POST.get('exam_duration')), instruction=request.POST.get('exam_instruction'), date=datetime.strptime(request.POST.get('exam_date'),'%Y-%m-%d'), start_time=datetime.strptime(request.POST.get('exam_start_time'), '%H:%M'))            
            return redirect('/home/exam/details/'+str(exam_code))
        elif request.POST.get('action') == "deletequestion":
            question_obj = Question.objects.get(id=request.POST.get('question_id'))
            question_obj.delete()
            return redirect('/home/exam/'+str(exam_code))
        elif request.POST.get('action') == "createquestion":
            qtype = request.POST.get('questiontype')
            if qtype == "SingleMCQ" or qtype == "MultipleMCQ":
                question = Question.objects.create(question=request.POST.get('question'), question_type=qtype, exam=exam_obj)
                question.save()
                for i in range(1,5):
                    temp = 'optioniscorrect' if qtype == 'SingleMCQ' else 'option'+str(i)+'iscorrect'
                    option = Option.objects.create(option=request.POST.get('option'+str(i)), is_correct=True if request.POST.get(temp) == str(i) else False)
                    option.save()
                    question.options.add(option)
            elif qtype == "TrueFalse":
                question = Question.objects.create(question=request.POST.get('question'), question_type=qtype, exam=exam_obj)
                question.save()
                option1 = Option.objects.create(option="True", is_correct=True if request.POST.get('truefalse') == "True" else False)
                option1.save()
                option2 = Option.objects.create(option="False", is_correct=True if request.POST.get('truefalse') == "False" else False)
                option2.save()
                question.options.add(option1, option2)
            elif qtype == "Subjective":
                question = Question.objects.create(question=request.POST.get('question'), question_type=qtype, exam=exam_obj)
                question.save()            
                option = Option.objects.create(option=request.POST.get('subjectiveanswer'), is_correct=True)
                option.save()
                return redirect('/home/exam/'+str(exam_obj.id))

    questions = Question.objects.filter(exam=exam_obj.id)
    data = {"class": class_obj, "exam": exam_obj, "questions": questions}
    return render(request, 'exam/examDetails.html', data)

@login_required(login_url='/login')
def examView(request, exam_id):
    if(request.user.id == Exam.objects.get(id=exam_id).classes.teacher.id):
        return redirect('/home/exam/details/'+str(exam_id))
    data = {}
    if not AnswerSheet.objects.filter(exam=exam_id, student=request.user.id).exists():
        AnswerSheet.objects.create(exam=Exam.objects.get(id=exam_id), student=request.user, status="STARTED")
    exam_obj = Exam.objects.get(id=exam_id)
    question_obj = Question.objects.filter(exam=exam_id)
    answersheet = AnswerSheet.objects.filter(exam=exam_id, student=request.user.id)
    if request.method == "POST":
        if request.POST.get('action') == "next":
            q = Question.objects.get(id=request.POST.get('question'))
            for o in q.options.all():
                if o.is_correct:
                    correct = 1 if o.option == request.POST.get('answer') else 0 
            a = Answer.objects.create(answersheet=answersheet[0], question=Question.objects.get(id=request.POST.get('question')), answer=request.POST.get('answer'),mark=correct, is_correct=True if correct == 1 else False, answered=True)
            a.save()
            AnswerSheet.objects.filter(exam=exam_id, student=request.user.id).update(mark = answersheet[0].mark + correct, total_marks = answersheet[0].total_marks + 1, percentage = (answersheet[0].mark + correct)/(answersheet[0].total_marks + 1)*100)
        elif request.POST.get('action') == "submit":
            AnswerSheet.objects.filter(exam=exam_id, student=request.user.id).update(status="SUBMITTED")
            return redirect('/home')
    done_answers = Answer.objects.filter(answersheet=answersheet[0].id, answered=True)
    done_questions = [x for x in done_answers.values_list('question', flat=True)]
    #print(done_questions)
    for question in question_obj:
        if question.id in done_questions:
            continue
        else:
            data = {"question": question, 'answersheet': answersheet[0].id,'total': question_obj.count()+1, 'done': done_answers.count()+1}
            break
    

    return render(request, 'exam/exam.html',data)



def reportcardView(request,exam_id, student_id=None):
    if request.user.id == Exam.objects.get(id=exam_id).classes.teacher.id and not student_id:

        exam = Exam.objects.get(id=exam_id)
        if AnswerSheet.objects.filter(student=request.user.id).exists():
            AnswerSheet.objects.filter(student = request.user.id).delete()
        answersheet = AnswerSheet.objects.filter(exam=exam)
        data = {"exam": exam, "answersheet": answersheet}
        return render (request, 'exam/reportcard.html', data)
    elif request.user.id == Exam.objects.get(id=exam_id).classes.teacher.id and student_id:
        student_id = student_id
    else:
        student_id = request.user.id
    
    student = User.objects.get(id=student_id)
    exam = Exam.objects.get(id=exam_id)
    questions = Question.objects.filter(exam=exam_id)
    if not AnswerSheet.objects.filter(exam=exam, student=student_id).exists():
        AnswerSheet.objects.create(exam=Exam.objects.get(id=exam_id), student=request.user, status="SUBMITTED")
    
    answersheet = AnswerSheet.objects.get(exam=exam, student=student_id)

    for question in questions:
        if not (Answer.objects.filter(answersheet=answersheet, question=question).exists()):
            Answer.objects.create(answersheet=answersheet, question=question, answer="Not Answered", mark=0, is_correct=False, answered=False)
    answersheet = AnswerSheet.objects.get(exam=exam, student=student_id)
    a = Answer.objects.filter(answersheet=answersheet)
    data = {"exam": exam, "answersheet": answersheet, "answers": a, "student": student}
    return render(request, 'exam/singlereportcard.html', data)
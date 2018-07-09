import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,server_username,server_password,
              smtpserver='smtp.gmail.com:587'):

    msg = MIMEMultipart('alternative')
    msg['From'] = from_addr
    msg['To'] = to_addr_list[0]
    msg['Subject'] = subject
    mimetext = MIMEText(message,'html','utf-8')
    msg.attach(mimetext)

    message = msg.as_string()
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(server_username,server_password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()


template_top = '''\
<html>
  <head></head>
  <body>
Hi,
'''
template_bottom = '''

</body>
</html>

'''


server_username = input('Enter Sender Email:')
server_password = input('Enter Sender password:')
to_address = input('Enter Receiver Email:')
subject = input('Enter Subject For Mail:')

todays_date = input("Enter today's date:")
todays_tasks = []
plans_for_tomorrow = []
doubts = []
while True:
    new_task = input('Is there new task?')
    if new_task == 'n':
        break
    t1 = input('Enter task:')
    todays_tasks.append(t1)

while True:
    new_task = input('Is there new task for tomorrow?')
    if new_task == 'n':
        break
    t1 = input('Enter Plan:')
    plans_for_tomorrow.append(t1)

while True:
    new_task = input('Is there any doubt?')
    if new_task == 'n':
        break
    t1 = input('Enter Doubt:')
    doubts.append(t1)

todays_date = '<h2>'+todays_date+'</h2>'
task_list_converted = ['<li>'+task+'</li>' for task in todays_tasks]
todays_tasks_converted = todays_date+'''<ul>'''+"".join(task_list_converted)+'''</ul>'''


plan_list_converted = ['<li>'+plan+'</li>' for plan in plans_for_tomorrow]
tomorrow_plans_converted = '''
    <h2>Plan for Tomorrow</h2>
    <ul>'''+"".join(plan_list_converted)+'''</ul>'''

doubt_list_converted = ['<li>'+doubt+'</li>' for doubt in doubts]
todays_doubts_converted = '''
    <h2>Requests/Doubts/Blockers</h2>
    <ul>'''+''.join(doubt_list_converted)+'''</ul>'''

template = template_top+todays_tasks_converted+tomorrow_plans_converted+todays_doubts_converted+template_bottom
print(template)


sendemail(from_addr    = server_username, 
          to_addr_list = [to_address],
          cc_addr_list = [], 
          subject      = subject, 
          message      = template,server_username='rhm.speakfood@gmail.com',server_password='RishabhHassanManjil123')

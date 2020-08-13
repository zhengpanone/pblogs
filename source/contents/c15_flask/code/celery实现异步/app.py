from flask import Flask
from celery import Celery

app = Flask(__name__)

app.config['SECRET_KEY'] = 'top-secret!'
# 配置消息代理路径,如果是在远程服务器上,则配置远程服务器中的redis的url
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# 要存储 Celery 任务的状态或运行结果时就必须要配置
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# 初始化Celery
celery = Celery(include=['app'], broker=app.config['CELERY_BROKER_URL'])
# 将Flask中的配置直接传递给Celery
celery.conf.update(app.config)


# 通过 celery.task 装饰器装饰耗时任务对应的函数
@celery.task
def long_task_do(arg1, arg2):
    time.sleep(10)
    print("done")

# bind=True 参数，这个参数会让 Celery 将 Celery本身传入，可以用于记录与更新任务状态。
@celery.task(bind=True)
def long_task(self):
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.radiant(10, 50)

    """for 迭代，迭代的逻辑没什么意义，
    就是随机从 list 中抽取一些词汇来模拟一些逻辑的运行，
    为了表示这是耗时逻辑，通过 time.sleep (1) 休眠一秒"""

    for i in range(total):
        if not message or random.random() < 0.25:
            # 随机的获取一些信息

            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective), random.choice(noun))
        # 更新Celery任务状态
        """
        每次获取一次词汇，就通过 self.update_state () 更新 Celery 任务的状态，
        Celery 包含一些内置状态，如 SUCCESS、STARTED 等等，这里使用了自定义状态「PROGRESS」，
        除了状态外，还将本次循环的一些信息通过 meta 参数 (元数据) 以字典的形式存储起来。
        有了这些数据，前端就可以显示进度条了。
        """
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total, 'status': message})
        time.sleep(1)

    return {'current': 100, 'total': 100, 'status': 'Task completed!', 'result': 42}


# Flask中定义接口通过异步的方式执行耗时任务
@app.route('/', methods=['GET', 'POST'])
def index():
    task = long_task_do.delay(1, 2)


# delay () 方法是 applyasync () 方法的快捷方式，applyasync () 参数更多，
# 可以更加细致的控制耗时任务，比如想要 long_task () 在一分钟后再执行

@app.route('/longtask', methods=['POST'])
def index_async():
    # 异步调用
    # task = log_task.apply_async(args=[1, 2], countdown=60)
    task = long_task.apppy_async()
    return jsonify({}), 202, {'Location': url_for('task_status',
                                                  task_id=task.id)}


# 前端通过 POST 请求到 /longtask，让后端开始去执行耗时任务
# delay () 与 apply_async () 会返回一个任务对象，该对象可以获取任务的状态与各种相关信息。
"""
返回的状态码为 202，202 通常表示一个请求正在进行中，
然后还在返回数据包的包头 (Header) 中添加了 Location 头信息，
前端可以通过读取数据包中 Header 中的 Location 的信息来获取任务 id 对应的完整 url。

前端有了任务 id 对应的 url 后，还需要提供一个接口给前端，让前端可以通过任务 id 去获取当前时刻任务的具体状态。
"""


@app.route('/status/<task_id>')
def task_status(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == "PENDING":  # 在等待
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':  # 没有失败
        response = {
            'state': task.state,  # 状态
            # meta中的数据，通过task.info.get()可以获得
            'current': task.info.get('current', 0),  # 当前循环进度
            'total': task.info.get('total', 1),
            # 总循环进度
            'status': task.info.get('status', '')
        }
    else:  # 后端执行任务出现了一些问题
        response = {
            'state': task.state, 'current': 1,
            'total': 1,
            'status': str(task.info),  # 报错的具体异常
        }
    return jsonify(response)


if __name__ == "__main__":
    app.run()
